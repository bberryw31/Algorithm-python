text = "Once upon a time, in a small village nestled among rolling hills, there lived a curious young girl named Lily. Lily had a boundless imagination and an insatiable thirst for adventure. Every day, she would wander through the meadows and explore the enchanting forests surrounding her village. One sunny morning, as Lily ventured deeper into the woods, she stumbled upon an ancient-looking book nestled beneath a majestic oak tree. With excitement sparkling in her eyes, she gently dusted off the book and opened its weathered pages. To her astonishment, the book contained a map leading to a hidden treasure! Determined to embark on a thrilling quest, Lily carefully traced the path marked on the map, memorizing each turn and landmark. With the map tucked securely in her bag, she set off on her grand adventure."

text2 = text.replace(",", "").replace(".","").replace("!","").lower()

text3 = text2.split()

word = []
wordcount = []

def counter(list):
    for i in range(len(list)):
        if list[i] not in word:
            word.append(list[i])
            wordcount.append(list.count(list[i]))

def sorter(list1, list2):
    for j in range(len(list1)):
        for k in range(1, len(list1)-j):
            if list2[k-1] > list2[k]:
                list1[k-1], list1[k] = list1[k], list1[k-1]
                list2[k-1], list2[k] = list2[k], list2[k-1]

counter(text3)
sorter(word, wordcount)

N = int(len(word))

for l in range(10):
    print(str(word[N-l-1]) + " : " + str(wordcount[N-l-1]))