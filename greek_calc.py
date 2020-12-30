#Greek simple calculator
#This program takes 2 numbers written in US or Greek way use of comma for floats


def asknumber(): #in this function I will ask the numbers and check if they are numbers
    x = input("Give me a number",)
    if "," in x:
        x=str.replace(x,",",".")
        x = check_input(x)
        return x
    elif x!=None:
        y=check_input(x)
        if y==None:
            return asknumber()
        else:
            return x
        
    


def check_input(number): # The checker function
    try:
        float(number)
    except ValueError:
        print("You didn't give me a number")
        number = None
    except:
        print("You didn't give me a number")
        number = None
    return number


def praxis():             # I ask what kind of calculation would be
    c = input("""What
    calculation you want to do?
    +,-,*,/
    """,)
    if c in ("+","-","*","/"):
        return c
    elif c == "x":
        c = "*"
        return c
    else:
        print("You didn't give me a praxis to do")
        c = None
        return c


def main():
    x = asknumber()      # Ask the first number until it takes a value
    if x == None:
        x = asknumber()
    else:
        x = float(x)
    operator = praxis()  # Ask the praxis
    if operator == None:
        operator = praxis()
    y = asknumber()      # Ask the 2nd number until it takes a value
    if y == None:
        y = asknumber()
    else:
        y = float(y)
    if operator == "+":
        result = x+y
    elif operator == "-":
        result = x-y
    elif operator == "*":
        result = x*y
    elif operator == "/" and y !=0:
        result = x/y
    else:
        result = "I cannot do this calculation"

    print(result)


main()
