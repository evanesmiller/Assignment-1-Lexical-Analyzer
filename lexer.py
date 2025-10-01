keywords = {'int', 'float', 'double', 'char', 'while', 'if', 'else', 'ADD MORE'}    # set of reserved words
operators = {'+', '-', '*', '/', '%', '=', '==', '<', '>', '||', '&&', 'ADD MORE'}  # set of operator symbols 
separators = {'(', ')', '{', '}', '[', ']', ',', ';', ':', '.', 'ADD MORE'}         # set of separator symbols 

def lex_identifier(text, i):
    state = "start"              # finite-state machine starts in "start" state
    lexeme = ""                  # will use characters that form the identifier

    while i < len(text):         # loop while we still have characters to read
        ch = text[i]             # created ch to look at current character at index i

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
    if i >= len(text) or not text[i].isdigit():    # must start with a digit or fail immediately
        return None                                # not an integer token starting here
    start = i                                      # remember where the integer begins
    while i < len(text) and text[i].isdigit():     # consume all consecutive digits
        i += 1                                     # advance through the digit run
    return "Integer", text[start:i], i             # return token type, the digits, and next index

def lex_real(text, i):
    j = i                                          # j scans the integer part before the dot
    while j < len(text) and text[j].isdigit():     # consume any leading digits
        j += 1                                     # advance through the digits
    if j < len(text) and text[j] == '.':           # require a decimal point to consider a real
        j += 1                                     # skip the '.'
        k = j                                      # k will scan the fractional digits
        while k < len(text) and text[k].isdigit(): # consume digits after the dot
            k += 1                                 # advance through fractional digits
        if k > j:                                  # ensure at least one digit after the dot
            return "Real", text[i:k], k            # return real token from i up to k
    return None                                    # not a real number starting at i

def lexer(text, start_index):
    if start_index + 1 < len(text):                     # make sure a 2-char slice is in range
        two = text[start_index:start_index+2]           # take two characters for multi-char operator check
        if two in operators:                            # if it's a known 2-char operator (==, &&, ||, etc.)
            return ("Operator", two, start_index + 2)   # return operator and advance by 2

    result = lex_identifier(text, start_index)     # try to recognize an identifier/keyword first
    if result:
        return result                              # if matched, we’re done

    ch = text[start_index] if start_index < len(text) else ''   # safely read current char (or empty at EOF)
    if ch.isdigit():                                            # if it starts with a digit, try number lexers
        result = lex_real(text, start_index)                    # try real first so 12.34 isn't split
        if result:
            return result                                       # return real token if matched
        result = lex_integer(text, start_index)                 # otherwise try integer
        if result:
            return result                           # return integer token if matched

    ch = text[start_index]                          # re-read the current character
    if ch in operators:                             # check single-character operators
        return ("Operator", ch, start_index + 1)    # return 1-char operator token
    if ch in separators:                            # check separators (punctuation-like)
        return ("Separator", ch, start_index + 1)   # return 1-char separator token

def main():
    with open("source.rat25f", "r") as f:           # open source file for reading
        source_code = f.read()                      # read entire source into a string

    index = 0                                       # current scanning position
    with open("output.txt", "w") as out:            # open output file for tokens
        while index < len(source_code):             # scan until we hit end of input
            if source_code[index].isspace():        # skip whitespace characters
                index += 1                          # move past the whitespace
                continue                            # continue with next loop iteration

            result = lexer(source_code, index)                  # attempt to lex a token at current index
            if not result:                                      # if nothing matched here
                print(f"Unknown: {repr(source_code[index])}")   # report unrecognized character
                index += 1                                      # skip one char to avoid infinite loop
                continue                                        # try lexing again at the next position

            token, lexeme, index = result           # unpack token type, lexeme text, and next index
            line = f"{lexeme:<12} | {token}"        # format a display line for terminal/file
            print(line)                             # emit token to terminal
            out.write(line + "\n")                  # write token to output file

if __name__ == "__main__":                          # run only when executed as a script (not imported)
    main()                                          # call the entry point
