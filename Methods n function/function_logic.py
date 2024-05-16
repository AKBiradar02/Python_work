
# Functions with logic

#mod operator "%" It shows the remainder 

x = 2 % 2 
print(x)

y = 3 % 2
print(y)


def even_check(number):
    result = number % 2==0
    return result

print(even_check(15))
print('\n')



#RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST

def check_even_list(num_list):

    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
print(check_even_list[1,3,5])



 