spec = """"!@#$%^&*()+=|\/?±§~1234567890[]:;"_,.`{}<>"""  # вся возможная пунктуация
lasts = """'-"""

def collector(inp, outp):
    d = dict()
    words3 = []
    with open(inp, 'r', encoding="utf-8") as f:
        for words in f:
            for i in spec:  # запускаем цикл по пунктуации
                words = words.replace(i, ' ')  # делю строки на слова
            words = words.split()  # массив слов
            for j in words:
                if j[0] in lasts:
                    j = j[1:]
                    if len(j) == 0:
                        continue
                if j[-1] in lasts:
                    j = j[:-1]
                    if len(j) == 0:
                        continue
                if len(j) != 0:
                    a = j.lower()
                    words3.append(a)
                    if a in d:
                        d[a] += 1
                    else:
                        d[a] = 1

    for i in range(len(words3)):
        a = words3[i]
        x = d[a]
        d[a] = str(x) + ' ' + str(i + 1)
    with open(outp, 'w', encoding="utf-8") as wrt:
        for k, v in d.items():  # в к хранит слова а в v позиция слова
            wrt.write(str(k) + ' ' + str(v) + '\n')
           


if __name__ == "__main__": 
	collector('input.txt', 'output.txt')
