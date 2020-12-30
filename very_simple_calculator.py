#simple calculator

choices =int(input("""
What you want to do?
0 - Exit
1 - calculate something
""",))
while choices !=0:
    a = float(input("Give me a number\t",))
    b = float(input("Give me a number\t",))

    calc=input("What calculation you want to do",)
    result=""
    if calc == "+":
        result = a+b
        print(result)
        choices =int(input("""What you want to do?
                          0 - Exit
                          1 - calculate something
                          """,))
    elif calc == "-":
        result = a-b
        print(result)
        choices =int(input("""What you want to do?
                          0 - Exit
                          1 - calculate something
                          """,))
    elif calc == "*":
         result = a*b   
         print(result)
         choices =int(input("""What you want to do?
                          0 - Exit
                          1 - calculate something
                          """,))
    elif calc == "/":
        result = a/b
        print(result)
        choices =int(input("""What you want to do?
                          0 - Exit
                          1 - calculate something
                          """,))
if choices == 0:
    print("Goodbye")

