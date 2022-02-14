secret_word = "chupacabra"

while True:
    user_word = input("Please enter any word: ")
    user_word = user_word.lower()
    
    if user_word == secret_word:
       break

print("You've successfully left the loop.")
