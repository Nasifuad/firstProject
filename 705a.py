
n = int(input())  # Read input
feelings = []

for i in range(1, n + 1):
    if i % 2 == 1:
        feelings.append("I hate")
    else:
        feelings.append("I love")

    if i != n:
        feelings.append("that")

feelings.append("it")

print(" ".join(feelings))
