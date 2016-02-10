from marshmallow import Schema, fields

# SCHEMAS
# =======

class UserSchema(Schema):
    id = fields.UUID(dump_only=True)
    firstname = fields.Str(required=True)
    lastname = fields.Str(required=True)
    created_timestamp = fields.DateTime()


users_schema = UserSchema(many=True)
user_schema = UserSchema()
