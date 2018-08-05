from aiopg.sa import create_engine
from models.database import get_connection_url
from tornado.testing import gen_test

from tests.conftest import BaseTestCase
from tests import factories
from models import users


class TestUserModel(BaseTestCase):

    def __init__(self, *args, **kwargs):
        self.engine = create_engine(get_connection_url())
        super(BaseTestCase, self).__init__(*args, **kwargs)

    @gen_test
    async def test_create_user(self):
        user_data = factories.UserFactory.build()
        created_user = await users.create_user(user_data)
        self.assertIsNotNone(created_user)

    @gen_test
    async def test_get_user(self):
        user = factories.UserFactory.create()
        user_from_db = await users.get_user_by_id(user['user_id'])
        self.assertIsNotNone(user_from_db)
        self.assertEqual(user, user_from_db)

    @gen_test
    async def test_update_user(self):
        user = factories.UserFactory.create()
        user_data = factories.UserFactory.build()
        updated_user = await users.update_user(
            user_id=user['user_id'],
            data=user_data
        )
        self.assertIsNotNone(updated_user)
        self.assertNotEqual(user, updated_user)
        self.assertTrue(updated_user['update_dttm'])

    @gen_test
    async def test_delete_user(self):
        user = factories.UserFactory.create()
        deleted_user = await users.delete_user(
            user_id=user['user_id']
        )
        self.assertIsNotNone(deleted_user)
        self.assertNotEqual(user, deleted_user)
        self.assertTrue(deleted_user['update_dttm'])
        self.assertTrue(deleted_user['delete_dttm'])
