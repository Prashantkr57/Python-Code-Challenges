s = "MMMCDXC"
my_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


rev_s = s[::-1]
my_list = []

for item in rev_s:
    my_list.append(item)

int_no = my_dict[my_list[0]]

for i in range(len(my_list)-1):
    if my_dict[my_list[i]] >= my_dict[my_list[i + 1]]:
        int_no += my_dict[my_list[i]]
        
print(int_no)   
    









"""list_of_roman = []

for i in s:
    list_of_roman.append(i)

for i in range(0, len(list_of_roman)):
    if list_of_roman[i] == "I":
        if (len(list_of_roman) - i) > 1:
            if list_of_roman[i+1] == "V":
                our_no += 4
                print("executed IV")

            elif list_of_roman[i+1] == "X":
                our_no += 9
                print("executed IX")

            else:
                our_no += 1
                print("executed I")
        else:
            our_no += 1
            print("executed only I")

    elif list_of_roman[i] == "X" and list_of_roman[i-1] != "I":
        if (len(list_of_roman) - i) > 0:
            if list_of_roman[i+1] == "L":
                our_no += 40
                print("executed XL")

            elif list_of_roman[i+1] == "C":
                our_no += 90
                print("executed XC")

            else:
                our_no += 10
                print("executed X")
        else:
            our_no += 10
            print("executed only X")

    elif list_of_roman[i] == "C" and list_of_roman[i-1] != "X":
        if (len(list_of_roman) - i) > 0:
            if list_of_roman[i+1] == "D":
                our_no += 400
                print("executed CD")

            elif list_of_roman[i+1] == "M":
                our_no += 900
                print("executed CM")

            else:
                our_no += 100
                print("executed C")
        else:
            our_no += 100
            print("executed Only C")

    elif list_of_roman[i] == "V" and list_of_roman[i-1] != "I":
        our_no += 5
        print("executed V")

    elif list_of_roman[i] == "L" and list_of_roman[i-1] != "X":
        our_no += 50
        print("executed L")

    elif list_of_roman[i] == "D" and list_of_roman[i-1] != "C":
        our_no += 500
        print("executed D")

    elif list_of_roman[i] == "M" and list_of_roman[i-1] != "C":
        our_no += 1000
        print("executed M")

# return our_no
print(our_no)"""
