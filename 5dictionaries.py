#dictionaries
dist = {'key1':'value1', 'key2':'value2'}
print(dist)
dist['key1']
print(dist['key1'])

prices = {'apple':120, 'orange':150, 'banana':60}
prices['apple']
prices['banana']
prices['orange']
print(prices['apple'])
print(prices['banana'])
print(prices['orange'])

#using multiple terms 
d = {'k1':124, 'k2':[1,2,3],'k3':{'val':139}}
d['k1']
d['k2']
d['k3']
print(d['k1'])
print(d['k2'])
print(d['k3'])
print(d['k3']['val'])
print(d['k2'][2])


a = {'key5':['a','b','c']}
print(a)
x = a['key5']
print(x)
letter = x[2]
print(letter)
letter.upper()
print(letter.upper())
a['key5'][2].upper()
print(a['key5'][2].upper())


j = {'s1':100, 's2':200}
j['s3'] = 300

j['s1']= 300
print(j)

j.keys()
print(j.keys())
j.items()
print(j.items())
