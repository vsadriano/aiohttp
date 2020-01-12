from aiohttp import web
from app.dao.base_dao import BaseDao
from app.routes.routes import Routes
import logging


class Server():
    def __init__(self):
        logging.basicConfig(format='''%(asctime)s %(levelname)s: %(message)s''',
            datefmt='%d/%m/%Y %H:%M:%S', level=logging.INFO)
        self.routes = Routes()

    def run(self):
        try:
            logging.info("Inicializando o servidor web...")
            app = web.Application()
            app.on_startup.append(BaseDao().pool_create)
            app.on_cleanup.append(BaseDao().pool_clear)
            self.routes.setup_routes(app)
            web.run_app(app)
        except Exception as err:
            logging.error("Falha ao inicializar o servidor!")
            logging.error(f"Erro: {err}")
            raise(err)


