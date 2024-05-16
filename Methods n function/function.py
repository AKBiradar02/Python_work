# def keyword

#defination of function
#Syntax
#def name_of_function():

def say_hello():
    print("hello")
    print("How Are")
    print("You?")

print(say_hello())

print('\n')

def say_helllo(name = 'default'):
    print(f'Hello {name}')

print(say_helllo('Abhay'))

print('\n')


def add_num(num1,num2):
    return num1+num2       

result = add_num(10,40)
print(result)

print('\n')

def print_result(a,b):
    print(a+b)
print(print_result(10,20))

def print_result(a,b):
    return a+b

print(print_result(10,30))