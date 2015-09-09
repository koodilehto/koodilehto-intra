from peewee import Model, \
    CharField, DateTimeField, ForeignKeyField, TextField
from flask.ext.security import UserMixin, RoleMixin
from . import db


# the user model specifies its fields (or columns) declaratively, like django
class User(db.Model):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()

    class Meta:
        order_by = ('username',)


# this model contains two foreign keys to user -- it essentially allows us to
# model a "many-to-many" relationship between users.  by querying and joining
# on different columns we can expose who a user is "related to" and who is
# "related to" a given user
class Relationship(db.Model):
    from_user = ForeignKeyField(User, related_name='relationships')
    to_user = ForeignKeyField(User, related_name='related_to')

    class Meta:
        indexes = (
            # Specify a unique multi-column index on from/to-user.
            (('from_user', 'to_user'), True),
        )


# a dead simple one-to-many relationship: one user has 0..n messages, exposed
# by the foreign key.  because we didn't specify, a users messages will be
# accessible as a special attribute, User.message_set
class Message(db.Model):
    user = ForeignKeyField(User)
    content = TextField()
    pub_date = DateTimeField()

    class Meta:
        order_by = ('-pub_date',)
