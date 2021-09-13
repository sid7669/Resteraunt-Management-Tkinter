def newton_method(number, number_iters = 500):
    a = float(number)
    for i in range(number_iters):
        number = 0.5 * (number + a / number)
    return number
a=int(input("Enter number "))    
print(newton_method(a))