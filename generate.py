#!/usr/bin/env python3
"""
Static site generator for Python cheatsheets.
Converts Markdown files in sheets/ to HTML using Jinja2 templates.
"""

import os
import sys
from pathlib import Path
import markdown
from jinja2 import Environment, FileSystemLoader

def extract_title_from_markdown(content):
    """Extract the first H1 title from markdown content."""
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('# '):
            return line[2:].strip()
    return "Python Cheatsheet"

def process_markdown_content(content):
    """Process markdown content, removing <article> tags if present."""
    # Remove opening and closing article tags
    content = content.replace('<article>', '').replace('</article>', '')
    return content.strip()

def generate_site():
    """Generate static HTML files from Markdown sheets."""
    # Setup paths
    sheets_dir = Path('sheets')
    output_dir = Path('dist')
    template_file = Path('template.html')

    # Create output directory
    output_dir.mkdir(exist_ok=True)

    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    # Process each markdown file
    markdown_files = list(sheets_dir.glob('*.md'))

    if not markdown_files:
        print("No markdown files found in sheets/ directory")
        return

    for md_file in markdown_files:
        print(f"Processing {md_file}")

        # Read markdown content
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Process content and extract title
        processed_content = process_markdown_content(content)
        title = extract_title_from_markdown(processed_content)

        # Convert markdown to HTML
        md = markdown.Markdown(extensions=['tables', 'fenced_code'])
        html_content = md.convert(processed_content)

        # Render template
        html = template.render(
            title=title,
            content=html_content
        )

        # Write output file
        output_file = output_dir / f"{md_file.stem}.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"Generated {output_file}")

    # Generate index page
    generate_index(markdown_files, output_dir, template)

def generate_index(markdown_files, output_dir, template):
    """Generate an index page listing all cheatsheets."""
    index_content = "<h1>Python Cheatsheets</h1>\n<ul>\n"

    for md_file in sorted(markdown_files):
        # Read file to get title
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        processed_content = process_markdown_content(content)
        title = extract_title_from_markdown(processed_content)

        html_filename = f"{md_file.stem}.html"
        index_content += f'  <li><a href="{html_filename}">{title}</a></li>\n'

    index_content += "</ul>"

    # Render index template
    html = template.render(
        title="Python Cheatsheets",
        content=index_content
    )

    # Write index file
    index_file = output_dir / "index.html"
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Generated {index_file}")

if __name__ == "__main__":
    generate_site()