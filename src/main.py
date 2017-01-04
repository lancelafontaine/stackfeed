from src import parsing
import requests

def main():
    parse_obj = parsing.Parser()
    args = parse_obj.parse_arguments()
    print(args)

if __name__ == "__main__":
    main()
