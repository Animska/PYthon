# Dado un array de números y un número goal, encuentra los dos primeros números del
# array que sumen el número goal y devuelve sus índices. Si no existe tal combinación,
# devuelve None.


def find_first_sum(numeros,goal):
    for index,numero in enumerate(numeros):
        for index2,_ in enumerate(numeros):
            print(index,numero)


nums = [4, 5, 6, 2]
goal = 8
find_first_sum(nums, goal) # [2, 3]