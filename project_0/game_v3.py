"""Игра угадай число
Компьютер сам загадывет и сам отгадывает число (с коррекцией)
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Сначала рандомно устанавливаем число, а потом уменьшаем или увеличиваем его
        в зависимости от того, больше оно или меньше нужного.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    prdict_number = np.random.randint(1, 101) # первое произвольное число
    
    while number != prdict_number:
        count += 1

        if number > prdict_number:
            prdict_number += 1
        elif number < prdict_number:
            prdict_number -= 1
        
    return(count)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): фнуция угадывания

    Returns:
        int: среднее количество
    """
    count_ls = []
    #np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number)) 
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за:{score} попыток')
    return(score)

if __name__ == '__main__':
    # RUN
    score_game(random_predict)