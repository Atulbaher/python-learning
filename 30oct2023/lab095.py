phone_book = {"batman": 9876543210,"superman": 1234567890, "wonder": 9893224601}

#dict ? it is very close to the JSON
print(phone_book)
print(len(phone_book))

# you can access alement by key only - Dict

phone_book2 = dict(batman=123,cersei=323, gb= 322)
print(phone_book2)
print(phone_book2['gb'])
print(phone_book2["gb"])
print(phone_book2.get('gb'))
print(phone_book2.get("gb"))

Atul_details = dict(name = "Atul", age =34, ismale = True, adress = "madhyapradesh")
Atul_details2 = {"name":"Atul", "age": 34,"ismale": True,"address":"madhyapradesh"}
print(Atul_details)
print(Atul_details['age'])
print(Atul_details.get('age'))

print(Atul_details2['age'])
print(Atul_details2.get("age"))
