'''
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
Each of 5 dice can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
'''


def score(dice):
    points = {
        "111": 1000,
        "666": 600,
        "555": 500,
        "444": 400,
        "333": 300,
        "222": 200,
        "1": 100,
        "5": 50
    }
    # user_points = 0
    check = set()
    check1 = []
    y = None
    for i in dice:
        x = dice.count(i)
        # z = str(i) * x
        if x > 3:
            y = ((x - 3), i)
            check.add(str(i)*3)

            

        elif x == 2:
            check1.append(str(i))

        else:
            check.add(str(i)*x)

    if y != None:
        if y[0] == 2:
            check1.append(str(i))
            check1.append(str(i))
        else:
            check.add(str(y[-1])*y[0])

    turn = list(check)
    # print(turn)

    got = [points[i] for i in turn if i in points]
    got_list = [points[i] for i in check1 if i in points]
    got.extend(got_list)
    # print(sum(got))
    return sum(got)




# score( [5, 1, 3, 4, 1] ),  250
'''
        test.assert_equals( score( [1, 1, 1, 3, 1] ), 1100)
        test.assert_equals( score( [2, 3, 4, 6, 2] ),    0)
        test.assert_equals( score( [4, 4, 4, 3, 3] ),  400)
        test.assert_equals( score( [2, 4, 4, 5, 4] ),  450)
'''
# print(score([5, 1, 3, 4, 1]))
# print(score([1, 1, 1, 3, 1]))
# print(score([2, 3, 4, 6, 2]))
# print(score([4, 4, 4, 3, 3]))
# print(score([2, 4, 4, 5, 4]))
print(score([1, 1, 1, 1, 1]))