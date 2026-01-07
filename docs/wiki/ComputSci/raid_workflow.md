---
layout: page
title: Langroup Server Raid1
author: Yifei Zhu
comments: true
tags:
  - ComputSci
  - Ubuntu
  - Raid
---
2025.11.25 做 Langroup Server Raid1


✅ **目标流程**：
1. 把 `/media/langroup/Backup`（即 `sdb1`）上的数据**临时迁移到 `/home/langroup`**（空间足够）。
2. **清空 `sda` 和 `sdb`，创建 RAID 1**。
3. 将 RAID 卷格式化、挂载到 **`/media/langroup/Backup`**（保持原挂载点名）。
4. 把之前备份的数据**迁回**到这个 RAID 卷。
5. 后续用这个 RAID 卷**定期备份 Ubuntu 系统盘**（保留多版本）。
6. 
---

## 🔧 准备工作

### 1. 确认磁盘信息（再次核对！）

```bash
lsblk -f
df -h
```

你应该看到类似：
```
sda    8:0    0   3.6T  0 disk
sdb    8:16   0   3.6T  0 disk
└─sdb1 8:17   0   3.6T  ext4  /media/langroup/Backup
```

> ✅ 确保没有其他服务在用 sdb1（如 Docker、数据库、下载工具等）。

---

## 📦 第一步：迁移 sdb1 数据到临时位置

```bash
# 1. 创建目标目录（如果还没有）
sudo mkdir -p /home/langroup/backup_temp

# 2. 停止可能使用 Backup 的服务（按需）
# 例如：sudo systemctl stop你的服务

# 3. 复制所有数据（保留权限和属性）
sudo rsync -aAXv --progress /media/langroup/Backup/ /home/langroup/backup_temp/

# 4. 验证数据完整性（可选但推荐）
sudo diff -r /media/langroup/Backup/ /home/langroup/backup_temp/ | head -20

# 5. 卸载 sdb1
sudo umount /media/langroup/Backup

# 6. 删除旧挂载点（可选，后面会重建）
sudo rmdir /media/langroup/Backup
```

> ✅ 此时 sdb1 已卸载，数据安全保存在 `/home/langroup/backup_temp`

---

## 🧹 第二步：清空 sda 和 sdb（为 RAID 准备）

> ⚠️ **这会永久删除两个盘上所有数据！确保你已备份 sdb！**

```bash
# 清除分区表和 RAID/文件系统签名
sudo wipefs -a /dev/sda
sudo wipefs -a /dev/sdb

# 可选：清空前 100MB（更彻底）
sudo dd if=/dev/zero of=/dev/sda bs=1M count=100
sudo dd if=/dev/zero of=/dev/sdb bs=1M count=100
```

> 💡 `wipefs` 通常就够了，`dd` 是保险做法（如果你有时间）。

---

## 🔗 第三步：创建 RAID 1

```bash
# 1. 安装 mdadm（Ubuntu 通常自带，但确认下）
sudo apt update
sudo apt install mdadm

# 2. 创建 RAID 1 阵列（使用整个磁盘，不分区）
sudo mdadm --create --verbose /dev/md0 --level=1 --raid-devices=2 /dev/sda /dev/sdb

# 3. 查看 RAID 状态（同步会后台进行，可能需要几小时）
cat /proc/mdstat

# 示例输出：[UU] 表示正常，[_U] 表示正在同步
```

> 🕒 **RAID 同步期间不要重启**！可以用 `watch -n 5 cat /proc/mdstat` 监控进度。

---

## 💾 第四步：格式化 RAID 卷并挂载到 `/media/langroup/Backup`

```bash
# 1. 格式化为 ext4（推荐）或 btrfs（如需快照）
sudo mkfs.ext4 -L BACKUP_RAID /dev/md0

# 2. 创建挂载点
sudo mkdir -p /media/langroup/Backup

# 3. 临时挂载测试
sudo mount /dev/md0 /media/langroup/Backup

# 4. 设置开机自动挂载
# 先获取 UUID
sudo blkid /dev/md0

# 假设输出：/dev/md0: UUID="abcd1234..." TYPE="ext4"
# 编辑 /etc/fstab
echo 'UUID=abcd1234... /media/langroup/Backup ext4 defaults 0 2' | sudo tee -a /etc/fstab

# 5. 保存 RAID 配置（重要！否则重启后 RAID 可能失效）
sudo mdadm --detail --scan | sudo tee -a /etc/mdadm/mdadm.conf
sudo update-initramfs -u
```

✅ 现在 `/media/langroup/Backup` 就是你的 RAID 1 卷了。

---

## 🔄 第五步：把数据迁回

```bash
# 1. 复制回 RAID 卷
sudo rsync -aAXv --progress /home/langroup/backup_temp/ /media/langroup/Backup/

# 2. 验证（可选）
ls -l /media/langroup/Backup/

# 3. 删除临时数据（确认无误后再删！）
sudo rm -rf /home/langroup/backup_temp
```

---

## 🖥️ 第六步：设置 Ubuntu 系统盘定期备份（多版本）

假设你的系统根目录是 `/`（通常如此），系统盘可能是 NVMe（如 `/dev/nvme0n1p2`），但我们**不需要知道设备名，只备份 `/` 目录内容**。

### 创建备份脚本

```bash
sudo mkdir -p /media/langroup/Backup/system-backups

# 创建备份脚本
sudo tee /usr/local/bin/backup-system.sh <<'EOF'
#!/bin/bash
BACKUP_ROOT="/media/langroup/Backup/system-backups"
DATE=$(date +%Y%m%d-%H%M)

# 创建新备份目录
DEST="$BACKUP_ROOT/system-backup-$DATE"
sudo rsync -aAXv --delete \
  --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found","/home/*/.cache/*"} \
  / "$DEST/"

# 可选：只保留最近 4 个备份
(ls -1t "$BACKUP_ROOT"/system-backup-* | tail -n +5) | while read old; do
  [ -d "$old" ] && sudo rm -rf "$old"
done

echo "Backup completed: $DEST"
EOF

# 赋予执行权限
sudo chmod +x /usr/local/bin/backup-system.sh
```

### 设置定时任务（每周日 2:00 AM）

```bash
# 编辑 root 的 cron（因为需要备份 /）
sudo crontab -e
```

添加一行：
```cron
0 2 * * 0 /usr/local/bin/backup-system.sh >> /var/log/system-backup.log 2>&1
```

> ✅ 这样每周会生成一个带时间戳的系统备份，并自动删除旧的，只留最新的 4 个。

---

## ✅ 最终验证

- 重启系统，确认 `/media/langroup/Backup` 自动挂载 ✔️  
- 检查 `cat /proc/mdstat` 看 RAID 是否正常 ✔️  
- 手动运行一次 `/usr/local/bin/backup-system.sh` 看是否成功 ✔️  

---

## 🔒 补充建议

- **监控 RAID 健康**：可安装 `smartmontools` + 配置邮件告警（进阶）
- **不要把 /home 备份进系统镜像**：如果你的 `/home` 很大，建议单独备份用户数据（用 `rsync /home` 到另一个目录）
- **恢复系统时**：可用 Ubuntu Live USB + `rsync` 或 `dd` 还原
