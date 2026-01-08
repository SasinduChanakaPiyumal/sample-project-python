"""
Micro-benchmark script to compare old vs new implementations.
Demonstrates performance improvements in optimized functions.
"""

import timeit
from typing import Callable, List, Tuple


# ============================================================================
# OLD IMPLEMENTATIONS (INEFFICIENT)
# ============================================================================

def prime_factors_old(n: int) -> List[int]:
    """Original inefficient prime factorization."""
    ret = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                ret.append(i)
                n = n // i
                break
    return ret


def sort_list_old(v: List[int]) -> List[int]:
    """Original bubble sort implementation."""
    ret = v.copy()
    for i in range(len(ret)):
        for j in range(i + 1, len(ret)):
            if ret[i] > ret[j]:
                ret[i], ret[j] = ret[j], ret[i]
    return ret


def str_reverse_old(s: str) -> str:
    """Original inefficient string reversal."""
    ret = ""
    for i in range(len(s)):
        ret += s[len(s) - 1 - i]
    return ret


def count_duplicates_old(arr0: List[int], arr1: List[int]) -> int:
    """Original O(n²) nested loop."""
    count = 0
    for i in range(len(arr0)):
        for j in range(len(arr1)):
            if i == j and arr0[i] == arr1[j]:
                count += 1
    return count


def sum_range_old(n: int) -> int:
    """Original implementation using array creation."""
    arr = []
    for i in range(n):
        arr.append(i)
    return sum(arr)


# ============================================================================
# NEW IMPLEMENTATIONS (OPTIMIZED)
# ============================================================================

def prime_factors_new(n: int) -> List[int]:
    """Optimized prime factorization - O(sqrt(n)) time."""
    ret = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            ret.append(d)
            n //= d
        d += 1
    if n > 1:
        ret.append(n)
    return ret


def sort_list_new(v: List[int]) -> List[int]:
    """Optimized using built-in sorted() - O(n log n) time."""
    return sorted(v)


def str_reverse_new(s: str) -> str:
    """Optimized using slice - O(n) time with optimal constant factor."""
    return s[::-1]


def count_duplicates_new(arr0: List[int], arr1: List[int]) -> int:
    """Optimized using set intersection - O(n) time."""
    set0 = set(arr0)
    set1 = set(arr1)
    return len(set0 & set1)


def sum_range_new(n: int) -> int:
    """Optimized using mathematical formula - O(1) time."""
    return n * (n - 1) // 2


# ============================================================================
# BENCHMARK FUNCTION
# ============================================================================

def benchmark_function(
    name: str,
    func_old: Callable,
    func_new: Callable,
    args: Tuple,
    number: int = 100,
) -> None:
    """Run a micro-benchmark comparing old vs new implementations."""
    
    # Time old implementation
    time_old = timeit.timeit(
        lambda: func_old(*args),
        number=number,
    )
    
    # Time new implementation
    time_new = timeit.timeit(
        lambda: func_new(*args),
        number=number,
    )
    
    # Calculate speedup
    speedup = time_old / time_new if time_new > 0 else float('inf')
    improvement_pct = ((time_old - time_new) / time_old) * 100
    
    # Print results
    print(f"\n{'=' * 70}")
    print(f"BENCHMARK: {name}")
    print(f"{'=' * 70}")
    print(f"Arguments: {args}")
    print(f"Iterations: {number}")
    print(f"\nOld Implementation:  {time_old:12.6f} seconds")
    print(f"New Implementation: {time_new:12.6f} seconds")
    print(f"\nSpeedup:            {speedup:12.2f}x faster")
    print(f"Improvement:        {improvement_pct:12.2f}%")
    

# ============================================================================
# MAIN BENCHMARK SUITE
# ============================================================================

def main():
    """Run all benchmarks."""
    print("\n" + "=" * 70)
    print("PERFORMANCE OPTIMIZATION MICRO-BENCHMARKS")
    print("=" * 70)
    
    # Benchmark 1: prime_factors
    benchmark_function(
        "prime_factors(84)",
        prime_factors_old,
        prime_factors_new,
        (84,),
        number=1000,
    )
    
    # Benchmark 2: sort_list with small list
    benchmark_function(
        "sort_list([5, 4, 3, 2, 1])",
        sort_list_old,
        sort_list_new,
        ([5, 4, 3, 2, 1],),
        number=1000,
    )
    
    # Benchmark 3: sort_list with larger list
    large_list = list(range(100, 0, -1))
    benchmark_function(
        "sort_list(large_list) - 100 elements",
        sort_list_old,
        sort_list_new,
        (large_list,),
        number=100,
    )
    
    # Benchmark 4: str_reverse with short string
    benchmark_function(
        "str_reverse('racecar')",
        str_reverse_old,
        str_reverse_new,
        ("racecar",),
        number=10000,
    )
    
    # Benchmark 5: str_reverse with longer string
    long_str = "abcdefghijklmnopqrstuvwxyz" * 10  # 260 chars
    benchmark_function(
        "str_reverse(long_string) - 260 chars",
        str_reverse_old,
        str_reverse_new,
        (long_str,),
        number=1000,
    )
    
    # Benchmark 6: count_duplicates
    benchmark_function(
        "count_duplicates([1,1,2,2], [1,1,2,2])",
        count_duplicates_old,
        count_duplicates_new,
        ([1, 1, 2, 2], [1, 1, 2, 2]),
        number=1000,
    )
    
    # Benchmark 7: count_duplicates with larger arrays
    large_arr = list(range(100)) * 2
    benchmark_function(
        "count_duplicates(large_arrays) - 200 elements each",
        count_duplicates_old,
        count_duplicates_new,
        (large_arr, large_arr),
        number=100,
    )
    
    # Benchmark 8: sum_range
    benchmark_function(
        "sum_range(100)",
        sum_range_old,
        sum_range_new,
        (100,),
        number=10000,
    )
    
    # Benchmark 9: sum_range with larger number
    benchmark_function(
        "sum_range(10000)",
        sum_range_old,
        sum_range_new,
        (10000,),
        number=10000,
    )
    
    print(f"\n{'=' * 70}")
    print("BENCHMARK SUMMARY")
    print("=" * 70)
    print("""
The optimizations demonstrate significant performance improvements:

1. prime_factors(): Changed from O(n²) nested loops to O(√n) iteration
   → Dramatically faster for large numbers
   
2. sort_list(): Changed from bubble sort O(n²) to Timsort O(n log n)
   → Massive improvement, especially with larger lists
   
3. str_reverse(): Changed from string concatenation to slice notation
   → Eliminates O(n²) concatenation overhead
   
4. count_duplicates(): Changed from O(n²) nested loops to O(n) set ops
   → Linear time complexity with low constant factor
   
5. sum_range(): Changed from O(n) array building to O(1) formula
   → Instantaneous for any input size

These optimizations improve memory usage, CPU efficiency, and reduce
algorithmic complexity across the board.
""")


if __name__ == "__main__":
    main()
