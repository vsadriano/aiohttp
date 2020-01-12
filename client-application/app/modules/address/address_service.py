from app.utils.utils import Utils
import aiohttp
# endpoint http://ip.jsontest.com


class AddressService():
    def __init__(self):
        self.utils = Utils()

    async def request_my_ip(self):
        my_ip = await self.utils.req_get_handler()
        return my_ip
