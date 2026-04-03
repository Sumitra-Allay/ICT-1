userDetails = {'Id,' : 1, 'userName':'Just_me'}
print(type(userDetails))
print(userDetails)

location = dict(s = 'Samtse', t = 'Thimphu', p = 'Paro')
print(location)

print(userDetails['userName']) #Just_me
print(location.get('t')) #Thimphu  = is also known as assignment operator

userDetails['email'] = 'justme@example.com'
print(userDetails)
userDetails['userName'] = 'Just_me_updated'
print(userDetails) 

del location ['p']
print(location)

deleted_value = userDetails.pop('email')
print(deleted_value)

del_key, del_value = userDetails.popitem()
print(f'the deleted key is {del_key}and the deleted value is {del_value}')
location.clear() #Clearing all key-value pairs from the ditionary
print(location) #{}:output 