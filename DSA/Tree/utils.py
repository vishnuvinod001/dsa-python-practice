import ast

def parse_input(arg):
    arg = arg.replace("null", "None")
    return ast.literal_eval(arg)