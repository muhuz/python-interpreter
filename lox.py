import argparse

import scanner

class Lox:
    
    @staticmethod
    def run_file(path: str) -> None:
        if Lox.had_error:
            return
        f = open(path, "r")
        Lox.run(f.read)
    

    @staticmethod
    def run_prompt() -> None:
        while True:
            print("> ")
            line = input()
            if line == None:
                continue
            Lox.run(line)
            Lox.had_error = False

    @staticmethod
    def run(source: str) -> None:
        scan = scanner.Scanner(source)
        tokens = scan.scan_tokens()

        for token in tokens:
            print(token)

    @staticmethod
    def error(line: int, message: str) -> None:
        Lox.report(line, "", message)
    
    @staticmethod
    def report(line: int, where: str, message: str) -> None:
        print("[line " + str(line) + "] Error" + where + ": " + message)
        Lox.had_error = True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lox interpreter in python')
    parser.add_argument('-filename')
    args = parser.parse_args()


    if args.filename == None:
        Lox.run_prompt()
        
