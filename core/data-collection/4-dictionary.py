"""
Dict = mutable, unindexed, duplicate keys are not allowed

syntax:

dict_name = {}
dict_name = dict()

dict_name = {"key1": value1, "key2": value2,..., "keyN": valueN}
"""

contacts = {
    'A':[
        {
            'ajay':{
                'phone': '9876543210',
                'email': 'ajay@example.com'
            },
            'atul':{
                'phone': '9988776655',
                'email': ['atul@example.com', 'atul.5234@gmail.com']
            }
        }
    ],
    'B':[
        {
            'balu':{
                'phone': '7788990011',
                'email': 'balu@example.com'
            },
            'bhanu':{
                'phone': '7788990012',
                'email': 'bhanu@example.com'
            }
        }
    ],
    'C':[
        {
            'chandan':{
                'phone': '8899001122',
                'email': 'chandan@example.com'
            }
        }
    ]
}

# print(contacts)

# print(contacts['B'])
# print(contacts['B'][0]['bhanu']['phone'])

# car = {
#     'brand': 'Toyota',
#     'model': 'Corolla',
#     'year': 2020,
#     'color': 'Blue'
# }

# car_type = {
#     'SUV': ['Toyota', 'Honda', 'Ford'],
#     'Sedan': ['BMW', 'Mercedes', 'Volkswagen']
# }
# car.update(car_type)
# print(car)

# car.setdefault("color", "black")

# print(car)


# print(dir(car))

# print(car.get('model'))

# print(car.keys())
# print(car.values())

# [(key1, value1), (key2, value2)]
# print(car.items())

# car.pop('model')
# car.popitem()

# print(car)


# setdefault
# update

# items = ['a', 'b', 'c']
# price = 50
# products = dict()

# print(products.fromkeys(items, price))

