import logging
import json
from aiohttp import web
from application.config import config
from application.config.const import *
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
        req_params = request.rel_url.query

        try:
            if "id" in req_params:
                id_ = req_params["id"]
                author = await self.author_svc.get_author(dbpool, id_)
                if not author:
                    self.utils.handler_bad_request(
                        f"Não foi encontrado registro com o ID {id_}")
                return web.json_response({"author": self._build_json_author(author), "success": True})

            authors = await self.author_svc.get_authors(dbpool)
            return web.json_response({"authors": self._build_json_authors(authors), "success": True})
        except web.HTTPBadRequest as err:
            logging.error("Falha ao consultar o registro informado.")
            logging.error(err)
            return web.json_response(text=err.text, content_type="application/json", status=400)
        except Exception as err:
            logging.error("Falha ao obter a lista de autores.")
            logging.error(type(err))
            self.utils.handler_internal_error()

    async def save_author(self, request):
        dbpool = request.app['dbpool']
        req_data = await request.json()
        author_data = self.utils.validate_author_data(req_data)

        try:
            await self.author_svc.insert_author(dbpool, author_data)
            res = self.utils.handler_registry_suceeded()
            return res
        except web.HTTPBadRequest as err:
            logging.error("Falha na inserção do registro.")
            logging.error(err)
        except Exception as err:
            logging.error("Falha na inserção do registro.")
            logging.error(err)
            self.utils.handler_internal_error()

    async def update_author(self, request):
        dbpool = request.app['dbpool']
        req_data = await request.json()
        author = self.utils.validate_author(req_data)

        try:
            author_data = await self.author_svc.get_author(dbpool, author.id)
            if not author_data:
                self.utils.handler_bad_request(
                    f"Não foi encontrado registro com o ID {author.id}")
            await self.author_svc.update_author(dbpool, author)
            res = self.utils.handler_update_succeeded()
            return res
        except web.HTTPBadRequest as err:
            logging.error("Falha na atualização do registro.")
            logging.error(err)
            return web.json_response(text=err.text, content_type="application/json", status=400)
        except Exception as err:
            logging.error("Falha na atualização do registro.")
            logging.error(err)
            self.utils.handler_internal_error()

    async def remove_author(self, request):
        dbpool = request.app['dbpool']
        req_params = request.rel_url.query

        try:
            if "id" in req_params:
                id_ = req_params["id"]
                author_data = await self.author_svc.get_author(dbpool, req_params["id"])
                if not author_data:
                    self.utils.handler_bad_request(
                        f"Não foi encontrado registro com o ID {id_}")
                await self.author_svc.delete_author(dbpool, id_)
                res = self.utils.handler_remove_succeeded()
                return res
            self.utils.handler_bad_request("Formato da requisição inválido.")
        except web.HTTPBadRequest as err:
            logging.error("Falha na remoção do registro.")
            logging.error(err)
            return web.json_response(text=err.text, content_type="application/json", status=400)
        except Exception as err:
            logging.error("Falha na remoção do registro.")
            logging.error(err)
            self.utils.handler_internal_error()

    def _build_json_authors(self, authors):
        return [{"id": a.id, "first_name": a.first_name, "last_name": a.last_name, "email": a.email} for a in authors]

    def _build_json_author(self, author):
        return {"id": author.id, "first_name": author.first_name, "last_name": author.last_name, "email": author.email}
