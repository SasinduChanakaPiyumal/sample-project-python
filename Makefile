.PHONY: install build test benchmark format lint clean run setup-hooks help

# Default target - display help when running 'make' without arguments
.DEFAULT_GOAL := help

# ============================================================================
# HELP TARGET
# ============================================================================

# Display all available commands with descriptions
help:
	@echo "Available make commands:"
	@echo ""
	@echo "  make install       Install project dependencies using Poetry"
	@echo "  make build         Alias for 'make install'"
	@echo "  make test          Run tests without benchmarks"
	@echo "  make benchmark     Run benchmarks only"
	@echo "  make format        Format code with black and isort"
	@echo "  make lint          Check code style (black and isort) without modifying"
	@echo "  make clean         Remove cache, build artifacts, and temporary files"
	@echo "  make run           Execute the main application"
	@echo "  make setup-hooks   Install pre-commit hooks for code quality"
	@echo "  make help          Display this help message"
	@echo ""

# ============================================================================
# INSTALL / BUILD TARGETS
# ============================================================================

# Install dependencies using Poetry
install:
	poetry install

# Alias for install
build: install

# ============================================================================
# TEST TARGETS
# ============================================================================

# Run tests without running benchmarks
test:
	poetry run pytest --benchmark-skip tests/

# Run benchmarks only
benchmark:
	poetry run pytest --benchmark-only tests/

# ============================================================================
# CODE QUALITY TARGETS
# ============================================================================

# Format code using black and isort
format:
	black src/ tests/
	isort src/ tests/

# Check code style using black and isort (without modifying files)
lint:
	black --check --diff src/ tests/
	isort --check-only --diff src/ tests/

# ============================================================================
# CLEAN TARGET
# ============================================================================

# Remove Python cache files, pytest cache, coverage files, and build artifacts
clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name .coverage -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name dist -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name build -exec rm -rf {} + 2>/dev/null || true
	@echo "Cleaned up cache, build artifacts, and temporary files"

# ============================================================================
# GIT HOOKS TARGET
# ============================================================================

# Install pre-commit hooks for code quality checks
setup-hooks:
	poetry run pre-commit install

# ============================================================================
# RUN TARGET
# ============================================================================

# Execute the main application
run:
	poetry run main
