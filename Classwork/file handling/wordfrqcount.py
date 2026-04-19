#
#Start
#Open article.txt in read mode
#Read content and convert to lowercase
#Remove punctuation
#split into words
#Count frequency using dictionary
#Display result
#Stop




import string
#open file in read mode 
with open("article.txt", "r") as file:
    text = file.read().lower()

# Remove punctuation
for p in string.punctuation:
    text = text.replace(p, "")

words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)