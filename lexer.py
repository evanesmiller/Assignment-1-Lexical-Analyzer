
keywords = {'int', 'float', 'double', 'char', 'while', 'if', 'else'}
operators = {'+', '-', '*', '/', '%', '=', '==', '<', '>', '||', '&&'}
seperators = {'(', ')', '{', '}', '[', ']', ',', ';', ':', '.'}



def lex_identifier(text, i):
    
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

    while i < len(text):
        ch = text[i]
        if state == "start":
            if ch.isdigit():
                state = "int"
                lexeme += ch
                i += 1
            else:
                break
        elif state == "int":
            if ch.isdigit():
                lexeme += ch
                i += 1
            else:
                break
        
    if state == "int":
        return "Integer", lexeme, i
    return None



def lex_real(text, i):
    
    state = "start"
    lexeme = ""
    decimal_found = False

    while i < len(text):
         ch = text[i]
         if state == "start":
            if ch.isdigit():
                 state = "real"
                 lexeme += ch
                 i += 1
            else:
                break
         elif state == "real":
            if ch.isdigit():
                 lexeme += ch
                 i += 1
            elif ch == "." and not decimal_found:
                decimal_found = True
                lexeme += ch
                i += 1
            else:
                break

    if decimal_found:
        return "Real", lexeme, i
    return None
    

         


def lexer(text, start_index):

    # Identifer FSM
    result = lex_identifier(text, start_index)
    if result:
        return result

    # Integer FSM
    result = lex_integer(text, start_index)
    if result:
        return result

    # Real FSM
    result = lex_real(text, start_index)
    if result:
        return result

    # Operators and Seperators
    ch = text[start_index]
    if ch in operators:
        return ("Operator", ch, start_index + 1)
    if ch in seperators:
        return ("Seperator", ch, start_index + 1)


def main():

    with open("source01.rat25f", "r") as f:
        source_code = f.read()

    index = 0
    with open("output.txt", "w") as out:

        print("  Token         |      Lexeme\n")
        print("'''''''''''''''''''''''''''''\n")
        out.write("  Token         |      Lexeme\n")
        out.write("''''''''''''''''''''''''''''''\n")

        while index < len(source_code):
            if source_code[index].isspace():
                index += 1
                continue

            result = lexer(source_code, index)
            if not result:
                break

            token, lexeme, index = result
            
            print(f"{token:<15} | {lexeme:>10}\n")
            out.write(f"{token:<15} | {lexeme:>10}\n")


if __name__ == "__main__":
    main()
