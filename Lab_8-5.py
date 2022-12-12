#author ate (12/6/22)

def count_a(sent):
    count = "a"
    word = "Alakazam"
    for letter in sent:
        if letter in word:
            count += 1
    return count

#print statement
print(count_a)