def adunare(a: float, b: float) -> float:
    return a + b


def scadere(a: float, b: float) -> float:
    return a - b


def inmultire(a: float, b: float) -> float:
    return a * b


def impartire(a: float, b: float) -> float:
    return a / b


def calculator(first_number: float, second_number: float, command: str) -> (str, float):

    if command == '+':
        return "Reusit", adunare(first_number, second_number)

    if command == '-':
        return "Reusit", scadere(first_number, second_number)

    if command == '*':
        return "Reusit", inmultire(first_number, second_number)

    try:
        if command == '/':
            c = first_number / second_number
            return "Reusit", impartire(first_number, second_number)
    except ZeroDivisionError:
        return "Alo vezi ca nu ai bagat ce trebuie", 0

    return "Nu cunoastem comanda", 0


def citire():
    try:
        a = float(input("First number\n"))
        b = float(input("Second number\n"))
        command = input("Command\n")
        return a, b, command, None
    except ValueError:
        return 0, 0, 0, "Ai eroare coane"


if __name__ == "__main__":
    a, b, command, error = citire()
    if error is None:
        print(calculator(a, b, command))
    else:
        print("Ce faci nene")

