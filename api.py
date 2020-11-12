from flask import Flask,request
from flask_restful import Resource,Api
from extract import main
from flask import jsonify
app = Flask(__name__)
api = Api(app)

class GetData(Resource):
    def get(self,name):
        return jsonify(main(name))

api.add_resource(GetData,"/<name>")
if __name__ == "__main__":
    app.run(debug=True)

