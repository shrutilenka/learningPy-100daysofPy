dict = {
    "name": "sagar",
    "age": 20,
    "gender": "male",
    "address": "pune",
    "phone": 1234567890
}

print(dict["name"])
dict["father"] = 'Suresh'
print(dict)

for i in dict:
    print(f'Key: {i}, Value: {dict[i]}')

# nested dictionary
data = {
    "child": {
        "name": "sagar",
        "age": 20,
        "gender": "male"
    },
    "parent": {
        "name": "sagar",
        "age": 20,
        "gender": "male"
    }
}
print(data["child"]['name'])

# nested list and dict
data2 = {
    "child": ['rahul', 'rohan'],
    "parent": ['suresh', 'madhuri'],
    "hobby": {
        'rahul': 'cricket',
        'rohan': 'football',
        'suresh': 'chess',
        'madhuri': 'reading'
    }
}
print(data2['hobby']['rahul'])
print(data2['child'][0])

travel_log = {
    'France': {
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
        'total_visits': 12
    },
    'Germany': {
        'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
        'total_visits': 5
    }
}
print(travel_log['Germany']['cities_visited'][2])
print(travel_log.items())
