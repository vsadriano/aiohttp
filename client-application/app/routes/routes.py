from aiohttp import web
from app.modules.author.author_controller import AuthorController


class Routes():
    def __init__(self):
        self.author_ctl = AuthorController()

    def setup_routes(self, app):
        app.add_routes([
            web.get("/api/v1/authors", self.author_ctl.get_authors),
            web.post("/api/v1/authors", self.author_ctl.save_author),
            web.put("/api/v1/authors", self.author_ctl.update_author),
            web.delete("/api/v1/authors", self.author_ctl.remove_author),
        ])
