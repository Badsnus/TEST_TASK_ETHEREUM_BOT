import databases
import orm

from data.config import DATABASE_URL

database = databases.Database(DATABASE_URL)
models = orm.ModelRegistry(database=database)


class Users(orm.Model):
    tablename = "users"
    registry = models
    fields = {
        'id': orm.Integer(primary_key=True),
        "user_id": orm.BigInteger()
    }


class Seeds(orm.Model):
    tablename = "seeds"
    registry = models
    fields = {
        "id": orm.Integer(primary_key=True),
        "user_id": orm.BigInteger(),
        "seed": orm.Text()
    }
