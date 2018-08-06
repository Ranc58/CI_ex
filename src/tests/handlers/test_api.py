import tornado.escape
import http.client as httplib

from tests.conftest import BaseTestCase
from tests import factories
from models.models import user


class BaseAPITestCase(BaseTestCase):
    base_url = '/api/v1/{}'
    response_fields = []
    resource = None

    def _build_url(self, endpoint):
        return self.base_url.format(endpoint)

    def make_request(self, endpoint, *args, body=None, headers=None, method='GET'):
        url = self.base_url.format(endpoint)
        if args:
            url = '{url}/{url_args}'.format(
                url=url,
                url_args='/'.join(str(arg) for arg in args if arg)
            )
        if body:
            body = tornado.escape.json_encode(body)
        response = self.fetch(url, method=method, body=body, headers=headers)
        try:
            response.json = tornado.escape.json_decode(response.body)
        except Exception:
            response.json = {}
        return response

    def assertResponseFields(self, response, resource):
        items = response.json[resource]
        if not isinstance(items, list):
            items = [items]

        for item in items:
            self.assertIsNot(item, None)
            for field in self.response_fields:
                self.assertIn(field, item)


class TestUsers(BaseAPITestCase):
    response_fields = ['user_id', 'first_name', 'last_name', 'phone_number']
    resource = 'users'

    def test_create_user(self):
        user = factories.UserFactory.build()
        data = dict(
            first_name=user['first_name'],
            last_name=user['last_name'],
            phone_number=user['phone_number']
        )
        response = self.make_request(self.resource, body=data, method='POST')
        self.assertEqual(response.code, httplib.CREATED)
        self.assertResponseFields(response, 'user')

    def test_get_users(self):
        for _ in range(2):
            factories.UserFactory.create()
        response = self.make_request(self.resource)
        self.assertEqual(response.code, httplib.OK)
        self.assertEqual(len(response.json['users']), 2)
        self.assertResponseFields(response, 'users')


class TestUser(BaseAPITestCase):
    response_fields = TestUsers.response_fields
    resource = 'users/{}'

    def test_get_user(self):
        user = factories.UserFactory.create()
        endpoint = self.resource.format(user['user_id'])
        response = self.make_request(endpoint)
        self.assertResponseFields(response, 'user')

    def test_update_user_phone(self):
        user_for_update = factories.UserFactory.create()
        user_info = factories.UserFactory.build()
        endpoint = self.resource.format(user_for_update['user_id'])
        data = dict(
            phone_number=user_info['phone_number']
        )
        response = self.make_request(endpoint, method='PUT', body=data)
        self.assertEqual(response.code, httplib.CREATED)
        self.assertResponseFields(response, 'user')
        self.assertEqual(response.json['user']['phone_number'], user_info['phone_number'])

    def test_delete_user(self):
        user_for_delete = factories.UserFactory.create()
        endpoint = self.resource.format(user_for_delete['user_id'])
        response = self.make_request(endpoint, method='DELETE')
        self.assertEqual(response.code, httplib.NO_CONTENT)


class Test404Handler(BaseAPITestCase):
    resource = 'error_endpoint'

    def test_get_error(self):
        response = self.make_request(self.resource)
        self.assertEqual(response.code, httplib.NOT_FOUND)
