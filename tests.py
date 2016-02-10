import unittest
from flask.ext.testing import TestCase
from app import app, db, models

class APITests(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"    # use memory db.
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_main_route_must_return_200(self):
        response = self.client.get("/")
        self.assertEquals(200, response.status_code)

    def test_is_empty_user_list(self):
        response = self.client.get("/users")
        self.assertEquals(response.json, {"data": []})

    def test_can_create_a_new_user(self):
        name = "test"
        lastname = "test123"
        data = '{"firstname":"%s", "lastname": "%s"}' %(name, lastname)

        response = self.client.get("/users")
        self.assertEquals(response.json["data"], [], "There is no users")

        response = self.client.post("/users", data=data, content_type='application/json')
        self.assertEquals(200, response.status_code)

        id_created = response.json['data']['id']

        # and works with a single record route
        response = self.client.get("/users/{0}".format(id_created))
        self.assertEquals(response.json['data']['id'], str(id_created))
        self.assertEquals(response.json['data']['firstname'], name)
        self.assertEquals(response.json['data']['lastname'], lastname)

    def test_can_change_a_user(self):
        name = "name"
        lastname = "lastname"
        data = '{"firstname":"%s", "lastname": "%s"}' %(name, lastname)

        response = self.client.post("/users", data=data, content_type='application/json')
        self.assertEquals(200, response.status_code)

        record_id = response.json['data']['id']

        name = "name 123"
        lastname = "lastname 123"
        new_data = '{"firstname":"%s", "lastname": "%s"}' %(name, lastname)

        result = self.client.put("/users/{0}".format(record_id), data=new_data, content_type='application/json')

        response = self.client.get("/users")
        self.assertEquals(len(response.json['data']), 1)
        self.assertEquals(response.json['data'][0]['firstname'], name)
        self.assertEquals(response.json['data'][0]['lastname'], lastname)

    def test_can_delete_command(self):
        name = "name"
        lastname = "lastname"
        data = '{"firstname":"%s", "lastname": "%s"}' %(name, lastname)
        response = self.client.post("/users", data=data, content_type='application/json')

        response = self.client.get("/users")
        self.assertEquals(len(response.json['data']), 1)
        record_id = response.json['data'][0]['id']

        self.client.delete("/users/{0}".format(record_id))

        response = self.client.get("/users")
        self.assertEquals(len(response.json['data']), 0)

    def test_must_return_400_when_incorrect_uuid(self):
        response = self.client.get("/users/{0}".format("TEST-invalid-UDDDD"))
        self.assertEquals(400, response.status_code)


if __name__ == '__main__':
    unittest.main()
