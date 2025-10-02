
keywords = {'int', 'float', 'double', 'char', 'while', 'if', 'else', 'ADD MORE'}
operators = {'+', '-', '*', '/', '%', '=', '==', '<', '>', '||', '&&', 'ADD MORE'}
seperators = {'(', ')', '{', '}', '[', ']', ',', ';', ':', '.', 'ADD MORE'}



def lex_indentifier(text, i):
    
    state = "start"
    lexeme = ""
    
    while i < len(text):
        ch  = text[i]

        if state == "start":     # at the beginning, we require a letter to start an identifier
            if ch.isalpha():     # letters start identifiers
                state = "id"     # move into the identifier-reading state
                lexeme += ch     # add the first character
                i += 1           # advance position
            else:
                break            # not a letter → this lexer can't consume anything; bail out
        elif state == "id":      # while inside an identifier
            if ch.isalnum():     # letters or digits are allowed to continue
                lexeme += ch     # append character
                i += 1           # advance position
            else:
                break            # any non-alnum ends the identifier

    if state == "id":                                                   # if we successfully read at least one char
        token_type = "Keyword" if lexeme in keywords else "Identifier"  # classify as keyword or identifier
        return token_type, lexeme, i                                    # return (type, text, next_index)

    return None # could not read an identifier at this position

def lex_integer(text, i):
    
    state = "start"
    lexeme = ""




def lex_real(text, i):
    
     state = "start"
     lexeme = ""



def lexer(text, start_index):
    if start_index + 1 < len(text):                     # make sure a 2-char slice is in range
        two = text[start_index:start_index+2]           # take two characters for multi-char operator check
        if two in operators:                            # if it's a known 2-char operator (==, &&, ||, etc.)
            return ("Operator", two, start_index + 2)   # return operator and advance by 2

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

            result = lexer(source_code, index)                  # attempt to lex a token at current index
            if not result:                                      # if nothing matched here
                print(f"Unknown: {repr(source_code[index])}")   # report unrecognized character
                index += 1                                      # skip one char to avoid infinite loop
                continue                                        # try lexing again at the next position

            token, lexeme, index = result
            out.write(f"{lexeme:<12} | {token}\n")
