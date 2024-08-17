import time

def calculate_wpm(time_taken, word_count):

    minutes = time_taken / 60
    wpm = word_count / minutes
    return round(wpm, 2)

def calculate_accuracy(typed_words, original_words):

    correct_words = sum(1 for typed, original in zip(typed_words, original_words) if typed == original)
    accuracy = (correct_words / len(original_words)) * 100
    return round(accuracy, 2)

def typing_speed_test():

    prompt = "The quick brown fox jumps over the lazy dog"
    print("Type the following sentence as quickly and accurately as you can:")
    print(prompt)
    print()

    input("Press Enter when you're ready to start...")
    
    start_time = time.time()
    user_input = input("Start typing here: ")
    end_time = time.time()

    time_taken = end_time - start_time
    typed_words = user_input.split()
    original_words = prompt.split()

    word_count = len(typed_words)
    wpm = calculate_wpm(time_taken, word_count)
    accuracy = calculate_accuracy(typed_words, original_words)

    print(f"\nTime Taken: {round(time_taken, 2)} seconds")
    print(f"Words Per Minute (WPM): {wpm}")
    print(f"Accuracy: {accuracy}%")

    if accuracy == 100 and wpm >= 60:
        print("Excellent typing speed and accuracy!")
    elif accuracy >= 90 and wpm >= 40:
        print("Good typing speed and accuracy!")
    else:
        print("Keep practicing to improve your speed and accuracy!")

if __name__ == "__main__":
  
    typing_speed_test()