from stack import Stack

input_value = str(input("Enter your input string of brackets: "))

para = Stack()

def checkPara(check):
    peekValue = para.getPeek()
    print("I am getting here peak value", peekValue)
    if peekValue == -1:
        return 0
    else:
        if peekValue == "(":
            para.pop()
            return 1
        else:
            return -1
Flag = False
for char in input_value:
    if char == "(":
        para.push("(")
    elif char == ")":
        check = checkPara(char)
        if check == -1:
            break
        elif check == 0:
            print("Paraenthesis is unbalanced")
            Flag = True
            break
        else:
            continue
if Flag == False:
    if para.getPeek() == -1:
        print("Parenthesis is balanced")
    else:
        print("Paraentheis is unbalanced")
else:
    pass