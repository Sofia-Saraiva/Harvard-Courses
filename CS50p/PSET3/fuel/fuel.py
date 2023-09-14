while True:
    try:
        fuel = input("Fuel: ")
        x, y = fuel.split("/")

        p = int(x) / int(y) * 100

        if round(p) <= 1:
            print("E")
            break
        elif 99 <= round(p) <= 100:
            print("F")
            break
        elif round(p) > 100:
            pass
        else:
            print(f"{round(p)}%")
            break
    except (ValueError, ZeroDivisionError):
        pass
