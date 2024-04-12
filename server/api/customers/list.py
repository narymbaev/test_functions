from utils.request import BaseAPI


class CustomersView(BaseAPI):
    async def get(self, request, user):
        return self.success()

    async def post(self, request, user):
        return self.success()