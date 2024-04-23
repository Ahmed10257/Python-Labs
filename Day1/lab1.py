
# Reverse the first name and last name
def reverse_name(first_name, last_name):
    f_name=first_name[::-1]
    l_name=last_name[::-1]
    return (l_name + " " + f_name)
Name=reverse_name("Ahmed", "Mansour")
print(Name)
#------------------------------------------------
# Calculating value of n
def calculate_n(n):
    nn=int(str(n)*2)
    nnn=int(str(n)*3)
    return (n+nn+nnn)
result=calculate_n(5)
print(result)
#------------------------------------------------
def print_string():
    print("""a string that you "don't" have to escape""")
    print("This \nis a ....... multi-line\n\
           \heredoc string --------> example")
print_string()
#------------------------------------------------
def sphere_volume(r):
    return (4/3*3.14159*r**3)
volume=sphere_volume(5)
print(volume," cm^3")
#------------------------------------------------
def triangle_area(base, height):
    return (0.5*base*height)
area=triangle_area(5, 6)
print(area," cm^2")
#------------------------------------------------
def print_pattern():
    for i in range(1, 6):
        print("*"*i)
        if i==5:
            for j in range(4, 0, -1):
                print("*"*j)
print_pattern()
#------------------------------------------------
def reverse_word(word):
    return word[::-1]
reversed_word=reverse_word("Hello")
print(reversed_word)
#------------------------------------------------
def print_numbers():
    for i in range(0, 6):
        if i==3 or i==6:
            continue
        print(i)
print_numbers()
#------------------------------------------------
def fibonacci(start,end):
    a, b = 0, 1
    for i in range(start, end):
        print(a)
        a, b = b, a+b
fibonacci(0, 50)
#------------------------------------------------
def digits_and_letters(string):
    digits=0
    letters=0
    for i in string:
        if i.isdigit():
            digits+=1
        elif i.isalpha():
            letters+=1
    return (letters, digits)
letters, digits=digits_and_letters("Python 3.2")
print("Letters: ", letters)
print("Digits: ", digits)
#------------------------------------------------