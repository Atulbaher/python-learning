import requests


def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/1421")
    print(response_body.status_code)
    print(response_body.json())
    print(response_body.text)


response_body = requests.get("https://restful-booker.herokuapp.com/booking/1421")
if response_body.status_code == 200:
    print("TC#1 - GET request is successfully")

else:
    print("TC#1 - GET request is Not successfully")

if __name__ == "__main__":
    main()
