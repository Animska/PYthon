# Dado un array de números y un número goal, encuentra los dos primeros números del
# array que sumen el número goal y devuelve sus índices. Si no existe tal combinación,
# devuelve None.


def find_first_sum(numeros, goal):
    for i in range(len(numeros)):
        for j in range(i+1, len(numeros)):
            if numeros[i] + numeros[j] == goal:
                return [i, j]
    return None

# Ejemplo de uso
nums = [4, 5, 6, 2]
goal = 8
print(find_first_sum(nums, goal))  # [2, 3]
