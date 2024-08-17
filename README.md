# Typing-Speed-Calculator-in-Python
## Code

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





  ##Output

  ![Screenshot 2024-08-17 223342](https://github.com/user-attachments/assets/a1717f46-d36f-4de2-8c9e-ed627fce7b8a)



    
### 1. **Self-Improvement and Skill Development**
   - **Practice and Improvement**: Regularly using a typing speed calculator helps individuals improve their typing speed and accuracy, which is essential for students, professionals, and anyone who frequently uses a computer.
   - **Tracking Progress**: Users can track their progress over time, setting goals to increase their words per minute (WPM) and reduce errors.

### 2. **Job Preparation and Career Development**
   - **Job Requirements**: Many jobs, especially those in data entry, transcription, customer support, and administrative roles, require a certain typing speed. Practicing with a typing speed calculator can help candidates meet or exceed these requirements.
   - **Certification and Testing**: Some jobs require a typing test as part of the application process. A typing speed calculator can be used to prepare for these tests, ensuring that candidates meet the necessary standards.

### 3. **Education and Learning**
   - **Teaching Typing Skills**: In schools and educational programs, typing speed calculators are used to teach and assess typing skills. Students can use these tools to practice and improve their typing as part of their curriculum.
   - **Online Learning**: With the rise of online education, students and teachers alike benefit from good typing skills. Faster typing enables more efficient communication and note-taking during online classes.

### 4. **Productivity in the Workplace**
   - **Efficiency in Tasks**: Faster typing translates to increased productivity in tasks like writing emails, creating reports, and entering data. A typing speed calculator helps employees assess and enhance their typing efficiency.
   - **Time Management**: By improving typing speed, individuals can complete tasks more quickly, leaving more time for other important activities.

These applications highlight the importance of typing speed in various aspects of everyday life, making the use of a typing speed calculator a valuable tool for personal and professional development.
