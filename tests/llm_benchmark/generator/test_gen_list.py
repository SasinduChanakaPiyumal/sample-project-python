import pytest
from llm_benchmark.generator.gen_list import GenList

def test_random_matrix_dimensions():
    n_rows = 3
    m_cols = 5
    matrix = GenList.random_matrix(n_rows, m_cols)
    
    assert len(matrix) == n_rows
    for row in matrix:
        assert len(row) == m_cols

def test_random_list_length():
    n = 10
    m = 100
    lst = GenList.random_list(n, m)
    assert len(lst) == n
    for x in lst:
        assert 0 <= x <= m
