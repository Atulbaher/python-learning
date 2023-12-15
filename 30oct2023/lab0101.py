api_response = {
    "first_name": "Atul",
    "last_name": "Baher",
    "age": 34,
    "email": "atulbaher@gmail.com",
    "password": "atul12345",
    "commissions": 10,
    "roles": [4]
}

print(api_response)
print(type(api_response))
print(api_response.get('passeord'))
print(api_response.get('role'))
print(api_response['roles'])

api_response['age'] = 34
print(api_response)


a = {
    "bookingid": 2345,
    "booking": {
        "firstname": "atul",
        "lastname": "baher",
        "totalprice": 432,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2023-11-12",
            "checkout": "2023-11-12"
        },
        "additionalneeds": "lunch"
    }
}

print(a["booking"]["bookingdates"]["checkin"])
print(a["booking"]["bookingdates"]["checkout"])
