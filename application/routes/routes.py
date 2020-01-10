from aiohttp import web
from application.modules.address.address_controller import AddressController
from application.modules.author.author_controller import AuthorController


class Routes():
    def __init__(self):
        self.address_ctl = AddressController()
        self.author_ctl = AuthorController()

    def setup_routes(self, app):
        app.add_routes([
            web.get("/api/v1/authors", self.author_ctl.get_authors),
            web.post("/api/v1/authors", self.author_ctl.save_author),
            web.get("/api/v1/ip", self.address_ctl.get_ip),
        ])
        