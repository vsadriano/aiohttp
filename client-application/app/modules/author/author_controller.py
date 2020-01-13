import logging
import json
from aiohttp import web
from app.config import config
from app.config.const import *
from app.modules.author.author_service import AuthorService
from app.utils.utils import Utils


class AuthorController():
    def __init__(self):
        self.author_svc = AuthorService()
        self.utils = Utils()
        logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                            level=logging.INFO)

    async def get_authors(self, request):
        req_params = request.rel_url.query

        try:
            if "id" in req_params:
                id_ = req_params["id"]
                author = await self.author_svc.get_authors({"id": id_})
                if not author:
                    self.utils.handler_bad_request(
                        f"Não foi encontrado registro com o ID {id_}")
                return web.json_response(author)

            authors = await self.author_svc.get_authors()
            return web.json_response(authors)
        except web.HTTPBadRequest as err:
            logging.error("Falha ao consultar o registro informado.")
            logging.error(err)
            return web.json_response(text=err.text, content_type="application/json", status=400)
        except Exception as err:
            logging.error("Falha ao obter a lista de autores.")
            logging.error(type(err))
            self.utils.handler_internal_error()

    async def save_author(self, request):
        req_data = await request.json()
        author_data = self.utils.validate_author_data(req_data)

        try:
            res = await self.author_svc.insert_author(author_data)
            return web.json_response(res)
        except web.HTTPBadRequest as err:
            logging.error("Falha na inserção do registro.")
            logging.error(err)
        except Exception as err:
            logging.error("Falha na inserção do registro.")
            logging.error(err)
            self.utils.handler_internal_error()

    async def update_author(self, request):
        req_data = await request.json()
        author = self.utils.validate_author(req_data)

        try:
            author_data = await self.author_svc.get_authors({"id": author.id})
            if not author_data:
                self.utils.handler_bad_request(
                    f"Não foi encontrado registro com o ID {author.id}")
            await self.author_svc.update_author(author)
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
        req_params = request.rel_url.query

        try:
            if "id" in req_params:
                id_ = req_params["id"]
                author_data = await self.author_svc.get_authors({"id": id_})
                if not author_data:
                    self.utils.handler_bad_request(
                        f"Não foi encontrado registro com o ID {id_}")
                await self.author_svc.delete_author({"id": id_})
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
