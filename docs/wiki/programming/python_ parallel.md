---
layout: page
title: Parallel Computing Methods in Python
author: Yifei Zhu
comments: true
tags:
 - Programming
 - Python
---

## Categories

| Computing Type | Recommended Libraries & Modules |
|----------------|----------------------------------|
| **CPU-Intensive** | `multiprocessing`, `concurrent.futures.ProcessPoolExecutor`, `joblib` |
| **I/O-Intensive** | `threading`, `asyncio`, `concurrent.futures.ThreadPoolExecutor` |
| **Big Data Processing** | `dask`, `pyspark` |
| **Distributed Computing** | `ray`, `celery`, `mpi4py` |
| **GPU Computing** | `numba`, `cupy`, `pycuda` |
| **Web Concurrency** | `asyncio`, `tornado`, `gevent` |

**Selection Guidelines:**
- Use **process-based** parallelism for CPU-bound tasks (bypasses GIL)
- Use **thread-based** or **async** parallelism for I/O-bound tasks
- Choose **distributed frameworks** for large-scale data processing
- Use **GPU libraries** for hardware-accelerated computations
- Prefer **async frameworks** for high-concurrency web applications

### CPU-intensive parallel processing

| Feature | `multiprocessing.Pool` | `ProcessPoolExecutor` | `joblib.Parallel` |
|---------|------------------------|-----------------------|-------------------|
| **API Complexity** | Medium | Low (simplest) | Low (very simple) |
| **Flexibility** | High | Medium | Medium |
| **Error Handling** | Manual | Good (Future objects) | Good |
| **Memory Usage** | Medium | Medium | **Low** (better memory mgmt) |
| **Scikit-learn Integration** | No | No | **Yes** (native) |
| **Progress Tracking** | Manual | Manual | **Yes** (with verbose) |
| **Chunk Size Control** | **Yes** (fine-grained) | Limited | Automatic |
| **Learning Curve** | Steeper | Gentle | Gentle |
| **Backend Options** | No | No | **Yes** (loky, threading, multiprocessing) |

- **Start with `ProcessPoolExecutor`** for simplicity and clean code
- **Use `joblib`** for scientific computing and scikit-learn integration
- **Choose `multiprocessing.Pool`** when you need advanced control patterns
- **Prefer `joblib` with loky backend** for production systems and better memory management

