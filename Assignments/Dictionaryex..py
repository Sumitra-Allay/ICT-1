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