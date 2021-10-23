def task1():
    a = 450
    b = 450
    if b > a:
        print("B is large")

    elif a > b:
        print("A is large")

    elif a==b:
        print("They are equal")

    else:
        print("Invalid")


def task2():
    a = 100
    b = 56
    c = 100
    if a > b and a > c:
        print("A is largest")

    elif b > a and b > c:
        print("B is largest")

    elif c > a and c > b:
        print("C is largest")

    elif a == b and b == c:
        print("They are same")

    else:
        print("ANy two two are same")


def task3():
    a = 10
    if a > 14 and a < 19:
        print("You should be in Highschool")
    elif a <= 14:
        print("You should be in primmary sch")
    else:
        print("You should be in college.. ")

def task4():
    weight = 55
    age = 80
    if age > 14:
        print("You are eligible to donate")
        if weight >50:
            print("You can donate")
            if age  > 70:
                print("Warning!. You need doctor advise")

        else:
            print("You cannot donate - less weight")
    else:
        print("You are no eligible")

# loops here
def task5():
    for i in range(0, 5):
        radius = float(input("Enter radius"))
        area = 3.14 * radius ** 2
        print(area)

task5()





























