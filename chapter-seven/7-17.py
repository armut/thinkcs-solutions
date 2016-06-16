# exercise 7.17

def play_once(human_plays_first):
    import random
    rng = random.Random()
    result = rng.randrange(-1,2)
    print("Human plays first={0}, winner={1} ".format(human_plays_first, result))
    return result


score = [0, 0, 0]
player = -1
while True:
    if player == -1:
        player = int(input("Who is the first player? Human(1) or Computer(0) : "))
    elif player == 0:
        player = 1
    else:
        player = 0
        
    result = play_once(player)
    if result == -1:
        print("I win!")
        score[0] += 1
    elif result == 0:
        print("Game drawn")
        score[1] += 1
    else:
        print("You win!")
        score[2] += 1

    print("Score | I win |\tYou win | Drawn")
    print("----------------------------")
    print("       {0} \t {1} \t {2}".format(score[0], score[2], score[1]))
    percentage = (100 * score[2]) / (score[0] + score[1] + score[2])
    print("Percentage of wins for the human: {0}".format(percentage))
    response = input("Do you want to play again? (y/n): ")
    if response != "y":
        break

print("Goodbye!")

