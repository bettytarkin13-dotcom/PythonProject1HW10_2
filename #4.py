#q4
sentences = ["Hello world","Python is fun", "I love coding"]
all_words=[]
for sentence in sentences:
 words=sentence.split()
 all_words.extend(words)

print(all_words)

