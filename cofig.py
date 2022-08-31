operators = ["=", "+", "-", "*", "\\", "^", "\"", "\'", ".", "~", "|", "[", "]", "(", ")", ";", ":", "%", ",", "!", "<",
             ">", "&", "{", "}"]

python_keywords = ["def", "global", "for", "end", "while", "if", "else", "elif", "await", "pass", 
            "break", "try", "raise" "except", "end", "const", "int", "bool", "float", "from", 
            "import", "export", "type", "return", "True", "False", "in", "abstract", "is",
             "continue", "do", "join", "map", "list", "str", "None", "class", "finally", "and",
             "lambda", "as", "assert", "not", "with", "async", "or", "yield", "print"
            ]

def get_python_operators():
    return set(operators + python_keywords)

def get_python_operands():
    return []