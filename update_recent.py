import os
import glob
import datetime

INDEX_FILE = os.path.join('docs', 'index.md')
INDEX_HEADER = \
"""
# Index

[Hu](https://zhuhu00.top/)'s notebook.

## Recent Updates
"""

_exclude_list = [INDEX_FILE,]

files = glob.glob('docs/**/*.md', recursive=True)
files = [f for f in files if f not in _exclude_list]
files = sorted(files, key=lambda t: -os.stat(t).st_mtime) # descending modification time

# write recent updated files to index.md
# files = files[:20]
with open(INDEX_FILE, 'w') as handle:
    handle.write(INDEX_HEADER)
    for file in files:
        name = os.path.basename(file)
        modified = os.path.getmtime(file)
        edit_time = datetime.datetime.fromtimestamp(modified).strftime('%Y-%m-%d %H:%M')
        
        handle.write(f'- [{name}]({os.path.relpath(file, "docs").replace(".md", "/")}) <span style="float: right;">{edit_time}</span>\n')