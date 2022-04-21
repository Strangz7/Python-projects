# def bracket_validator(brackets: str):
#     if (brackets.startswith('(') and brackets.endswith(')')) or (brackets.startswith('{') \
#     and brackets.endswith('}')) or (brackets.startswith("[") and brackets.endswith("]")):
#         print('valid')
#     else:
#         print('invalid')

def bracket_validator(brackets: str):
    stack: list[str] = []
    for bracket in brackets:
        if bracket in "{[(":
            stack.append(bracket)
        if bracket in "}])":
            if bracket == "}" and stack[-1] == "{":
                stack.pop()
            elif bracket == "]" and stack[-1] == "[":
                stack.pop()
            elif bracket == ")" and stack[-1] == "(":
                stack.pop()
            else:
                return False
    return len(stack) == 0
print(bracket_validator("{()()}"))