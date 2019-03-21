import random
import null as null


def Problem1():
    list1 = []
    list2 = []

    for x in range(20):
        list1.append(random.randint(0, 101))

    for x in range(20):
        list2.append(round(random.uniform(10.0, 80.0), 3))

    print(list1)
    print(list2)


def makeTerm(expression):
    a = ""
    b = ""
    x = 0
    term = ""

    while expression[x] != ' ':
        a += expression[x]
        x += 1

    x += 1
    while expression[x] != null:
        b += expression[x]
        x += 1
        if x >= len(expression):
            break

    for x in a:
        if x != '-':
            temp = "+"
            temp += a
            a = temp
            break
        else:
            break

    if b == '0':
        for x in a:
            if x != '-':
                return "+1 "
            else:
                return "-1 "

    elif b == '1':
        return a + "x "

    term += a + "x^" + b + " "

    return term


def solve(statement):
    solution = ""
    for x in range(len(statement)):
        expression = []
        if statement[x] == '(':
            x += 1
            while statement[x] != ")":
                expression.append(statement[x])
                x += 1
            term = makeTerm(expression)
            solution += term
        # elif statement[x] == ' ':
        # x += 1
    return solution


def Problem2():
    test1 = "NIL"
    test2 = "((2 1) (1 0))"
    test3 = "((3 2) (-1 0))"
    test4 = "((5 2) (-4 1) (1 0))"
    test5 = "((7 14) (11 13) (-3 2) (7 1) (-5 0))"
    test6 = "((1 0) (2 1) (-5 3) (-3 1) (7 0))"

    testCases = [test1, test2, test3, test4, test5, test6]

    for x in range(6):
        test = testCases[x]

        if test == "NIL":
            print("0")
            continue

        temp = []
        statement = []

        for c in test:
            temp.append(c)

        for x in range(1, len(temp) - 1):
            statement.append(temp[x])

        solution = solve(statement)

        print(solution)


print("Problem 1 Solution: ")
Problem1()

print()
print("Problem 2 Solution: ")
Problem2()

#Problem 1 Solution:
#[51, 43, 46, 29, 80, 27, 92, 29, 30, 70, 7, 40, 0, 68, 38, 75, 16, 66, 1, 46]
#[16.974, 68.492, 75.825, 75.6, 33.048, 55.459, 16.256, 40.839, 62.691, 53.667, 25.092, 68.703, 18.54, 46.231, 49.087, 23.571, 67.671, 67.908, 55.267, 30.411]

#Problem 2 Solution:
#0
#+2x +1
#+3x^2 -1
#+5x^2 -4x +1
#+7x^14 +11x^13 -3x^2 +7x -1
#+1 +2x -5x^3 -3x +1