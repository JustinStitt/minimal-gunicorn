from flask import Flask
from flask_restful import Api, Resource
from utils.even import Even

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"message": "It works!"}


class CheckEven(Resource):
    def get(self, num: int):
        checker = Even(num)
        return {"message": f"{num} is {'even' if checker.check() else 'not even'}"}


api.add_resource(HelloWorld, "/")
api.add_resource(CheckEven, "/even/<int:num>")

if __name__ == "__main__":
    app.run(debug=True)
