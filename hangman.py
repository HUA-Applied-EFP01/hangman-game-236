import time
class HangmanGame:
    def __init__(self, word):
        self.word = word.lower()  # ορισμός της λέξης και αρχικοποίηση μεταβλητών, μετατροπή της λέξης σε πεζά γράμματα
        self.guesses_left = 6  # ορίζουμε πόσες μαντεψιές μπορεί να κάνει ο παίκτης
        self.guessed_letters = set()  # σύνολο που κρατάει τα γράμματα που έχει μαντέψει ο χρήστης χωρίς να μετράει τα γράμματα που μπορεί να επαναληφθούν
        self.word_guesses_left = 2  # ορίζουμε πόσες φορές μπορεί να μαντέψει ολόκληρη την λέξη ο παίκτης
        self.words_guessed = set()  # σύνολο που μετράει πόσες φορές έχει μαντέψει ολόκληρη την λέξη ο παίκτης
    
    def display_word(self):
        display = ''
        if self.word not in self.words_guessed:
            for letter in self.word:
                if letter in self.guessed_letters:
                    display += letter + ' '  # εμφάνιση γραμμάτων που έχει μαντέψει σωστά ο χρήστης
                else:
                    display += '_ '  # εμφάνιση κενών για γράμματα που δεν έχει μαντέψει ο χρήστης
        else:
            display = self.word
        return display
   
    def make_guess(self, guess):  # ο παίκτης μαντεύει ένα γράμμα κάθε φορά
        guess = guess.lower()
        if guess.isalpha() and len(guess) == 1:
            if guess in self.guessed_letters:
                print("You already guessed that letter.")  # έλεγχος εάν ο χρήστης έχει μαντέψει ήδη το γράμμα
            elif guess in self.word:
                print("Good guess!")  # έλεγχος εάν το γράμμα είναι στη λέξη
            else:
                print("Wrong guess!")
                self.guesses_left -= 1  # μείωση των εναπομεινάντων προσπαθειών
            self.guessed_letters.add(guess)
        else:
            print("Invalid input. Please enter a single letter.")  # Εμφάνιση μηνύματος λάθους για μη έγκυρη εισαγωγή
    
    def make_word_guess(self, guess):  # ο παίκτης μαντεύει ολόκληρη τη λέξη
        guess = guess.lower()
        if guess in self.words_guessed:
            print("You already guessed that word.")  # έλεγχος εάν ο χρήστης έχει μαντέψει ήδη τη λέξη
        elif guess == self.word:
            print("Good guess!.")  # έλεγχος εάν είναι η σωστή λέξη
        elif guess != self.word:
            print("Wrong guess!")
            self.word_guesses_left -= 1  # μείωση των εναπομεινάντων προσπαθειών
        self.words_guessed.add(guess)
   
    def check_game_status(self):
        if '_' not in self.display_word():
            print("Congratulations! You guessed the word:", self.word)
            return True  # επιστροφή True αν ολοκληρώθηκε επιτυχώς το παιχνίδι
        elif self.guesses_left == 0 or self.word_guesses_left == 0:
            print("Sorry, you ran out of guesses. The word was:", self.word)
            return True  # επιστροφή True αν εξαντλήθηκαν οι επιτρεπόμενες προσπάθειες
        else:
            print("Word: ", self.display_word())
            time.sleep(.6)
            print("Guesses left:", self.guesses_left)
            time.sleep(.6)
            print("Whole word guesses left:", self.word_guesses_left)
            return False  # επιστροφή False αν το παιχνίδι δεν έχει ολοκληρωθεί

def play_hangman():
    time.sleep(.6)
    player1 = input("Hello Player 1! Enter your name: ")
    time.sleep(.6)
    player2 = input("Hello Player 2! Enter your name: ")
    time.sleep(.8)
    word_to_guess = input(
        f"Let the game begin! {player1.capitalize()}, enter a word for {player2.capitalize()} to guess: ")

    game = HangmanGame(word_to_guess)

    while not game.check_game_status():  # όσο το παιχνίδι ΔΕΝ έχει ολοκληρωθεί
        time.sleep(1)
        whole_word = input(f"{player2.capitalize()} do you want to guess the whole word? (yes/no): ")
        while whole_word.lower() != 'yes' and whole_word.lower() != 'no':
            print("Please type yes or no")
            whole_word = input("Do you want to guess the whole word? (yes/no): ")
        if whole_word == 'yes':
            time.sleep(.7)
            guess = input(f"{player2.capitalize()} enter the whole word: ")
            game.make_word_guess(guess)  # την καλούμε για να επεξεργαστεί την μαντεψιά του παίκτη
        elif whole_word == 'no':
            time.sleep(.6)
            guess = input(f"{player2.capitalize()} enter a letter: ")
            game.make_guess(guess)  # την καλούμε για να επεξεργαστεί την μαντεψιά του παίκτη

    play_again = input("Do you want to play again? (yes/no): ")  # ερώτηση εάν ο παίκτης θέλει να παίξει ξανά
    while play_again.lower() != 'yes' and play_again.lower() != 'no':
        print("Please type yes or no")
        play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        print("Thanks for choosing to play again!")
        play_hangman()
    else:
        print("Thanks for playing!")

play_hangman()