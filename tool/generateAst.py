import argparse

TYPES = [
    "Binary : Expr left, Token operator, Expr right",
    "Grouping : Expr expression",
    "Literal : object value",
    "Unary : Token operator, Expr right"
]

def define_ast(output_dir: str, base_name: str, types: list[str]) -> None:
    path = output_dir + '/' + base_name.lower() + '.py'
    f = open(path, "x")
    f.write("from abc import ABC, abstractmethod\n")
    f.write("from lox_token import Token")
    f.write("\n\n")
    f.write(f"class {base_name}(ABC):\n")
    f.write("\tpass\n\n")

    for type in types:
        class_name = type.split(":")[0].strip()
        fields = type.split(":")[1].strip()
        define_type(f, base_name, class_name, fields)
    
        f.write("\t@abstractmethod\n")
        f.write("\tdef accept(visitor):\n")
        f.write("\t\treturn visitor.visit" + class_name + base_name + "()\n\n")
    
    define_visitor(f, base_name, types)


def define_visitor(f, base_name: str, types: list[str]) -> None:
    f.write("class Visitor(ABC):\n")
    for type in types:
        type_name = type.split(":")[0].strip()
        f.write("\tdef visit" + type_name + base_name + "(" + base_name.lower() + ": " + type_name + "):\n")
        f.write("\t\tpass\n\n")
    f.write("\n")


def define_type(f, base_name: str, class_name: str, fields: str) -> None:
    f.write(f"class {class_name}({base_name}):\n")
    init_str = "\tdef __init__(self{}):\n"
    field_list = fields.split(", ")

    arg_str = ""
    setter_str = ""
    for field in field_list:
        field_type, field_name = field.split(" ")
        arg_str += f", {field_name}: {field_type}"
        setter_str += f"\t\tself.{field_name} = {field_name}\n"

    f.write(init_str.format(arg_str))
    f.write(setter_str)
    f.write("\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Ast code')
    parser.add_argument('output_dir')
    parser.add_argument('base_name')
    args = parser.parse_args()
    define_ast(args.output_dir, args.base_name, TYPES)