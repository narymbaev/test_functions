

class TasksView(BaseAPI):
    async def get(self, request, user):
        success, response = await FunnelsRepository.instance().list_funnel(
            user_id=user['id'],
            is_template=request.args.get('is_template'),
            page=request.args.get('page'),
            limit=request.args.get('limit'),
            sort_by=request.args.get('sort_by')
        )

        if not success:
            return self.error(response)

        return self.success(**response)