def hangman(word):
    wrong = 0
    stages = ["",
              "________       ",
              "|              ",
              "|       |      ",
              "|       O      ",
              "|      -|-     ",
              "|      ! !     ",
              "|              ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcom to Hangman! stages:{}".format(len(stages)-1))
    while wrong < len(stages) - 1:
        print("\n")
        char = input("Guess one letter: ")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        print("***debug***", "wrong: {}".format(wrong))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lost. Answer is {}.".format(word))

if __name__ == "__main__":
    print("---Start of hangman---")
    hangman("cat")
