def is_palindrome_recursive(word, low_index, high_index):
    # Verificar se a palavra é vazia
    if word == "":
        return False

    # Condição de parada: índices se encontram ou se cruzaram
    if low_index >= high_index:
        return True

    # Verificar se os caracteres nos índices baixo e alto são diferentes
    if word[low_index] != word[high_index]:
        return False

    # Chamada recursiva com os índices atualizados
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


# Uma forma de resolver se pensar na recursividade:
# def is_palindrome(word):
#     if not word:
#         return False
#    Inverter a palavra usando a sintaxe de fatiamento
#     reversed_word = word[::-1]

#     return word == reversed_word
