"""
-------------------------------Funny Names------------------------------------
Its result day at school and not everyone is happy. You decided to make your friends laugh by jumbling their names to come up with some funny names.
Your program should take the number of names and the names separated by space as input. Output should be funny names in the same order.

Input:
Enter number of friends:
3
Enter the name of your 3 friends:
Rohan Das
Shubham Agarwal
Ritesh Arora

Output:
Ritesh Das
Shubham Arora
Rohan Agarwal
"""
import random
def swapping_name(first_name, last_name, no_name):
    for i in range(0, no_name):
        joint_name = first_name[i] + " " + last_name[random.randint(0, no_name - 1)]
        print(f"Name-{i}-{joint_name}")

if __name__ == "__main__":
    no_name = int(input("Enter a number of name:-"))
    list_name = []
    first_name = []
    last_name = []
    for i in range(1, no_name + 1):
        name_collect = input("Enter a name :-")
        list_name.append(name_collect)
        # print(list_name)
    for i in (list_name):
        word = i.split(" ")
        first_name.append(word[0])
        last_name.append(word[1])
    # print(first_name)
    # print(last_name)
    swapping_name(first_name, last_name, no_name)