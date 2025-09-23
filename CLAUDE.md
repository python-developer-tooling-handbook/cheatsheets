# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static site generator for Python cheatsheets. It converts Markdown files in the `sheets/` directory to styled HTML pages using Jinja2 templates and Python's markdown library.

## Development Commands

### Build System
- `make build` - Generate static HTML files from markdown (uses `uv run --with jinja2 --with markdown generate.py`)
- `make serve` - Build and serve locally on port 8000
- `make clean` - Remove generated files in `dist/`
- `make help` - Show available targets

### Dependencies
The project uses `uv` for dependency management and doesn't have a traditional requirements.txt. Dependencies are managed inline via `uv run --with` commands:
- `jinja2` - Template engine
- `markdown` - Markdown processing with tables and fenced_code extensions

## Architecture

### Core Components
- `generate.py` - Main static site generator script
- `template.html` - Jinja2 HTML template with embedded CSS styling
- `sheets/*.md` - Markdown cheatsheet source files
- `dist/` - Generated HTML output directory
- `netlify.toml` - Deployment configuration

### Site Generation Process
1. Reads all `.md` files from `sheets/` directory
2. Extracts H1 titles from markdown content
3. Processes content (removes `<article>` tags if present)
4. Converts markdown to HTML using extensions for tables and fenced code
5. Renders content through `template.html` with title and content variables
6. Generates individual HTML files in `dist/`
7. Creates `index.html` with links to all cheatsheets

### Styling
The template includes comprehensive CSS with:
- Lime green (#84cc16) color scheme for headings and accents
- Responsive design with mobile breakpoints
- Table styling with hover effects
- Code block and inline code formatting
- Clean typography using system fonts

## Adding New Cheatsheets

1. Create a new `.md` file in the `sheets/` directory
2. Start with an H1 title (`# Title`) - this becomes the page title
3. Use tables, code blocks, and standard markdown formatting
4. Run `make build` to generate the HTML
5. The new cheatsheet will automatically appear in the index

## Deployment

The site is configured for Netlify deployment with special handling to make the uv cheatsheet the default index page (`mv dist/uv.html dist/index.html`).