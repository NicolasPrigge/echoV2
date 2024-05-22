import sys
from colored import fg


def print_menu() -> None:
    print("usage: echo [option] [text] [color or file]")
    print("-t: print plain text")
    print("-f: append text to a file\nusage: echo [mode] [text] [file]")
    print("-c: print text in color\nusage: echo [mode] [text] [color]")


def echo(mode: str = "-t", text: str = "") -> None:
    """

    :param mode: le mode utilisation de la function -t si output text  -f si output dans un fichier
    :param text: le texte a append a un fichier ou a print
    :raise: index error si y manque le nom du fichier
    :return:
    """
    if mode == "-f":
        try:
            with open(sys.argv[3], "a") as f:
                f.write(text)
        except IndexError:
            raise IndexError("no file name given")
    elif mode == "-h":
        print_menu()
    elif mode == "-t":
        print(text)
    elif mode == "-c":
        try:
            color: str = fg(sys.argv[3])
            print(color + text)
            color = fg('white')
            print(color)
        except IndexError:
            raise IndexError("no color given")
    elif mode == "-h" or mode == "-help":
        print_menu()
    elif mode == "--version":
        print("echo version 1.0 by nicolas Prigge")


def main() -> None:
    """

    :raise: Index error si manque un argument lors de lappelle de la function
    :return:
    """
    try:
        echo(sys.argv[1], sys.argv[2])
    except IndexError:
        print("missing parameters")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
