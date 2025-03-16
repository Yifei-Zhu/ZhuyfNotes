#!/usr/bin/env python3
import os
import frontmatter
from datetime import datetime
from collections import defaultdict

WIKI_DIR = 'docs/wiki'
TIMELINE_FILE = 'docs/wiki/timeline.md'
EXCLUDE_FILES = {'timeline.md', 'tags.md'}

def get_wiki_files():
    """Get all markdown files in the wiki directory."""
    wiki_files = []
    for root, _, files in os.walk(WIKI_DIR):
        for file in files:
            if file.endswith('.md') and file not in EXCLUDE_FILES:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, WIKI_DIR)
                wiki_files.append(rel_path)
    return wiki_files

def parse_wiki_file(file_path):
    """Parse a wiki file to get its metadata and description."""
    full_path = os.path.join(WIKI_DIR, file_path)
    with open(full_path, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)
    
    # Get date from frontmatter or file modification time
    date = post.get('date', datetime.fromtimestamp(os.path.getmtime(full_path)))
    if isinstance(date, str):
        date = datetime.strptime(date, '%Y-%m-%d')
    
    # Get title from frontmatter or filename
    title = post.get('title', os.path.splitext(os.path.basename(file_path))[0].replace('_', ' ').title())
    
    # Get description from frontmatter or first paragraph
    description = post.get('description', '')
    if not description and post.content:
        paragraphs = [p for p in post.content.split('\n\n') if p.strip()]
        if paragraphs:
            description = paragraphs[0].replace('\n', ' ').strip()
            if len(description) > 150:
                description = description[:147] + '...'
    
    return {
        'date': date,
        'title': title,
        'path': file_path,
        'description': description
    }

def generate_timeline():
    """Generate the timeline markdown content."""
    wiki_files = get_wiki_files()
    posts = [parse_wiki_file(f) for f in wiki_files]
    posts.sort(key=lambda x: x['date'], reverse=True)
    
    # Group posts by year and month
    posts_by_year = defaultdict(lambda: defaultdict(list))
    for post in posts:
        year = post['date'].year
        month = post['date'].strftime('%B')
        posts_by_year[year][month].append(post)
    
    # Generate markdown
    timeline_content = """# Wiki Timeline

<div class="timeline">
"""
    
    for year in sorted(posts_by_year.keys(), reverse=True):
        timeline_content += f"\n## {year}\n"
        
        for month in sorted(posts_by_year[year].keys(), 
                          key=lambda m: datetime.strptime(m, '%B'), 
                          reverse=True):
            timeline_content += f"\n### {month}\n\n"
            
            for post in posts_by_year[year][month]:
                date_str = post['date'].strftime('%b %d, %Y')
                timeline_content += f"- [{post['title']}]({post['path']}) - *{date_str}*\n"
                if post['description']:
                    timeline_content += f"  > {post['description']}\n\n"
    
    timeline_content += """</div>

<style>
.timeline {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

.timeline h2 {
    color: var(--md-primary-fg-color);
    border-bottom: 2px solid var(--md-primary-fg-color);
    padding-bottom: 0.5rem;
    margin-top: 2rem;
}

.timeline h3 {
    color: var(--md-accent-fg-color);
    margin-top: 1.5rem;
    margin-left: 1rem;
}

.timeline ul {
    list-style: none;
    padding-left: 2rem;
}

.timeline li {
    position: relative;
    margin-bottom: 1.5rem;
    padding-left: 1.5rem;
}

.timeline li:before {
    content: "";
    position: absolute;
    left: -0.5rem;
    top: 0.5rem;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: var(--md-primary-fg-color);
}

.timeline li a {
    font-size: 1.1rem;
    font-weight: 500;
    text-decoration: none;
}

.timeline li em {
    display: block;
    font-size: 0.9rem;
    color: var(--md-default-fg-color--light);
    margin: 0.2rem 0;
}

.timeline li blockquote {
    margin: 0.5rem 0;
    padding: 0.5rem 1rem;
    border-left: 4px solid var(--md-accent-fg-color);
    background: var(--md-code-bg-color);
}

.timeline li blockquote p {
    margin: 0;
}
</style>
"""
    
    return timeline_content

def main():
    """Main function to update the timeline file."""
    timeline_content = generate_timeline()
    with open(TIMELINE_FILE, 'w', encoding='utf-8') as f:
        f.write(timeline_content)

if __name__ == '__main__':
    main() 