from stack import Stack

input_Value = int(input("Enter your integer value for conversion to binary: "))
binaryStack = Stack()

while input_Value > 0:
    remainder = input_Value % 2
    input_Value = input_Value // 2
    binaryStack.push(remainder)
res = binaryStack.getStack()
print(res)
binary_value = ""
for i in range(len(res)-1,-1,-1):
    poped_value = res.pop()
    binary_value = binary_value + str(poped_value)
print(binary_value)