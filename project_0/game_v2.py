import numpy as np

def game_v3(number: int = 1) -> int:
    """
    Угадываем число бинарным поиском.
    Функция принимает загаданное число и возвращает число попыток.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1
    high = 100

    while low <= high:
        count += 1
        predict = (low + high) // 2

        if predict == number:
            break
        elif predict > number:
            high = predict - 1
        else:
            low = predict + 1

    return count

# Функция для тестирования (из задания)
def score_game(random_predict) -> int:
    count_ls = []
    np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

# Тестируем
if __name__ == "__main__":
    print('Run benchmarking for game_v3: ', end='')
    score_game(game_v3)