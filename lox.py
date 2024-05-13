import argparse
import sys

class Lox:
    
    def run_file(self, path:str) -> None:
        if self.had_error:
            return
        f = open(path, "r")
        self.run(f.read)
    
    def run_prompt(self) -> None:
        while True:
            print("> ")
            line = input()
            if line == None:
                continue
            self.run(line)
            self.had_error = False
    
    def run(self, source: str) -> None:
        print(source)
    #     self.scanner = Scanner()
    #     tokens = scanner.scan_tokens()

    #     for token in tokens:
    #         print(token)

    def error(self, line: int, message: str) -> None:
        self.report(line, "", message)
    
    def report(self, line: int, where: str, message: str) -> None:
        print("[line " + line + "] Error" + where + ": " + "message")
        self.had_error = True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lox interpreter in python')
    parser.add_argument('-filename')
    args = parser.parse_args()

    lox = Lox()

    if args.filename == None:
        lox.run_prompt()
        
