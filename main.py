"""
Benchmark Suite Main Module

This module provides a comprehensive benchmark suite for testing various
LLM-generated algorithms and operations including:
- Control flow operations (single/double loops)
- SQL queries
- Prime number algorithms
- Sorting algorithms
- Data structure operations
- String operations

The suite includes robust error handling to ensure that failures in individual
benchmarks don't crash the entire test suite.
"""

import logging
import sys
from llm_benchmark.algorithms.primes import Primes
from llm_benchmark.algorithms.sort import Sort
from llm_benchmark.control.double import DoubleForLoop
from llm_benchmark.control.single import SingleForLoop
from llm_benchmark.generator.gen_list import GenList
from llm_benchmark.sql.query import SqlQuery
from llm_benchmark.datastructures.dslist import DsList
from llm_benchmark.strings.strops import StrOps


# ============================================================================
# Benchmark Functions
# ============================================================================
# The following functions test different aspects of the LLM benchmark suite.
# Each function is designed to be executed independently with proper error
# handling to ensure failures don't affect other benchmarks.


def single():
    """Test single for loop control flow operations."""
    print("SingleForLoop")
    print("-------------")

    print(f"sum_range(10): {SingleForLoop.sum_range(10)}")
    print(f"max_list([1, 2, 3]): {SingleForLoop.max_list([1, 2, 3])}")
    print(f"sum_modulus(100, 3): {SingleForLoop.sum_modulus(100, 3)}")
    print()


def double():
    """Test double for loop control flow operations."""
    print("DoubleForLoop")
    print("-------------")

    print(f"sum_square(10): {DoubleForLoop.sum_square(10)}")
    print(f"sum_triangle(10): {DoubleForLoop.sum_triangle(10)}")
    print(
        f"count_pairs(random_list(30, 10)): {DoubleForLoop.count_pairs(GenList.random_list(30, 10))}"
    )
    print(
        "count_duplicates(10, 10)",
        DoubleForLoop.count_duplicates(
            GenList.random_list(10, 2), GenList.random_list(10, 2)
        ),
    )
    print(
        f"sum_matrix(random_matrix(10, 10)): {DoubleForLoop.sum_matrix(GenList.random_matrix(10, 10))}"
    )
    print()


def sql():
    """Test SQL query operations against the database."""
    print("SQL")
    print("---")

    print(f"query_album('Presence'): {SqlQuery.query_album('Presence')}")
    print(f"query_album('Roundabout'): {SqlQuery.query_album('Roundabout')}")
    print()

    print("join_albums()")
    print(SqlQuery.join_albums()[0])
    print()

    print("top_invoices()")
    print(SqlQuery.top_invoices())
    print()

def primes():
    """Test prime number algorithms and operations."""
    print("Primes")
    print("------")

    print(f"is_prime(1700): {Primes.is_prime_ineff(1700)}")
    print(f"sum_primes(210): {Primes.sum_primes(210)}")
    print(f"prime_factors(840): {Primes.prime_factors(840)}")
    print()

def sort():
    """Test sorting algorithms and list operations."""
    print("Sort")
    print("----")

    v = [5, 3, 2, 1, 4]
    print(f"sort_list({v}): ", end="")
    Sort.sort_list(v)
    print(v)

    v = [5, 3, 2, 1, 4]
    print(f"dutch_flag_partition({v}, 3): ", end="")
    Sort.dutch_flag_partition(v, 3)
    print(v)

    v = [5, 3, 2, 1, 4]
    print(f"max_n({v}, 3): {Sort.max_n(v, 3)}")
    print()


def dslist():
    """Test data structure list operations."""
    print("DsList")
    print("----")

    test_list = [1, 2, 3, 4, 5]
    print("Original list:", test_list)

    modified_list = DsList.modify_list(test_list)
    print("Modified list:", modified_list)

    search_result = DsList.search_list(test_list, 3)
    print("Search result for 3:", search_result)

    sorted_list = DsList.sort_list(test_list)
    print("Sorted list:", sorted_list)

    reversed_list = DsList.reverse_list(test_list)
    print("Reversed list:", reversed_list)

    rotated_list = DsList.rotate_list(test_list, 2)
    print("Rotated list by 2 positions:", rotated_list)

    merged_list = DsList.merge_lists(test_list, [6, 7, 8])
    print("Merged list with [6, 7, 8]:", merged_list)

def strops():
    """Test string operations including reversal and palindrome detection."""
    print("Strops")
    print("----")

    test_str = "racecar"
    print("Original string:", test_str)

    reversed_str = StrOps.str_reverse(test_str)
    print("Reversed string:", reversed_str)

    is_palindrome = StrOps.palindrome(test_str)
    print("Is palindrome:", is_palindrome)


# ============================================================================
# Error Handling and Execution Utilities
# ============================================================================
# These utility functions provide robust error handling for the benchmark suite,
# ensuring that individual test failures don't crash the entire execution.


def execute_benchmark(func, func_name):
    """
    Execute a benchmark function with exception handling.
    
    Args:
        func: The function to execute
        func_name: Name of the function for logging purposes
    
    Returns:
        bool: True if execution was successful, False otherwise
    """
    try:
        logging.info(f"Starting benchmark: {func_name}")
        func()
        logging.info(f"Successfully completed benchmark: {func_name}")
        return True
    except Exception as e:
        logging.error(f"Error in {func_name}: {type(e).__name__}: {str(e)}")
        logging.debug(f"Exception details for {func_name}", exc_info=True)
        print(f"\n[ERROR] Benchmark '{func_name}' failed: {type(e).__name__}: {str(e)}\n")
        return False


def main():
    """
    Main entry point for the benchmark suite.
    
    Executes all benchmark functions with proper error handling and logging.
    If any benchmark fails, it logs the error and continues with the remaining
    benchmarks. Provides a summary of execution results at the end.
    
    Exit codes:
        0: All benchmarks completed successfully
        1: One or more benchmarks failed
    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('benchmark.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    logging.info("Starting benchmark suite")
    
    # List of benchmarks to execute
    benchmarks = [
        (single, "single"),
        (double, "double"),
        (sql, "sql"),
        (primes, "primes"),
        (sort, "sort"),
        (dslist, "dslist"),
        (strops, "strops")
    ]
    
    # Track execution results
    results = []
    
    # Execute each benchmark with exception handling
    for func, name in benchmarks:
        success = execute_benchmark(func, name)
        results.append((name, success))
    
    # Summary of execution
    logging.info("Benchmark suite completed")
    total = len(results)
    successful = sum(1 for _, success in results if success)
    failed = total - successful
    
    print("\n" + "=" * 50)
    print("BENCHMARK EXECUTION SUMMARY")
    print("=" * 50)
    print(f"Total benchmarks: {total}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    
    if failed > 0:
        print("\nFailed benchmarks:")
        for name, success in results:
            if not success:
                print(f"  - {name}")
    
    print("=" * 50)
    
    # Exit with appropriate status code
    if failed > 0:
        logging.warning(f"Benchmark suite completed with {failed} failure(s)")
        sys.exit(1)
    else:
        logging.info("All benchmarks completed successfully")
        sys.exit(0)


if __name__ == "__main__":
    main()
