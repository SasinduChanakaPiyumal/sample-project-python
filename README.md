# llm-benchmarking-py

## Quick Start

Get started with the project in just a few commands:

```bash
# Install dependencies
make install

# View all available commands
make help
```

## Development Commands

This project uses a Makefile for simplified command execution. Replace verbose Poetry commands with short, memorable `make` commands:

### Installation & Setup

```bash
make install    # Install project dependencies using Poetry
make build      # Alias for 'make install'
```

### Running the Application

```bash
make run        # Execute the main application
```

### Testing & Benchmarking

```bash
make test       # Run tests without benchmarks
make benchmark  # Run benchmarks only
```

### Code Quality

```bash
make format     # Format code with black and isort
make lint       # Check code style (without modifying files)
make clean      # Remove cache, build artifacts, and temporary files
```

### Pre-commit Hooks

To enable automatic code quality checks on every commit:

```bash
make setup-hooks    # Install pre-commit hooks
```

Once installed, pre-commit will automatically run code quality checks before each commit, preventing formatting issues from being committed.

## Help & All Commands

```bash
make help       # Display all available commands with descriptions
```

---

## Manual Commands (Poetry Reference)

For reference, here are the underlying Poetry commands if you prefer to run them directly:

```bash
# Install dependencies
poetry install

# Run the application
poetry run main

# Run tests without benchmarks
poetry run pytest --benchmark-skip tests/

# Run benchmarks
poetry run pytest --benchmark-only tests/

# Format code
black src/ tests/
isort src/ tests/

# Check code style
black --check --diff src/ tests/
isort --check-only --diff src/ tests/
```

---

## Documentation

For detailed information about the project's performance optimizations and benchmarks, see:
- **BENCHMARK_QUICKSTART.md** - Quick overview of the benchmark results
- **PERFORMANCE_SUMMARY.md** - Detailed performance metrics and analysis
- **BENCHMARK_RESULTS.md** - Comprehensive technical analysis
- **PERFORMANCE_VERIFICATION.md** - Requirements verification and status
- **DOCUMENTATION_INDEX.md** - Complete documentation index and navigation guide
