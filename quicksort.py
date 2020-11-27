def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        dokimi = lista[0]
        less = [i for i in lista[1:] if i <= dokimi]

        greater = [i for i in lista[1:] if i >= dokimi]

        return quicksort(less) + [dokimi] + quicksort(greater)
import random
L=[]
for i in range(40):
    L.append(random.randint(1,20000))
    

print(L)
print (quicksort(L))
