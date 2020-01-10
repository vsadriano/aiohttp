# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import aiopg
import asyncio
import logging
from application.config import config

db_name = config.db_name
db_user = config.db_user
db_password = config.db_password
db_host = config.db_host
db_port = config.db_port

dsn = f"dbname={db_name} user={db_user} password={db_password} host={db_host} port={db_port}"


class BaseDao:

    def __init__(self):
        logging.basicConfig(format='''%(asctime)s %(levelname)s: %(message)s''',
                            datefmt='%d/%m/%Y %H:%M:%S', level=logging.INFO)

    async def pool_create(self, app):
        try: 
            pool = await aiopg.create_pool(dsn, minsize=10, maxsize=10)
            app['dbpool'] = pool
        except Exception as err:
            logging.error("Falha ao criar o pool de conexões com o banco de dados!")
            logging.error(f"Erro: {err}")
            raise(err)

    async def pool_clear(self, app):
        try:
            await app['dbpool'].clear()
        except Exception as err:
            logging.error("Falha ao encerrar o pool de conexões com o banco de dados!")
            logging.error(f"Erro: {err}")
            raise(err)
