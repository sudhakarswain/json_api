from datetime import timedelta

from flask import Flask
from flask_cors import CORS
from flask_restful import Api


from employe.employe_data import GetEmployee

app = Flask(__name__)
api = Api(app)
CORS(app)
api.add_resource(GetEmployee,'/employee')  # TODO: generate password user


if __name__=='__main__':
    app.run(debug=True,port=52040)