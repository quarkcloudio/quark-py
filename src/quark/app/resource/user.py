from quark.template.resource import Resource

class User(Resource):
    def index(self):
        return "Hello World"

    def create(self):
        return "Hello World"

    def show(self, id):
        return "Hello World"

    def update(self, id):
        return "Hello World"

    def delete(self, id):
        return "Hello World"