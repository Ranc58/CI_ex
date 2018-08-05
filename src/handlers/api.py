from tornado.options import options

from handlers.base import BaseAPIHandler
from models import users


class UsersHandler(BaseAPIHandler):

    #TODO add serializer
    async def post(self, *args, **kwargs):
        data = self.build_arguments_from_json()
        user = await users.create_user(data)
        return self.return_created({"user": dict(user)})

    async def get(self, *args, **kwargs):
        try:
            all_users = await users.get_all_users()
        except Exception as e:
            self.json_response({"users": e})
        users_list = [dict(user) for user in all_users]
        return self.json_response({"users": users_list})


class UserHandler(BaseAPIHandler):

    async def put(self, user_id):
        data = self.build_arguments_from_json()
        updated_user = await users.update_user(user_id, data)
        return self.return_created({"user": dict(updated_user)})

    async def get(self, user_id):
        user = await users.get_user_by_id(user_id)
        return self.json_response({'user': dict(user)})

    async def delete(self, user_id):
        user = await users.delete_user(user_id)
        return self.return_no_content()


class Error404(BaseAPIHandler):

    def get(self):
        self.screen()

    def post(self):
        self.screen()

    def patch(self):
        self.screen()

    def put(self):
        self.screen()

    def delete(self):
        self.screen()

    def screen(self):
        self.return_not_found()
