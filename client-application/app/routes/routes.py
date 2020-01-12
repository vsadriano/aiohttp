from aiohttp import web
from app.modules.address.address_controller import AddressController


class Routes():
    def __init__(self):
        self.address_ctl = AddressController()

    def setup_routes(self, app):
        app.add_routes([
            web.get("/api/v1/ip", self.address_ctl.get_ip),
        ])
