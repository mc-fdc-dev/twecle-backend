from rt_lib.common import database


DatabaseManager = database.DatabaseManager
cursor = database.cursor

__all__ = (
    "DatabaseManager",
    "cursor"
)
