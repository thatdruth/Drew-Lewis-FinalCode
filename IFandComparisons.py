

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: #Can also compare strings with == "SOmething" also != is not equals
        return num1 
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(46, 89, 9))
