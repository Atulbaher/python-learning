# 1. Python Testing Framework -> 1. Unit Test, Nose, Pytest ( TestNG)
# 2. Every Test will start from test_name.py
# 3. pytest -h
# 4. pytest -k  - Match substring - pytest -k "name"  -> test_name.py
# 5. pytest -v logs
# How to do Create Booking by using the pyTest -> allure

# Create a Booking - POST -
# URL
# Headers
# BODY ( Payload) - Json
# Token ? / Auth
# Verify the Booking ID, Booking Information( as JSON)

import pytest
import requests


@pytest.mark.positive
def test_create_booking_positive():
    print("Create Booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    # Assertions
    assert response.status_code == 200
    # Get the response body and verify the json,bookingid ID is not None
    data = response.json()
    booking_id = data["bookingid"]
    print(booking_id)
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"] == "Jim", "Failed Message - Incorrect First Name"

    @pytest.mark.negetive
    def test_create_booking_negetive():
        print("Create Booking Testcase")
        URL = "https://restful-booker.herokuapp.com/booking"
        headers = {"Content-Type": "application/json"}
        json_payload = {

        }
        response = requests.post(url=URL, headers=headers, json=json_payload)
        print(type(URL))
        print(type(headers))
        print(type(json_payload))

        #Assersions
        assert response.status_code == 500

