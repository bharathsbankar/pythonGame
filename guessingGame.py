from random import randint
class NumberGuessingGame:
    def __init__(self,min_value,max_value):
        self.min_value=min_value
        self.max_value=max_value
        self.secret_number=randint(self.min_value,self.max_value)
        self.attempts=0
        self.max_attempts=10

    def guess(self,player_guess):
        self.attempts+=1
        if player_guess<self.secret_number:
            return "----------------------------------------too low-<<<<<<<<"
        elif player_guess>self.secret_number:
            return "----------------------------------------too high->>>>>>>"
        else:
            return ":-correct-:"
    def is_game_over(self):
        return self.attempts==self.max_attempts
    def reset_game(self):
        self.secret_number = randint(self.min_value, self.max_value)
        self.attempts = 0

if __name__=="__main__":
    print("welcome to number guessing game")
    lowerLimit=int(input("enter a lower limit :"))
    upperLimit=int(input("enter a upper limit :"))
    game=NumberGuessingGame(lowerLimit,upperLimit)

    while not game.is_game_over():
        if game.attempts!=0:
            print("************** try again **************")

        print(f"remaining attempts : {game.max_attempts-game.attempts} \nGuess a number  between {game.min_value} and {game.max_value} ")
        try:
            a=int(input("enter a guess num :"))
        except ValueError:
            print("invalid input\n************** try again **************")
            continue
        if a<game.min_value or a>game.max_value:
            print("out of bounds !\n************** try again **************")
            continue
        result=game.guess(a)
        print(result)
        if a==game.secret_number:
            print("************** { congratulations you won } *************")
            game.reset_game()
            break
        if game.is_game_over():
            print("**************you lost**************")
            print(f"the correct answer was {game.secret_number}")
            game.reset_game()
            break

