I = input().lower()

score = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(26):
    score.append(0)

for i in I:
    score[alphabet.index(i)] += 1

max_score = max(score)
max_score_count = 0

for i in score:
    if i == max_score:
        max_score_count += 1

if max_score_count > 1:
    print("?")
else:
    print(alphabet[score.index(max_score)].upper())