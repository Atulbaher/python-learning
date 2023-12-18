import requests

response_body = requests.get("https://restful-booker.herokuapp.com/booking/1421")
print(response_body.text)
print(response_body.headers)


# verify ?

# Assertion - > Verify the expected result with the actual result

# status code ER -> 200
# AR ->  200

# if id == 1420

#ER = 404

#AR = 404
