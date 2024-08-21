info = {
    'Name':'swagatika',
    'Age':23,
    'subject':['python','core java','c'],
    'Topics':('dict','set'),
    'is adult':True,
    'cgpa':8.37
}
print(info)
print(type(info))


#callig the key and getting its corresponding value//
data = info['Name']
print(data)

var = info['Age']
print(var)

#to change the value in any of the keys//
info['Name'] = 'Abhilash'
print(info)