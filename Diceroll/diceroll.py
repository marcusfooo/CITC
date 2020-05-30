from random import randrange # Import random library

name = input ("Enter your name: ")
print(" Hi", name,"! Try guessing my number. It's between 1-100 :)")

number = randrange(100) # Set a random number
guess = int(input("Whats your guess? ")) # Ask for a guess
tries = 1 # Start the count for number of tries

# While guess is wrong, give a hint
while guess != number:
    tries += 1 # Increment try count
    if guess > number:
        print("Too high! Try guessing lower")
        guess = int(input("Whats your guess? "))
    elif guess < number:
        print("Too low! Try guessing higher")
        guess = int(input("Whats your guess? "))

print("Sweet! Your guess is correct!\n You took a total of", tries, "tries!")