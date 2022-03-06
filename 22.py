def letter_to_number(letter :str) -> int:
    return ord(letter.upper()) - 64

def name_scores(path :str) -> int:
    all_score = 0
    pos = 1

    file = open(path)
    names = sorted(file.read().replace('"', '').split(','))

    for name in names:
        score = 0
        for i in range(0, len(name)):
            score += letter_to_number(name[i])
            i += 1

        all_score += score * pos
        pos += 1

    return all_score

print(name_scores('./resources/p022_names.txt'))