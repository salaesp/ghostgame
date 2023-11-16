#
 # Crea una función que encuentre todas las combinaciones de los números
 # de una lista que suman el valor objetivo.
 # - La función recibirá una lista de números enteros positivos
 #   y un valor objetivo.
 # - Para obtener las combinaciones sólo se puede usar
 #   una vez cada elemento de la lista (pero pueden existir
 #   elementos repetidos en ella).
 # - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
 #   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
 #   (Si no existen combinaciones, retornar una lista vacía)
 #


def find_nums(numbers: list, target: int) -> list:

    results = []

    def find_combinations(start: int, current_combination: list, target: int):
        
        if target == 0:
            results.append(current_combination[:])
            return
        
        if target < 0:
            return
        
        for index in range(start, len(numbers)):
            if numbers[index] in current_combination:
                continue

            current_target = target - numbers[index]
            current_combination.append(numbers[index])
            find_combinations(index + 1, current_combination, current_target)
            current_combination.pop()

    
    find_combinations(0, [], target)
    return results




print(find_nums([1,5,3,2], 6))
print(find_nums([0,3,2,5,2,10], 10))
