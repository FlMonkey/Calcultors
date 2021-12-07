print("my first shot at a calculator :)")


n1 = int(input("N1: "))
op = input("OP: ")
n2 = int(input("N2: "))

#OG calculate
if op == "+":
    result = n1 + n2
    print("result: " + str(result))
elif op == "-":
    result = n1 - n2
    print("result: " + str(result))
elif op == "*":
    result = n1 * n2
    print("result: " + str(result))
elif op == "/":
    result = n1 / n2
    print("result: " + str(result))



#later calculate
while True:
    op1 = input("OP: ")
    if op1 == "+":
        n3 = int(input("N3: "))
        result = result + n3
        print("result: " + str(result))
    elif op1 == "-":
        n3 = int(input("N3: "))
        result = result - n3
        print("result: " + str(result))
    elif op1 == "*":
        n3 = int(input("N3: "))
        result = result * n3
        print("result: " + str(result))
    elif op1 == "/":
        n3 = int(input("N3: "))
        result = result / n3
        print("result: " + str(result))
    




