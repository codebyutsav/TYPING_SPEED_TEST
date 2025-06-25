import time
import random

sentences=[
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language.",
    "Typing fast requires practice and focus.",
    "Always write clean and readable code.",
    "Debugging is twice as hard as writing the code."
]

sentence=random.choice(sentences)
print("Type the given sentence:\n")
print(sentence)
print()

start_time=time.time()

typed=input("Enter the sentence and press Enter when done:\n")

end_time=time.time()

time_elapsed = end_time - start_time
words=len(typed.split())
wpm=words/(time_elapsed/60)

correct_char=sum(1 for idx,item in enumerate(typed.strip()) if idx < len(sentence) and item == sentence[idx])
accuracy=(correct_char/len(sentence))*100

print("\n---Results---")
print(f"Time taken : {time_elapsed:.2f} seconds")
print(f"Speed : {wpm:.2f} WPM")
print(f"Accuracy : {accuracy:.2f}")