import random
EasyWordBank = ['tree', 'file' 'studio', 'world', 'pink', 'page', 'stay', 'hurt', 'silver', 'wings', 'apple', 'hang', 'music', 'battle', 'weary', 'storm' ]
DifficultWordBank = ['chicken', 'apricot', 'destiny', 'tedious', 'doctor', 'loading', 'content', 'quoted', 'length', 'socket', 'lining', 'blizzard', '']
HardWordBank = ['credentials', 'fantastic', 'function', 'discover', 'purpose', 'elongate', 'calendar', 'controller', 'indentation', 'observation', 'selection', 'simulation', 'pedestrian', 'willpower', 'archeology']
BlankOutput = []
HangmanWord = ''
WordLength = 0
Difficulty = ''

def ChooseDifficulty():
    global Difficulty
    Difficulty = input("At what difficulty would you like the word to be? (Easy/Difficult/Hard) ")
    

def ChooseWord():
    global HangmanWord
    global WordLength
    global Difficulty
    if Difficulty == 'Easy' or Difficulty == 'easy':
        BankLength = len(EasyWordBank)
        WordChoice = random.randint(0,BankLength)
        HangmanWord = EasyWordBank[WordChoice]
        WordLength = len(HangmanWord)
    if Difficulty == 'Difficult' or Difficulty == 'difficult':
        BankLength = len(DifficultWordBank)
        WordChoice = random.randint(0,BankLength)
        HangmanWord = DifficultWordBank[WordChoice]
        WordLength = len(HangmanWord)
        
    if Difficulty == 'Hard' or Difficulty == 'hard':
        BankLength = len(HardWordBank)
        WordChoice = random.randint(0,BankLength)
        HangmanWord = HardWordBank[WordChoice]
        WordLength = len(HangmanWord)

def WordOutput():
    global BlankOutput
    for i in range(WordLength):
        BlankOutput.append("-")
    print(BlankOutput)

def PlayerGuess():
    global BlankOutput
    global WordLength
    global HangmanWord
    
    RemainingGuesses = 6
    Condition = 0
    while Condition == 0:
        WinChecker = 0
        WinTally = 0
        
        LetterGuess = input("Enter a letter ")
        Counter = 0
        Correct = 0
        for i in range (WordLength):
            if LetterGuess == HangmanWord[Counter]:
                BlankOutput[Counter] = LetterGuess
                print(BlankOutput)
                print("")
                Counter = Counter + 1
                Correct = Correct + 1
                
            else:
                Counter = Counter + 1
                if Counter == WordLength and Correct == 0:
                    RemainingGuesses = RemainingGuesses - 1
                    print("That letter was wrong, Guesses left", RemainingGuesses)
                    print(BlankOutput)
        
        if RemainingGuesses == 0:
            print("Unfortunately you've ran out of guesses and have lost the word was ", HangmanWord)
            Condition = 1
            

        for i in range(WordLength):
            if BlankOutput[WinChecker] == HangmanWord[WinChecker]:
                WinChecker = WinChecker + 1
                WinTally = WinTally + 1
                if WinTally == WordLength:
                    print("Congrats you guessed the word correctly the word was", HangmanWord)
                    Condition = 2
    
    Restart = input("Would you like to play again Y/N ")
    if Restart == 'Y' or Restart == 'Yes' or Restart == 'yes' or Restart == 'y':
        StartGame()


def StartGame(): 
    global BlankOutput
    global WordLength
    global HangmanWord
    global Difficulty
    BlankOutput = []
    HangmanWord = ''
    WordLength = 0   
    Difficulty = '' 
    ChooseDifficulty()  
    ChooseWord()
    WordOutput()
    PlayerGuess()

StartGame()