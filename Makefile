.PHONY: all clean serve

# Default target
all: build

# Build static site
build:
	uv run --with jinja2 --with markdown generate.py

# Clean generated files
clean:
	rm -rf dist/

# Serve locally (requires Python's http.server)
serve: build
	cd dist && python -m http.server 8000

# Help
help:
	@echo "Available targets:"
	@echo "  all     - Build site"
	@echo "  build   - Generate static HTML files"
	@echo "  clean   - Remove generated files"
	@echo "  serve   - Build and serve locally on port 8000"
	@echo "  help    - Show this help message"