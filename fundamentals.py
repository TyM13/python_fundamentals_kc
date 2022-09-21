# num = -5
# string = 'im a string'
# boolean = False

# print(num)
# print(string)
# print(boolean)
# print(num, string, boolean)


# if(num > 10):
#     print('that is larger than 10')
# else:
#     print('that is not larger than 10')



# if(num < 0 and boolean == True): 
#     print('negative and true')
# elif(num > 0 and boolean == False):
#     print('posative false')
# elif(num > 100 or boolean == True):
#     print('larger or true')
# else:
#     print("i don't know")


# array_of_strings = ['one','two','three']
# array_of_numbers = [1,2,3]

# for string in array_of_strings:
#     print(string)

# for num in array_of_numbers:
#     print('look at this number', num)



# def static_greeting():
#     print('hello my name is tyler')


# static_greeting()


# def dynamic_greeting(arg1):
#     print('hello', arg1)

# dynamic_greeting('user')
# dynamic_greeting('best user')
# dynamic_greeting('best')




def find_treasure(string):
    for string in array_strings:    
        if(string == 'treasure'):
            print('found treasure')
            return True
    print('no treasure')
    return False
           

array_strings = ['treasures','treasures','three'] 
find_treasure(array_strings)