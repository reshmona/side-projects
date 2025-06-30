def reverse_words(sentence):
    stack = []
    word = ""
    i = 0
    n = len(sentence)
    while i < n:
        if sentence[i] != " ":
            word += sentence[i]
        else:
            if word != "":
                stack.append(word)
                word = ""
        i += 1
    if word != "":
        stack.append(word)
    reversed_sentence = ""
    while stack:
        reversed_sentence += stack.pop()
        if stack:
            reversed_sentence += " "
    return reversed_sentence