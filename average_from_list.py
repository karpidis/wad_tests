import random
random_lista = [random.randint(0, 1000000) for i in range(50)]


def mesos_oros(x):
    return sum(x)/len(x)


print(mesos_oros(random_lista))
