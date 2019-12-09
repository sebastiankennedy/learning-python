import numpy

scores = [91, 95, 97, 99, 92, 93, 96, 98]
sum = numpy.sum(scores)
len = len(scores)
avg = sum / len
print(sum, len, avg)

result = []
for score in scores:
    if score < avg:
        result.append(score)
print(result)