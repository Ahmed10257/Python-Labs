# Elliminating similar adjacent numbers
def eliminate_adjacent(numbers):
    return list(set(numbers))
numbers=[1, 2, 2, 3, 4, 4, 5]
result=eliminate_adjacent(numbers)
print(result)
#------------------------------------------------
# Spliting two strings and joining them
def split_join(string1, string2):
    string1_len=len(string1)
    string2_len=len(string2)

    if string1_len%2==0:
        string1_left_half=string1[:string1_len//2]
        string1_right_half=string1[string1_len//2:]
    else:
        string1_left_half=string1[:string1_len//2+1]
        string1_right_half=string1[string1_len//2+1:]

    if string2_len%2==0:
        string2_lefthalf=string2[:string2_len//2]
        string2_righthalf=string2[string2_len//2:]
    else:
        string2_lefthalf=string2[:string2_len//2+1]
        string2_righthalf=string2[string2_len//2+1:]

    print(string1_left_half+" "+string2_lefthalf)
    print(string1_right_half+" "+string2_righthalf)

split_join("Ahmed", "Mansour")
#------------------------------------------------
# Checking if the sequnce is unique
def unique_sequence(sequence):
    seq_len=len(sequence)
    cond=None
    for i in range(seq_len-1):
        if sequence[i]==sequence[i+1]:
            cond="False"
    cond= "True"
    return cond

sequence=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result=unique_sequence(sequence)
print(result)
#------------------------------------------------
# Bubble sorting unordered list
def bubble_sort(numbers):
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-1):
            if numbers[j]>numbers[j+1]:
                numbers[j], numbers[j+1]=numbers[j+1], numbers[j]
    return numbers

numbers=[64, 34, 25, 12, 22, 11, 90]
result=bubble_sort(numbers)
print(result)
#------------------------------------------------
# Guessing the number
def guess_number():
    input("Please think of a number between 0 and 100: ")
    low=0
    high=100
    guess=50
    trial=0
    while True:
        print("Is your secret number ", guess, "?")
        response=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        if response=="h":
            high=guess
            guess=(low+high)//2
            trial+=1
        elif response=="l":
            low=guess
            guess=(low+high)//2
            trial+=1
        elif response=="c":
            print("Game over. Your secret number was: ", guess)
            break
        elif trial==10:
            print("Sorry, reached maximum number of trials. Game over.")
            break
        else:
            print("Sorry, I did not understand your input.")

guess_number()
#------------------------------------------------
# Bonus Problem
def diagonalDifference(arr):
    arr_length = len(arr)
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    for i in range(arr_length):
        primary_diagonal_sum += arr[i][i]
        secondary_diagonal_sum += arr[i][arr_length - i - 1]
    print(primary_diagonal_sum)
    print(secondary_diagonal_sum)    
    return abs(primary_diagonal_sum - secondary_diagonal_sum)

arr = [[7, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonalDifference(arr))