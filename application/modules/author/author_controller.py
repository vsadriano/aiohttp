import logging
import json
from aiohttp import web
from application.config import config
from application.modules.author.author_service import AuthorService
from application.utils.utils import Utils


class AuthorController():
    def __init__(self):
        self.author_svc = AuthorService()
        self.utils = Utils()
        logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
            level=logging.INFO)

    async def get_authors(self, request):
        dbpool = request.app['dbpool']
        
        try:
            authors = await self.author_svc.get_authors(dbpool)
            return web.json_response({"authors": self._build_json(authors), "success": True})
        except Exception as err:
            logging.error("Falha ao obter a lista de autores.")
            logging.error(err)
            self.utils.handler_internal_error()

    async def save_author(self, request):
        dbpool = request.app['dbpool']
        req_data = await request.json()
        author_data = self.utils.validate_author_data(req_data)

        if not author_data:
            self.utils.handler_bad_request()

        try:
            await self.author_svc.insert_author(dbpool, author_data)
            res = self.utils.handler_registry_suceeded()
            return res
        except Exception as err:
            logging.error("Falha no cadastro do autor.")
            logging.error(err)
            self.utils.handler_internal_error()

    def _build_json(self, authors):
        return [{"id": a.id, "first_name": a.first_name, "last_name": a.last_name, "email": a.email} for a in authors]
