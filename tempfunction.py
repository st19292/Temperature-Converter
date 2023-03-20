def check_temp(min_value):
    error = f"Plaese enter a number that is more that {min_value}"

    try:
        response = float(input("Choose a number: "))

        if response < min_value:
            print(error)
        else:
            return response
    
    except ValueError:
        print(error)


while True:
    to_check = check_temp(-273)
    print("Success")
