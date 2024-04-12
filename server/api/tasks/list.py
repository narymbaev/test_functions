from utils.request import BaseAPI


class TasksView(BaseAPI):
    async def get(self, request, user):
        return self.success()