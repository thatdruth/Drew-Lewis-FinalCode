

print(3**3) #Easy exponent

def raise_to_power(base_num, pow_num):
    result = 1 
    for index in range(pow_num):
        result = result * base_num
    return result 

print(raise_to_power(4,3)) #A coded loop exponent function


