import logging
import sqlite3
from textwrap import dedent

logger = logging.getLogger(__name__)


class SqlQuery:
    @staticmethod
    def query_album(name: str) -> bool:
        """Check if an album exists

        Args:
            name (str): Name of the album

        Returns:
            bool: True if the album exists, False otherwise
        """
        try:
            with sqlite3.connect("data/chinook.db") as conn:
                cur = conn.cursor()

                cur.execute(
                    "SELECT 1 FROM Album WHERE Title = ? LIMIT 1",
                    (name,),
                )
                return cur.fetchone() is not None
        except (sqlite3.DatabaseError, FileNotFoundError) as e:
            logger.error(f"Error querying album: {e}")
            return False

    @staticmethod
    def join_albums() -> list:
        """Join the Album, Artist, and Track tables

        Returns:
            list:
        """
        try:
            with sqlite3.connect("data/chinook.db") as conn:
                cur = conn.cursor()

                cur.execute(
                    dedent(
                        """\
                        SELECT 
                            t.Name AS TrackName,
                            a.Title AS AlbumName,
                            ar.Name AS ArtistName
                        FROM 
                            Track t
                        JOIN Album a ON a.AlbumId = t.AlbumId
                        JOIN Artist ar ON ar.ArtistId = a.ArtistId
                        """
                    )
                )
                return cur.fetchall()
        except (sqlite3.DatabaseError, FileNotFoundError) as e:
            logger.error(f"Error joining albums: {e}")
            return []

    @staticmethod
    def top_invoices() -> list:
        """Get the top 10 invoices by total

        Returns:
            list: List of tuples
        """
        try:
            with sqlite3.connect("data/chinook.db") as conn:
                cur = conn.cursor()

                cur.execute(
                    dedent(
                        """\
                        SELECT 
                            i.InvoiceId, 
                            c.FirstName || ' ' || c.LastName AS CustomerName, 
                            i.Total
                        FROM 
                            Invoice i
                        JOIN Customer c ON c.CustomerId = i.CustomerId
                        ORDER BY i.Total DESC
                        LIMIT 10
                        """
                    )
                )
                return cur.fetchall()
        except (sqlite3.DatabaseError, FileNotFoundError) as e:
            logger.error(f"Error getting top invoices: {e}")
            return []
