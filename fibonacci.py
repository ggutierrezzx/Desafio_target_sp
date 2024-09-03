def numero_fibonacci(num):

    a = 0
    b = 1


    while b < num:
        temp = b  
        b = a + b  
        a = temp 

    if num == b or num == 0:  
        print(f"O numero {num} pertence a sequencia de Fibonacci.") 
    else:
        print(f"O numero {num} nao pertence a sequencia de Fibonacci.")


numero = 30
numero_fibonacci(numero)