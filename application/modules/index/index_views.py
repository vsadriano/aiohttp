from aiohttp import web

class IndexViews():
    def __init__(self):
        pass

    async def index_handler(self, request):
        return web.FileResponse('./app/templates/index.html')
