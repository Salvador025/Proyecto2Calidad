def NumeroMax(x, y, z):    
    
    if x > y and x > z:
        max_value = x
        max_variable = "x"

    elif z > y:
        max_value = z
        max_variable = "z"
    else:
        max_value = y
        max_variable = "y"

    return f"El valor máximo es {max_value} y se encuentra en la variable '{max_variable}'"
    
