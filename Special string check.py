while True:
    getString = input ("Provide checking-desired string: ")

    for i in range(0, len(getString)-2):
        if getString[i] == getString[i+2]:
            print("It is special!!!")
            break
        else:
            print("Try again!")
            break