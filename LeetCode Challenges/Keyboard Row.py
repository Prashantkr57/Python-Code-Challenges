words = ["Hello", "Alaska", "Dad", "Peace"]
output_list = []

first_row = "qwertyuiop"
second_row = "asdfghjkl"
third_row = "zxcvbnm"


def find_row(s):
    if s[0].lower() in first_row:
        return first_row
    elif s[0].lower() in second_row:
        return second_row
    elif s[0].lower() in third_row:
        return third_row
    else:
        return "Not Found"


def is_present(word_com, row):
    loop = True
    present = True
    while present:
        for c in word_com:
            if c in row:
                continue
            else:
                present = False
                break
        present = False

    return present


for word in words:
    lower_word = word.lower()
    print(is_present(lower_word, second_row))



