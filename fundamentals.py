num = 5
string = 'im a string'
boolean = False

print(num)
print(string)
print(boolean)
print(num, string, boolean)


if(num > 10):
    print('that is larger than 10')
else:
    print('that is not larger than 10')



if(num < 0 and boolean == True): 
    print('negative and true')
elif(num > 0 and boolean == False):
    print('posative false')
elif(num > 100 or boolean == True):
    print('larger or true')
else:
    ('i dont know')
