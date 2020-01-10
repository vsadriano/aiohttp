from application.modules.address.address_service import AddressService


class AddressController():
    def __init__(self):
        self.address_svc = AddressService()

    async def get_ip(self, _request):
        res = await self.address_svc.request_my_ip()
        return res
