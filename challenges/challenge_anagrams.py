def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def is_anagram(first_string, second_string):
    if first_string is None or second_string is None:
        return first_string, second_string, False

    if first_string == "" and second_string == "":
        return first_string, second_string, False

    # Converte as strings para minúsculas
    first_string = first_string.lower()
    second_string = second_string.lower()

    # Ordena as strings usando o Merge Sort
    sorted_first = merge_sort(list(first_string))
    sorted_second = merge_sort(list(second_string))
    new_first = "".join(sorted_first)
    new_second = "".join(sorted_second)

    # Verifica se as strings ordenadas são iguais
    return new_first, new_second, new_first == new_second
