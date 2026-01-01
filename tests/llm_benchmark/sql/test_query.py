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
    assert SqlQuery.query_album(name) == expected


def test_query_album_sql_injection_or_condition() -> None:
    """Test that SQL injection with OR condition is prevented.
    
    Before the fix, query_album("' OR '1'='1") would return True
    because it would execute: SELECT * FROM Album WHERE Title = '' OR '1'='1'
    which returns all records.
    
    After the fix, it treats the input as a literal string and looks for
    an album with that exact title, which doesn't exist.
    """
    # This should return False because no album has this literal title
    result = SqlQuery.query_album("' OR '1'='1")
    assert result is False, "SQL injection with OR condition should not work"


def test_query_album_sql_injection_comment() -> None:
    """Test that SQL injection with comment is prevented.
    
    Before the fix, query_album("'; --") would potentially cause issues
    by commenting out the rest of the query.
    
    After the fix, it treats the input as a literal string.
    """
    # This should return False because no album has this literal title
    result = SqlQuery.query_album("'; --")
    assert result is False, "SQL injection with comment should not work"


def test_query_album_sql_injection_union() -> None:
    """Test that SQL injection with UNION is prevented.
    
    Before the fix, query_album("' UNION SELECT 1,2,3 --") could
    potentially return unexpected data.
    
    After the fix, it treats the input as a literal string.
    """
    # This should return False because no album has this literal title
    result = SqlQuery.query_album("' UNION SELECT 1,2,3 --")
    assert result is False, "SQL injection with UNION should not work"


def test_query_album_legitimate_special_characters() -> None:
    """Test that legitimate album names with special characters work correctly.
    
    This ensures that while SQL injection is prevented, normal queries
    with special characters in album names still work as expected.
    """
    # These albums should not exist, but we're testing the parameter handling
    result = SqlQuery.query_album("Album's Title")
    assert result is False, "Album with apostrophe should be handled safely"
    
    result = SqlQuery.query_album('Album "Title"')
    assert result is False, "Album with quotes should be handled safely"


def test_benchmark_query_album(benchmark) -> None:
    benchmark(SqlQuery.query_album, "Presence")


def test_join_albums() -> None:
    assert SqlQuery.join_albums()[0] == (
        "For Those About To Rock (We Salute You)",
        "For Those About To Rock We Salute You",
        "AC/DC",
    )


def test_benchmark_join_albums(benchmark) -> None:
    benchmark(SqlQuery.join_albums)


def test_top_invoices() -> None:
    top = SqlQuery.top_invoices()
    assert top[0][2] == 25.86
    assert top[2][2] == 21.86
    assert len(top) == 10


def test_benchmark_top_invoices(benchmark) -> None:
    benchmark(SqlQuery.top_invoices)
