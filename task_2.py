def jaccard_index(set_a, set_b):

    intersection = len(set_a & set_b)
    union = len(set_a | set_b)


    if union == 0:
        return 0


    return intersection / union



a = {1, 2, 3}
b = {2, 3, 5}
result = jaccard_index(a, b)
print(f"Коэффициент Жаккара для множеств {a} и {b} равен {result:.2f}")