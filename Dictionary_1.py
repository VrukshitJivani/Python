#Dictionary is used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

mix={
    "name":"Vijay",
    "age":30,
    "city":"Bhavnagar",
    "country":"India",
    "phone":1234567890,
    "marks":[60,50,78,73,56,'red'],
    "isPassed":True,
    "color":("red","green","blue",12)
}

print(mix)
print(type(mix))
print(mix['name'])
print(mix['age'])

mix['pincode']=364120
print(mix)

mix['age']=31
print(mix)

del mix['phone']
print(mix)

print(mix['marks'][0])
print(mix['color'][2])

del mix['marks'][5]
print(mix)