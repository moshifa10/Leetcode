

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties



phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)


def most_money(students):
    # NOTE: the Student class is preloaded
    if len(students) == 1:
        return students[0].name
    winner_name = []
    total = 0


    for i in students:
        calc = i.fives*5 + i.tens*10 + i.twenties*20
        
        if calc > total and len(winner_name) >0:
            total = calc
            winner_name = []
            winner_name.append(i.name)
        elif calc > total and len(winner_name) == 0:
            total = calc
            # winner_name = []
            winner_name.append(i.name)
        elif calc == total:
            winner_name.append(i.name)

    if len(winner_name) == 1:
        return winner_name[0]
    
    elif len(winner_name) == len(students):
        return "all"
    else:
        return winner_name
# most_money([cam, geoff, phil]), "Phil"
# test.assert_equals(most_money([cam, geoff, phil]), "Phil")
# test.assert_equals(most_money([cam, geoff]), "all")
# test.assert_equals(most_money([geoff]), "Geoff")

print(most_money([cam, geoff, phil]))
print(most_money([cam, geoff]))
print(most_money([geoff]))