def move_ring(L1,L2):
    if L2 == [] or L1[0] < L2[0]:
        L2.append(L1.pop(0))
        L2.sort()
        return [L1,L2]
    else:
        print("No valid move")
        return (L1,L2)
k1=[1,2,3]
k2=[]
k3=[]
moves=0
print ("k1",k1,"k2",k2,"k3",k3)
print("Move ring from k1 to k3")
m=move_ring(k1,k3)
moves+=1
k1=m[0]
k3=m[1]
print("moves:", moves)
print ("k1",k1,"k2",k2,"k3",k3)
print("Move ring from k1 to k2")
m=move_ring(k1,k2)
moves+=1
k1=m[0]
k2=m[1]
print("moves:", moves)
print ("k1",k1,"k2",k2,"k3",k3)
print("Move ring from k3 to k2")
m=move_ring(k3,k2)
moves+=1
k3=m[0]
k2=m[1]
print("moves:", moves)
print ("k1",k1,"k2",k2,"k3",k3)
print("Move ring from k1 to k3")
m=move_ring(k1,k3)
moves+=1
k1=m[0]
k3=m[1]
print("moves:", moves)
print ("k1",k1,"k2",k2,"k3",k3)
print("Move ring from k2 to k1")
m=move_ring(k2,k1)
moves+=1
k2=m[0]
k1=m[1]
print("moves:", moves)
print ("k1",k1,"k2",k2,"k3",k3)
print("Move ring from k2 to k3")
m=move_ring(k2,k3)
moves+=1
k2=m[0]
k3=m[1]
print("moves:", moves)
print ("k1",k1,"k2",k2,"k3",k3)
print("Move ring from k2 to k3")
m=move_ring(k1,k3)
moves+=1
k2=m[0]
k3=m[1]
print("moves:", moves)
print ("k1",k1,"k2",k2,"k3",k3)
