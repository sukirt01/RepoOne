operator = {
    "+": "Addition",
    "-": "Subtraction",
    "/": "Division",
    "*": "Multiplication",
    "++": "Unary Increment",
    "--": "Unary Decrement",
}

inputOperator = input("Input Enter any operator: ")
isOperator = False

for key in operator.keys():
    if inputOperator == key:
        isOperator = True
        print("Output: ", operator.get(key))

if isOperator == False:
    print("Invalid Operator")

inputData = input("Input Enter any data: ")
print("Output: ", end="")

if inputData.__len__() == 1 and not inputData.isdigit():
    print("Char")
elif (
    inputData == "True"
    or inputData == "true"
    or inputData == "false"
    or inputData == "False"
):
    print("Boolean")
elif inputData.isdecimal() and inputData.__contains__("."):
    print("Float")
elif inputData.isnumeric():
    print("Integer")
elif inputData.isalnum() or (inputData.startswith('"') and inputData.endswith('"')):
    print("String")
