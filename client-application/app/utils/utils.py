from aiohttp import web
from app.config import config
from app.config.const import *
from app.models.author import Author
import aiohttp
import json


class Utils():
    def __init__(self):
        pass

    def handler_bad_request(self, msg):
        bad_request_msg = {"success": False,
                           "status": "400: Bad Request",
                           "message": f"{msg}"
                           }
        raise web.HTTPBadRequest(text=json.dumps(
            bad_request_msg), content_type="application/json")

    def handler_internal_error(self):
        raise web.HTTPInternalServerError(text=json.dumps(
            INTERNAL_ERROR_MSG), content_type="application/json")

    def handler_not_acceptable(self):
        raise web.HTTPNotAcceptable(text=json.dumps(
            NOT_ACCEPTABLE_MSG), content_type="application/json")

    def handler_registry_suceeded(self):
        return web.json_response(text=json.dumps(
            REGISTRY_SUCCEEDED_MSG), content_type="application/json")

    def handler_update_succeeded(self):
        return web.json_response(text=json.dumps(
            UPDATE_SUCCEEDED_MSG), content_type="application/json")

    def handler_remove_succeeded(self):
        return web.json_response(text=json.dumps(
            NO_CONTENT_MSG), content_type="application/json")

    async def req_get_handler(self, endpoint, params=None):
        async with aiohttp.ClientSession() as session:
            # async with session.get(f"{config.url}{endpoint}", params=params) as resp:
            #     res = await resp.json()
                # if not res["success"]:
                #     return None
                # return res
            async with session.Request('GET', f"{config.url}{endpoint}", params=params) as resp:
                res = await resp.json()
                if not res["success"]:
                    return None
                return res

    async def req_post_handler(self, endpoint, data=None):
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{config.url}{endpoint}", json=data) as resp:
                res = await resp.json()
                return res
    
    async def req_put_handler(self, endpoint, data=None):
        async with aiohttp.ClientSession() as session:
            async with session.put(f"{config.url}{endpoint}", json=data) as resp:
                res = await resp.json()
                if not res["success"]:
                    return None
                return res

    async def req_delete_handler(self, endpoint, params):
        async with aiohttp.ClientSession() as session:
            async with session.delete(f"{config.url}{endpoint}", params=params) as resp:
                res = await resp.json()
                if not res["success"]:
                    return None
                return res

    def validate_author(self, data):
        if "id" in data:
            return Author(data["first_name"],
                          data["last_name"],
                          data["email"],
                          data["id"])
        raise self.handler_bad_request("JSON inválido")

    def validate_author_data(self, data):
        if "first_name" in data:
            if "last_name" in data:
                if "email" in data:
                    return Author(data["first_name"],
                                  data["last_name"],
                                  data["email"])

        raise self.handler_bad_request("JSON inválido")
