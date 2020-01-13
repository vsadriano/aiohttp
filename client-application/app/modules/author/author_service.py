from app.config import config
from app.models.author import Author
from app.utils.utils import Utils


class AuthorService():
    def __init__(self):
        self.endpoint = "/authors"
        self.utils = Utils()

    async def get_authors(self, params=None):
        res = await self.utils.req_get_handler(self.endpoint, params)
        return res

    async def insert_author(self, author):
        payload = {"first_name": author.first_name,
            "last_name": author.last_name,
            "email": author.email}

        res = await self.utils.req_post_handler(self.endpoint, payload)
        return res

    async def update_author(self, author):
        payload = {"id": author.id,
            "first_name": author.first_name,
            "last_name": author.last_name,
            "email": author.email}

        res = await self.utils.req_put_handler(self.endpoint, payload)
        return res

    async def delete_author(self, params):
        res = await self.utils.req_delete_handler(self.endpoint, params)
        return res
