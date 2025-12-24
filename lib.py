def count_common_elements(*lists):
    """
    Принимает произвольное количество списков.
    Возвращает количество элементов, которые встречаются в каждом из этих списков.
    """
    if not lists:  # Если списков не передано
        return 0

    # Находим пересечение множеств всех переданных списков
    common_elements = set(lists[0])
    for current_list in lists[1:]:
        common_elements.intersection_update(current_list)

    # Возвращаем количество элементов в пересечении
    return len(common_elements)

# Пример использования функции
if __name__ == "__main__":
    list1 = [1, 2, 3, 4]
    list2 = [2, 3, 4, 5]
    list3 = [3, 4, 5, 6]

    result = count_common_elements(list1, list2, list3)
    print(f"Количество одинаковых элементов: {result}")  # Ожидается: 2 (элементы 3 и 4)