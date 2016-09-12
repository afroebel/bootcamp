seq1 = input('Input seq1')
seq2 = input('Input seq2')
a = len(seq1)
b = len(seq2)
d = abs(len(seq1)-len(seq2))
i = 0
j = 0

def e14(seq1, seq2):
    if seq1 == seq2:
        print(seq1)

    elif a == b or a < b:
        i = 0
        j = 0
        f = 0
        m = a
        x = m
        y = m
        while seq1[i:(i + m - f)] != seq2[j:(j + m - f)]:
            j += 1
            f += 1
            print(seq2[i:(i + m - f)])

    else:
        i = 0
        j = 0
        f = 0
        m = b
        x = m
        y = m
        while seq1[i:(i + m - f)] != seq2[j:(j + m - f)]:
            i += 1
            f += 1
            print(seq2[j:(j + m - f)])
