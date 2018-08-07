import factory

from models import models
from models.database import CiexEngine, get_connection_url
from sqlalchemy import create_engine

LOCALE = "ru_RU"


class BaseFactory(factory.Factory):
    
    class Meta:
        abstract = True

    @classmethod
    def _build(cls, model_class, *args, **kwargs):
        return kwargs

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        engine = create_engine(get_connection_url())
        res = engine.execute(model_class.insert().values(**kwargs).returning(*model_class.c))
        return res.fetchone()


class UserFactory(BaseFactory):

    class Meta:
        model = models.user

    first_name = factory.Faker('first_name', locale=LOCALE)
    last_name = factory.Faker('last_name', locale=LOCALE)
    phone_number = factory.Faker('phone_number', locale=LOCALE)
