def move_ring(L1,L2):
    if L2 == [] or L1[0] < L2[0]:
        L2.append(L1.pop(0))
        L2.sort()
        return [L1,L2]
    else:
        print("No valid move")
        return (L1,L2)
k1 = [1,2,3]
print("k1",k1)
k2 = []
print("k2",k2)
k3 = []
print("k3",k3)
while True:
    try:
        f1=int(input("Move from Colon number:",))
        if f1 == 1 or f1 == 2 or f1 == 3:
            break
        else:
            print("There is no such a colon number")
    except ValueError:
        print("Choose colon number")
while True:
    try:
        f2=int(input("Move to Colon number:",))
        if f2 == 1 or f2 == 2 or f2 == 3:
            if f2 != f1:
                break
            else:
                print("You cannot move from the same Colon to the same Colon")
        else:
            print("There is no such a colon number")
    except ValueError:
        print("Choose colon number")   
if f1 == 1:
    if k1 != None:
        if f2 == 2:
            K=move_ring(k1,k2)
        elif f2 == 3:
            K=move_ring(k1,k3)
    else:
        print ("There is no ring left in this colon")




        
    
