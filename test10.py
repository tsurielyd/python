def printthenums(numbers):
    print(','.join(numbers))
    print(numbers)
    mylist = []
    for i in numbers:
        mylist.append(int(i))
    print(sum(mylist))

UserInput = input("enter 5 digits number:")

printthenums(UserInput)