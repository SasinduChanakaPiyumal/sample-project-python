"""Main entry point for LLM benchmark demonstrations."""

import logging
import os

from llm_benchmark.algorithms.primes import Primes
from llm_benchmark.algorithms.sort import Sort
from llm_benchmark.control.double import DoubleForLoop
from llm_benchmark.control.single import SingleForLoop
from llm_benchmark.datastructures.dslist import DsList
from llm_benchmark.generator.gen_list import GenList
from llm_benchmark.sql.query import SqlQuery
from llm_benchmark.strings.strops import StrOps

# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

LOGS_DIR = "logs"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
LOG_DATEFORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging():
    """Configure logging with file and console handlers."""
    # Create logs directory if it doesn't exist
    os.makedirs(LOGS_DIR, exist_ok=True)

    # Initialize root logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Remove any existing handlers to avoid duplicate logs
    logger.handlers.clear()

    # Configure FileHandler
    file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "main.log"))
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(LOG_FORMAT, datefmt=LOG_DATEFORMAT)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # Configure StreamHandler (console output)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter(LOG_FORMAT, datefmt=LOG_DATEFORMAT)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Log initialization message
    logger.info("Logging infrastructure initialized")


def demo_single_for_loop():
    """Demonstrate SingleForLoop operations."""
    print("SingleForLoop")
    print("-------------")
    print(f"sum_range(10): {SingleForLoop.sum_range(10)}")
    print(f"max_list([1, 2, 3]): {SingleForLoop.max_list([1, 2, 3])}")
    print(f"sum_modulus(100, 3): {SingleForLoop.sum_modulus(100, 3)}")
    print()


def demo_double_for_loop():
    """Demonstrate DoubleForLoop operations."""
    print("DoubleForLoop")
    print("-------------")
    print(f"sum_square(10): {DoubleForLoop.sum_square(10)}")
    print(f"sum_triangle(10): {DoubleForLoop.sum_triangle(10)}")
    
    random_list = GenList.random_list(30, 10)
    print(f"count_pairs(random_list(30, 10)): {DoubleForLoop.count_pairs(random_list)}")
    
    list1 = GenList.random_list(10, 2)
    list2 = GenList.random_list(10, 2)
    duplicates = DoubleForLoop.count_duplicates(list1, list2)
    print(f"count_duplicates(10, 10): {duplicates}")
    
    random_matrix = GenList.random_matrix(10, 10)
    print(f"sum_matrix(random_matrix(10, 10)): {DoubleForLoop.sum_matrix(random_matrix)}")
    print()


def demo_sql():
    """Demonstrate SQL query operations."""
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

def demo_primes():
    """Demonstrate prime number operations."""
    print("Primes")
    print("------")
    print(f"is_prime(1700): {Primes.is_prime_ineff(1700)}")
    print(f"sum_primes(210): {Primes.sum_primes(210)}")
    print(f"prime_factors(840): {Primes.prime_factors(840)}")
    print()

def demo_sort():
    """Demonstrate sorting operations."""
    print("Sort")
    print("----")

    test_list = [5, 3, 2, 1, 4]
    print(f"sort_list({test_list}): ", end="")
    Sort.sort_list(test_list)
    print(test_list)

    test_list = [5, 3, 2, 1, 4]
    print(f"dutch_flag_partition({test_list}, 3): ", end="")
    Sort.dutch_flag_partition(test_list, 3)
    print(test_list)

    test_list = [5, 3, 2, 1, 4]
    print(f"max_n({test_list}, 3): {Sort.max_n(test_list, 3)}")
    print()


def demo_dslist():
    """Demonstrate data structure list operations."""
    print("DsList")
    print("------")

    test_list = [1, 2, 3, 4, 5]
    print(f"Original list: {test_list}")
    print(f"Modified list: {DsList.modify_list(test_list)}")
    print(f"Search result for 3: {DsList.search_list(test_list, 3)}")
    print(f"Sorted list: {DsList.sort_list(test_list)}")
    print(f"Reversed list: {DsList.reverse_list(test_list)}")
    print(f"Rotated list by 2 positions: {DsList.rotate_list(test_list, 2)}")
    print(f"Merged list with [6, 7, 8]: {DsList.merge_lists(test_list, [6, 7, 8])}")
    print()

def demo_strops():
    """Demonstrate string operations."""
    print("StrOps")
    print("------")

    test_str = "racecar"
    print(f"Original string: {test_str}")
    print(f"Reversed string: {StrOps.str_reverse(test_str)}")
    print(f"Is palindrome: {StrOps.palindrome(test_str)}")
    print()


def main():
    """Run all benchmark demonstrations."""
    setup_logging()
    
    demo_single_for_loop()
    demo_double_for_loop()
    demo_sql()
    demo_primes()
    demo_sort()
    demo_dslist()
    demo_strops()


if __name__ == "__main__":
    main()