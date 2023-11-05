def printthenums(numbers):
    print(','.join(numbers))
    print(numbers)
    mylist = []
    for i in numbers:
        mylist.append(int(i))
    print(sum(mylist))

UserInput = "123456"

printthenums(UserInput)
