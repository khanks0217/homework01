
words = []

with open('words', 'r') as f:
    words = f.read().splitlines()
    words.sort(key=len, reverse = True)
    #sort function "key" tells how, reverse = true sorts in descending
    for i in range(5):
        print (words[i])
