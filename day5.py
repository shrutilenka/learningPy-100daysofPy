alpa = ['a', 'b', 'c']
for i in alpa:
    print(i)
print(alpa)

student_scores = [150, 200, 250, 300, 211, 156, 321, 400]
print(sum(student_scores))
print(max(student_scores))
print(min(student_scores))
print(sorted(student_scores))
print(sorted(student_scores, reverse=True))

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

sum = 0
for i in range(1, 101):
    sum = sum+i
print(sum)
