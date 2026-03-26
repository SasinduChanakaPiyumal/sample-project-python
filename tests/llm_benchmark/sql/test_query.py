import pytest

from llm_benchmark.sql.query import SqlQuery


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Presence", True),
        ("Roundabout", False),
    ],
)
def test_query_album(name: str, expected: bool) -> None:
    """Test query_album() returns True for existing albums and False for non-existent ones."""
    assert SqlQuery.query_album(name) == expected


def test_benchmark_query_album(benchmark) -> None:
    """Benchmark the query_album() method for performance regression detection."""
    benchmark(SqlQuery.query_album, "Presence")


def test_join_albums() -> None:
    """Test join_albums() correctly joins Album, Artist, and Track tables."""
    assert SqlQuery.join_albums()[0] == (
        "For Those About To Rock (We Salute You)",
        "For Those About To Rock We Salute You",
        "AC/DC",
    )


def test_benchmark_join_albums(benchmark) -> None:
    """Benchmark the join_albums() method for performance regression detection."""
    benchmark(SqlQuery.join_albums)


def test_top_invoices() -> None:
    """Test top_invoices() returns the top 10 invoices sorted by total in descending order."""
    top = SqlQuery.top_invoices()
    assert top[0][2] == 25.86
    assert top[2][2] == 21.86
    assert len(top) == 10


def test_benchmark_top_invoices(benchmark) -> None:
    """Benchmark the top_invoices() method for performance regression detection."""
    benchmark(SqlQuery.top_invoices)
