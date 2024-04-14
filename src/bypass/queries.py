"""
DB queries.
"""

from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.sql import select

from .db import metadata


async def fetch_requests(conn: AsyncConnection):
    requests = metadata.tables['requests']
    records = await conn.execute(select(requests))
    return records


async def fetch_request(conn: AsyncConnection, id: int):
    requests = metadata.tables['users']

    stmt = select(requests).where(requests.c.request_id == id)
    records = await conn.execute(stmt)
    return records
