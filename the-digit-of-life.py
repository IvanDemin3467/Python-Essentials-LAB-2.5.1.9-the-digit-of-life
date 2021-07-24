#This is the Python Essentials 2 LAB 2.5.1.9 The digit of life


def user_input():
    # This function prompts the user and validates the input
    # It returns a string of digits
    # It checks user input for numeric characters without spaces
    # Exactly 8 digits required
    while True:
        text = input("Enter your birth date in format DDMMYYYY: ")
        if not text.isdigit():        # only digits are allowed
            print("Invalid input. Only digits are allowed.")
        elif len(text) != 8:          # blank lines are not allowed
            print("Invalid input. Exactly 8 digits required.")
        else:
            break
    return text


def digit_of_life(text):
    # This function calculates The digit of life
    # Input is string of 8 digits without any other symbols
    # Output is integer, that represents The digit of life
    if not text.isdigit() or len(text) != 8: # check for incorrect input
        return -1                            # return -1 on every incorrect input
    while True:                              # working in endless cycle
        the_digit = 0                        # prepare variable to sum digits
        for char in text:                    # iterate over the digits in birth date
            the_digit += int(char)           # and susum them up
        text = str(the_digit)                # preparing next iteration of summation
        if len(text) == 1:                   # if we got single-digit result
            return the_digit                 # job is done -> return result
        else: continue                       # else do the next iteration
    

def tests():
    # typical function that tries test cases
    print("Self-test ...")
    test_texts = ("19991229",
                  "20000101",
                  "2021",       # too short
                  "123456789",  # too long
                  "abc")        # digits required
    test_results = (6,
                    4,
                    -1,
                    -1,
                    -1)
    for i in range(len(test_texts)):
        txt = test_texts[i]
        result = digit_of_life(txt)
        print(txt, "->", result, end=" ")
        if result == test_results[i]:
                print("OK")
        else:
                print("Failed")


# Main
if __name__ == "__main__":
    text = user_input()
    print(digit_of_life(text))

##tests() # uncomment to perform self-test
