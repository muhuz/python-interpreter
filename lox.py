import argparse
import sys

from scanner import Scanner

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
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()

        for token in tokens:
            print(token)

    @staticmethod
    def error(line: int, message: str) -> None:
        Lox.report(line, "", message)
    
    @staticmethod
    def report(line: int, where: str, message: str) -> None:
        print("[line " + line + "] Error" + where + ": " + message)
        Lox.had_error = True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lox interpreter in python')
    parser.add_argument('-filename')
    args = parser.parse_args()


    if args.filename == None:
        Lox.run_prompt()
        
