def main():
    x = int(input("Introduce x: "))
    y = int(input("Introduce y: "))
    z = int(input("Introduce z: "))

    if x > y and x > z:
        max_value = x
        max_variable = "x"

    elif z > y:
        max_value = z
        max_variable = "z"
    else:
        max_value = y
        max_variable = "y"

    print(f"El valor máximo es {max_value} y se encuentra en la variable {max_variable}")

if __name__ == '__main__':
    main()