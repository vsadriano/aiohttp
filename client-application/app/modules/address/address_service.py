from app.utils.utils import Utils
from app.config import config
import aiohttp


class AddressService():
    def __init__(self):
        self.utils = Utils()

    async def request_my_ip(self):
        my_ip = await self.utils.req_get_handler(config.endpoint_ip)
        return my_ip
