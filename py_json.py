# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

#sample json
userJSON = '{"first_name": "Efe", "last_name": "Elmas", "age": 30}'

#parse to dict
user_mee =json.loads(userJSON)

print(user_mee)
print(user_mee['first_name'])

car_mee={'make':'Ford','model':'Mustang','year': 1970}

carJSON=json.dumps(car_mee)

print(carJSON)