from application.config import config
from application.models.author import Author


class AuthorService():
    def __init__(self):
        pass

    async def get_authors(self, dbpool):
        sql = f"""SELECT author_fname,
            author_lname,
            author_email,
            author_id
            FROM author"""
            
        async with dbpool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(sql)
                rows = await cursor.fetchall()
                return [Author(*row) for row in rows] if rows else None

    async def insert_author(self, dbpool, author):
        sql = f"""INSERT INTO author
            (
                author_fname,
                author_lname,
                author_email
            ) VALUES
            (
                '{author.first_name}',
                '{author.last_name}',
                '{author.email}'
            )"""
            
        async with dbpool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(sql)
