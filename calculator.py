import sys


def calculator(num1: float = 0, num2: float = 0, operator: str = "") -> float:
    """

    utilise la reverse polish notation
    :param num1: premier chifre de operation
    :param num2: deuxiemme chiffre de operation
    :param operator: l'operateur {+,-,*,/,^,%}
    :return: resulta(float)
    :raise: ZeroDivisionError
    """

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            raise ZeroDivisionError("can't divide by zero")
    elif operator == "^":
        return num1 ** num2
    elif operator == "%":
        return num1 % num2


def print_help() -> None:
    """
    print the help menu
    :return:
    """
    print("enter your equation in reverse polish notation"
          "if you don't know wath it his go check that link out: https://en.wikipedia.org/wiki/Reverse_Polish_notation")


def print_version() -> None:
    """
    function qui print la version
    :return:
    """
    print("version 1.0 by Nicolas Prigge")


def main() -> None:
    """
    fonction principal du code
    :return:
    """
    try:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print_help()
        elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
            print_version()
        else:
            print(f"result: {calculator(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3])}")

    except IndexError:
        print("please enter something")

    except ZeroDivisionError:
        print("don not divide by zero")


if __name__ == "__main__":
    main()
