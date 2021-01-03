import random
l = [random.randint(0, 1000000) for i in range(50)]
print(l)


def mesos_oros(x):
    sum = 0
    for i in x:
        sum += i
    sum = sum/50
    return sum


print(mesos_oros(l))
