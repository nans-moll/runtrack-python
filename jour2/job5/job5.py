for i in range (0,101):
    if i % 3 == 0 and i % 5 == 0:
        print("afficher fizzbuzz")
    elif i % 3 == 0: 
        print("afficher fizz")
    elif i % 5 == 0:
        print(" afficher buzz")
    else:
        print(i)