def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("To jest liczba prime")
    else:
        print("To nie jest liczba prime")

prime_checker(4)
