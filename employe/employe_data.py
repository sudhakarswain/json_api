from flask import Flask, request, json
from flask_restful import Resource, request

from database import database

import pandas as pd
# import json
class GetEmployee(Resource): #class define CAMEL IT MEANS 1ST LETTER CAPITAL AND MILLDE ONE CAPITAL
    def post(self):
        try:
            conn=database.connection()
            req_data = request.get_json()
            print(req_data)
            query = "select * from json_data"
            df = pd.read_sql(query,conn)
            print(df)
            print(conn)                             #curd operations
            js = df.to_json(orient='records')
            print(js.__class__)

            #return json.loads(js)
            return {'res_status': True,
                                'status_code': 200,
                                        'employess': json.loads(js)}

        except Exception as error:
            print("an error occour",{error})




# Python program to convert JSON to Python


import json

# JSON string
employee ='{"id":"09", "name": "Nitin", "department":"Finance"}'

# Convert string to Python dict
employee_dict = json.loads(employee)
print(employee_dict)


