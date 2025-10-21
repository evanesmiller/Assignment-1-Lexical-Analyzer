
keywords = {'integer', 'boolean', 'function', 'real',  'if', 'else', 'fi', 'return', 'put', 'get', 'while', 'true', 'false'}
operators = {'+', '-', '*', '/', '%', '=', '==', '<', '>', '||', '&&'}
separators = {'(', ')', '{', '}', '[', ']', ',', ';', ':', '.'}



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
                state = "integer"
                lexeme += ch
                i += 1
            else:
                break
        elif state == "integer":
            if ch.isdigit():
                lexeme += ch
                i += 1
            else:
                break
        
    if state == "integer":
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
    

 def lex_comment(text, i):
     state = "start"
     quote_found = False

    while i < len(text):
        ch = text[i]
        if state == "start"
            if ch == '"':
                i += 1


def lexer(text, start_index):

    # Identifier FSM
    result = lex_identifier(text, start_index)
    if result:
        return result

    # Real FSM
    result = lex_real(text, start_index)
    if result:
        return result
    
    # Integer FSM
    result = lex_integer(text, start_index)
    if result:
        return result

    

    # Operators and Separators
    ch = text[start_index]
    if ch in operators:
        return ("Operator", ch, start_index + 1)
    if ch in separators:
        return ("Separator", ch, start_index + 1)


def main():


    sources = ["source01.rat25f", "source02.rat25f", "source03.rat25f"]
    outputs = ["output01.txt", "output02.txt", "output03.txt"]

    for filename, output_filename in zip(sources, outputs):

        with open(filename, "r") as f:
            source_code = f.read()

        with open(output_filename, "w") as out:

            print("  Token         |      Lexeme\n")
            print("'''''''''''''''''''''''''''''\n")
            out.write("  Token         |      Lexeme\n")
            out.write("''''''''''''''''''''''''''''''\n")

        
            index = 0
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
