print("Welcome to the Quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Excellent! Let's proceed.")

score = 0

answer = input("What is the highest-ranking hand in a Poker game? ")
if answer == "Royal Flush":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the minimum point recommended to bid eight in a Trump-Pass game? ")
if answer == "12":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What is the total points a Queen, a Rook, a Bishop, and a Knight worth in chess? ")
if answer == "20":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What is the highest card in a Capsa game? ")
if answer == "Deuce of Spades":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What card is played first in a Seven game? ")
if answer == "Seven of Spades":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"Your score is {str(score)} out of 5.")
if score == 5:
    print("PERFECT!")
elif score < 5 and score >= 3:
    print("AWESOME!")
elif score < 3 and score >= 1:
    print("NOT BAD!")
else:
    print("YOU ARE AN IDIOT!")
    
print("/nTHE END")