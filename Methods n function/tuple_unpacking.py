# tuple unpacking with python function 

stock_prices = [('APPL',200),('GOOG',400),('MSFT',100)]

for item in stock_prices:
    print(item)

print('\n')

for company,price in stock_prices:
    print(company,price+(0.1*price))
    
print('\n')

work_hours = [('Abhay',100),('Shradha',80),('Kapil',300)]

def employee_check(work_hours):


    current_max = 0    # Reset the value of employee 
    employee_of_month = ''   # reset the value of string 

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    #return
    return(employee_of_month,current_max)

result = employee_check(work_hours)
name,hours = employee_check(work_hours)
print(name)
print(result)

