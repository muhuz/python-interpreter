import argparse

def define_ast(output_dir: str, base_name: str, types: list[str]) -> None:
    path = output_dir + '/' + base_name + '.py'
    f = open(path, "x")
    f.write("from abc import ABC, abstractmethod")
    f.write("\n\n")
    f.write(f"class {base_name}(ABC):\n")

    for type in types:
        class_name = type.split(":")[0].strip()
        fields = type.split(":")[1].strip()
        define_type(f, base_name, class_name, fields)

def define_type(f, base_name: str, class_name: str, fields: str) -> None:
    base_str = f"""
    class {class_name}({base_name}):
        def __init__():
    \t
    """
    for field in fields:
        name = field.split(" ")[1]
        base_str += f"self.{name} = {name}\n"
    f.write(base_str)
    f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Ast code')
    parser.add_argument('output_dir')
    parser.add_argument('base_name')
    parser.add_argument('types', nargs='+', default=[])
    args = parser.parse_args()
    define_ast(args.output_dir, args.base_name, args.types)