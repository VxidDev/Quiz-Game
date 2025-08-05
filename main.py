from random import choice

questions = ["What is the capital of France?" , "What is 5 + 7?" , "What color do you get when you mix red and white?" , "How many continents are there?" ,
            "What planet is known as the Red Planet?" , "What is the boiling point of water in Celsius?" , "What is the largest ocean on Earth?" , 
            "Who wrote 'Romeo and Juliet'?" , "What is the fastest land animal?" , "What is the square root of 64?"]

answers = ["paris" , "12" , "pink" , "7" , "mars" , "100" , "pacific" , "shakespeare" , "cheetah" , "8"]

points = 0

for i in range(0 , 3):
    x = choice(questions)
    z = answers[questions.index(x)]

    print(f"\n{x}")
    user_input = input("\nAnswer: ").lower()
    if user_input == z:
        points += 1
        print("\nYou're right! +1 point!")
        answers.remove(questions.index(x))
        questions.remove(x)

print(f"Your points are: {points}! Well done!")