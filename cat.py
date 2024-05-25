import sys


def cat(file: str) -> None:
    try:
        with open(file, "r") as f:
            print(f.read())
    except FileNotFoundError:
        raise FileNotFoundError(f"cannot find {file}")


def main() -> None:
    try:
        cat(sys.argv[1])
    except IndexError:
        print("missing file name")
    except FileNotFoundError:
        print(f"cant find {sys.argv[1]}")


if __name__ == "__main__":
    main()
