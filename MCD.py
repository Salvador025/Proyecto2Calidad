def mcd(x, y):
    
    if x <= 0 or y <= 0:
        print("Error: Los números deben ser positivos")  # Error
        return -1
    
    elif x == 1 or y == 1:
        return 1
    
    else:
        while x != y:
            if x > y:
                x = x - y
            else:
                y = y - x
        return x
    
