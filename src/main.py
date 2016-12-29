import requests
import parsing

def main():
    parse_obj = parsing.Parser()
    args = parse_obj.parse_arguments()
    print(args)

if __name__ == "__main__":
    main()
