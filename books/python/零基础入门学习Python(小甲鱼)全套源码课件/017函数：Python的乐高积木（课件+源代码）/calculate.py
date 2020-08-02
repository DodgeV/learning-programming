def calculate(temp):
    op = temp.find('+')
    if temp[op] == '+':
        num1 = float(temp[:op])
        num2 = float(temp[op+1:])
        return num1 + num2

    op = temp.find('-')
    if temp[op] == '-':
        num1 = float(temp[:op])
        num2 = float(temp[op+1:])
        return num1 - num2

    op = temp.find('*')
    if temp[op] == '*':
        num1 = float(temp[:op])
        num2 = float(temp[op+1:])
        return num1 * num2

    op = temp.find('/')
    if temp[op] == '/':
        num1 = float(temp[:op])
        num2 = float(temp[op+1:])
        return num1 / num2

temp = input("请输入一个算式：")
print(calculate(temp))
