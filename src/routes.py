from handlers import api
from tornado.web import url

url_list = [
    # api
    url(r"/api/v1/users/?", api.UsersHandler, name='users_handler'),
    url(r"/api/v1/users/([0-9a-f\-])/?", api.UserHandler, name='user_handler'),
    url(r"/api/v1/.*", api.Error404, name='error_handler'),
]
