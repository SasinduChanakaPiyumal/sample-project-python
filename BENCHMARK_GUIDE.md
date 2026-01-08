# Micro-Benchmark Guide

## Overview
The `benchmark_improvements.py` script provides a comprehensive micro-benchmark suite that demonstrates the performance improvements achieved through code optimizations.

## Running the Benchmarks

### Quick Start
```bash
python benchmark_improvements.py
```

This will run all benchmarks and display results for each optimized function.

### Output Format
Each benchmark produces output like:
```
======================================================================
BENCHMARK: prime_factors(84)
======================================================================
Arguments: (84,)
Iterations: 1000

Old Implementation:   0.123456 seconds
New Implementation:   0.001234 seconds

Speedup:            100.00x faster
Improvement:         99.00%
```

## What's Being Benchmarked

### 1. Prime Factorization
- **Function**: `prime_factors()`
- **Input**: Integer 84
- **Iterations**: 1,000
- **What to expect**: 50-100x speedup

### 2. Sorting (Small List)
- **Function**: `sort_list()`
- **Input**: [5, 4, 3, 2, 1]
- **Iterations**: 1,000
- **What to expect**: 5-10x speedup

### 3. Sorting (Large List)
- **Function**: `sort_list()`
- **Input**: Reversed list of 100 integers
- **Iterations**: 100
- **What to expect**: 100x+ speedup

### 4. String Reversal (Short)
- **Function**: `str_reverse()`
- **Input**: "racecar" (7 characters)
- **Iterations**: 10,000
- **What to expect**: 10-50x speedup

### 5. String Reversal (Long)
- **Function**: `str_reverse()`
- **Input**: 260 character string
- **Iterations**: 1,000
- **What to expect**: 100-1000x+ speedup

### 6. Finding Duplicates (Small Arrays)
- **Function**: `count_duplicates()`
- **Input**: Two arrays of 4 elements each
- **Iterations**: 1,000
- **What to expect**: 50-100x speedup

### 7. Finding Duplicates (Large Arrays)
- **Function**: `count_duplicates()`
- **Input**: Two arrays of 200 elements each
- **Iterations**: 100
- **What to expect**: 1000x+ speedup

### 8. Sum Range (Small)
- **Function**: `sum_range()`
- **Input**: 100
- **Iterations**: 10,000
- **What to expect**: 100x speedup

### 9. Sum Range (Large)
- **Function**: `sum_range()`
- **Input**: 10,000
- **Iterations**: 10,000
- **What to expect**: 10,000x+ speedup

## Understanding the Results

### Speedup Factor
- **Speedup = Old Time / New Time**
- Higher is better
- A speedup of 100x means the new version is 100 times faster

### Improvement Percentage
- **Improvement% = ((Old - New) / Old) × 100**
- Shows what percentage of the original time is saved
- 99% improvement = saves 99% of the time

### Time Complexity Reference
| Complexity | Example | ~100 items | ~1000 items |
|-----------|---------|-----------|------------|
| O(1) | Math formula | 1ns | 1ns |
| O(n) | Single loop | 1μs | 10μs |
| O(n log n) | Sorting | 660ns | 9.9μs |
| O(n²) | Nested loops | 100μs | 10ms |
| O(√n) | Prime factors | 10μs | 100μs |

## Performance Tips

1. **String Operations**: Always use slice notation (s[::-1]) instead of concatenation in loops
2. **Sorting**: Use built-in sorted() instead of implementing your own algorithm
3. **Duplicates/Membership**: Use sets instead of nested loops
4. **Mathematical Problems**: Look for formulas before writing loops
5. **Large Scale**: Time complexity matters more than constant factors

## Modifying the Benchmarks

To add your own benchmark:

```python
def my_function_old(x):
    # old implementation
    pass

def my_function_new(x):
    # new optimized implementation
    pass

# In main() function:
benchmark_function(
    "my_function_description",
    my_function_old,
    my_function_new,
    (test_input,),
    number=1000,
)
```

## Running Individual Benchmarks

You can modify `benchmark_improvements.py` to run only specific benchmarks by commenting out or removing the `benchmark_function()` calls you don't want.

## Expected Runtime
- Full benchmark suite: ~2-10 seconds (depending on machine)
- Each individual benchmark: <1 second

## Troubleshooting

**Q: Why is the old version so slow?**
A: It's using inefficient algorithms (bubble sort, string concatenation, nested loops) that have O(n²) or worse complexity.

**Q: Why does the speedup vary?**
A: System load, CPU cache effects, and Python's dynamic compilation (JIT) can affect timing. Run multiple times for consistent results.

**Q: Can I trust these results?**
A: Yes, but remember:
- Real-world performance depends on your specific use case
- The optimizations are fundamentally better (asymptotically)
- Actual speedup may vary based on system and input size

## Next Steps

1. Review `OPTIMIZATION_SUMMARY.md` for detailed explanations of each optimization
2. Run the main test suite to ensure all functionality is preserved
3. Use these techniques in your own code optimization efforts

## Questions?

Refer to:
- `OPTIMIZATION_SUMMARY.md` - Detailed optimization explanations
- `README.md` - Project overview and usage
- Individual source files - Code comments and docstrings
