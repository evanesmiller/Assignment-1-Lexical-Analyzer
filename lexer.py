
keywords = {'int', 'float', 'double', 'char', 'while', 'if', 'else', 'ADD MORE'}
operators = {'+', '-', '*', '/', '%', '=', '==', '<', '>', '||', '&&', 'ADD MORE'}
seperators = {'(', ')', '{', '}', '[', ']', ',', ';', ':', '.', 'ADD MORE'}



def lex_indentifier(text, i):
    
    state = "start"
    lexeme = ""
    
    while i < len(text):
        ch  = text[i]

        if state == "start":
            if ch.isalpha():
                state = "id"
                lexeme += ch
                i += 1
            else:
                break
        elif state == "id":
            if ch.isalnum():
                lexeme += ch
                i += 1
            else:
                break
    if state == "id":
        token_type = "Keyword" if lexeme in keywords else "Identifier"
        return token_type, lexeme, i
    
    return None


def lex_integer(text, i):
    
    state = "start"
    lexeme = ""




def lex_real(text, i):
    
     state = "start"
     lexeme = ""



def lexer(text, start_index):

    # Identifer FSM
    result = lex_indentifier(text, start_index)
    if result:
        return result

    # Integer FSM
    result = lex_integer(text, start_index)


    # Real FSM
    result = lex_real(text, start_index)


    # Operators and Seperators
    ch = text[start_index]
    if ch in operators:
        return ("Operator", ch, start_index + 1)
    if ch in seperators:
        return ("Seperator", ch, start_index + 1)


def main():

    with open("source.rat25f", "r") as f:
        source_code = f.read()

    index = 0
    with open("output.txt", "w") as out:
        while index < len(source_code):
            if source_code[index].isspace():
                index += 1
                continue

            result = lexer(source_code, index)
            if not result:
                break

            token, lexeme, index = result
            out.write(f"{lexeme:<12} | {token}\n")
