"""
eval() func -> Parsing of string equations

TODO: trig func support
TODO: sqrt symbol support
TODO: (maybe) algebra support
TODO: (interest) speed test vs eval
"""
# Supported operators and BIDMAS order of operations - global vars
bidmas = ['^', '*', '/', '_', '%', '-', '+']  # NOTE: _ is alias for floor division
operators = "+-*/()^%_"

replace_ops = [('//', '_')]  # [(operator to replace, operator to replace with)]

def lex(eq: str) -> []:
    """
    Lexing stage - splits into full numbers and
    :param eq: string in form of equation
    :return:
    """
    strings = []
    # Lexing
    number = ""
    isNumbering: bool = False  # Flag for number recognition
    for char in eq:
        if char == " ":
            # Ignore white space
            continue
        global operators
        if char in operators:
            if isNumbering:
                isNumbering = False
                strings.append(float(number))
                number = ""
            if char == '-':
                if eq.index(char) == 0 or eq[eq.index(char)-1] in operators:
                    isNumbering = True
                    number += char
                else:
                    strings.append(char)
            else:
                strings.append(char)
        else:
            if char.isnumeric() or char == '.':
                isNumbering = True
                number += char
            else:
                print("SYNTAX ERROR")
    if number != "":
        strings.append(float(number))
        number = ""
    return strings


def bracket_madness(strings: [str, float]) -> float:
    """
    Carry out calculation of lexed equation
    Calls getResult when brackets dealt with
    :param strings: list of lexed floats and str operators
    :return: Result from equation
    """
    if '(' in strings and ')' not in strings:
        print("BRACKET ERROR")
        return None
    elif '(' not in strings and ')' in strings:
        print("BRACKET ERROR")
        return None
    if '(' not in strings:
        return getResult(strings)
    bOpen = -1
    for i, char in enumerate(strings):
        if char == '(':
            bOpen = i
        if char == ')':
            if bOpen != -1:
                res = []
                res.extend(strings[:bOpen])
                res.append(getResult(strings[bOpen+1:i]))
                res.extend(strings[i+1:])
                return bracket_madness(res)


def getResult(eq) -> float:
    """
    Carries out parsing on already lexed eq with brackets removed
    :param eq: lexed eq
    :return: value of equation
    """
    # Parse
    global bidmas
    mode = 0

    def splitOn2(bidmasElement, focus) -> [str]:
        for bi in bidmasElement[::-1]:
            for i in range(len(focus) - 1, 0, -1):
                char = focus[i]
                if char == bi:
                    if char == '/':
                        indLast = len(focus) - 1 - focus[::-1].index(char)
                        if i == indLast:
                            split = [focus[:i], focus[i + 1:]]
                            return [splitOn2(bidmasElement, split[0]), bi, splitOn2(bidmasElement, split[1])]
                        else:
                            continue
                    else:
                        split = [focus[:i], focus[i + 1:]]
                        return [splitOn2(bidmasElement, split[0]), bi, splitOn2(bidmasElement, split[1])]
        return focus

    strings = splitOn2(bidmas, eq)

    # Evaluation
    def evaluate(string):
        if len(string) == 1:
            return string[0]
        match(string[1]):
            case '/':
                return evaluate(string[0]) / evaluate(string[2])
            case '*':
                return evaluate(string[0]) * evaluate(string[2])

            case '+':
                return evaluate(string[0]) + evaluate(string[2])

            case '-':
                return evaluate(string[0]) - evaluate(string[2])
            case '^':
                return evaluate(string[0]) ** evaluate(string[2])
            case '%':
                return evaluate(string[0]) % evaluate(string[2])
            case '_':
                return evaluate(string[0]) // evaluate(string[2])

    return evaluate(strings)

def maina(eq):
    for op, rep in replace_ops:
        eq.replace(op, rep)
    return bracket_madness(lex(eq))


if __name__ == '__main__':
    eq = input(">>> ")
    for op, rep in replace_ops:
        eq.replace(op, rep)
