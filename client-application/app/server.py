from aiohttp import web
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
            self.routes.setup_routes(app)
            web.run_app(app)
        except Exception as err:
            logging.error("Falha ao inicializar o servidor!")
            logging.error(f"Erro: {err}")
            raise(err)
