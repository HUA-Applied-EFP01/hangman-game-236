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

