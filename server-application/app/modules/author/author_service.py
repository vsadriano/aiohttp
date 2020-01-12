from app.config import config
from app.models.author import Author


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

    async def get_author(self, dbpool, author_id):
        sql = f"""SELECT author_fname,
            author_lname,
            author_email,
            author_id
            FROM author
            WHERE author_id = %s"""

        async with dbpool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(sql, (author_id,))
                row = await cursor.fetchone()
                return Author(*row) if row else None

    async def insert_author(self, dbpool, author):
        sql = f"""INSERT INTO author
            (
                author_fname,
                author_lname,
                author_email
            ) VALUES
            (
                %s, %s, %s
            )"""

        async with dbpool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(sql, (author.first_name,
                                           author.last_name,
                                           author.email))

    async def update_author(self, dbpool, author):
        sql = f"""UPDATE author
            SET author_fname = %s,
                author_lname = %s,
                author_email = %s
            WHERE author_id = {author.id}
            """
        print(f"Author: {author.last_name}")

        async with dbpool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(sql,
                                     (author.first_name,
                                      author.last_name,
                                      author.email))

    async def delete_author(self, dbpool, author_id):
        sql = f"""DELETE FROM author
            WHERE author_id = {author_id}"""

        async with dbpool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(sql)
