import requests
import json 

input_dict1 = {
                "age": 22,
                "workclass": "Private",
                "fnlgt": 201490,
                "education": "HS-grad",
                "education_num": 9,
                "marital_status": "Never-married",
                "occupation": "Adm-clerical",
                "relationship": "Own-child",
                "race": "White",
                "sex": "Male",
                "capital_gain": 0,
                "capital_loss": 0,
                "hours_per_week": 20,
                "native_country": "United-States"
                }

input_dict2 = {
                "age": 52,
                "workclass": "Self-emp-inc",
                "fnlgt": 287927,
                "education": "HS-grad",
                "education_num": 9,
                "marital_status": "HS-grad",
                "occupation": "Exec-managerial",
                "relationship": "Wife",
                "race": "White",
                "sex": "Female",
                "capital_gain": 15024,
                "capital_loss": 0,
                "hours_per_week": 40,
                "native_country": "United-States"
                }

response = requests.post('https://udacityc3.herokuapp.com/predict/', data=json.dumps(input_dict1))
print(response.status_code)
print(response.json())

response = requests.post('https://udacityc3.herokuapp.com/predict/', data=json.dumps(input_dict2))
print(response.status_code)
print(response.json())