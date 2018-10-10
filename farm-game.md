# Animal farm gameplay mechanics

<br>

In the main way you earn gold in Four Elements Trainer - Book 2 is by managing an 'animal farm' and breeding cows. I'll be explaining how I coded this gameplay mechanic that allows you to buy and breed animals.

<br>
<br>

First I created a class that represents the cows that keeps track of whether they are pregnant and how long they've been pregnant.
```renpy
class Cow():
    def __init__(self, has_been, is_preg):
        self.has_been_pregnant = has_been
        self.is_pregnant = is_preg
        self.days_pregnant = 0

    def breed(self):
        self.has_been_pregnant = True
        self.is_pregnant = True
```

<br>
<br>

Next is the function that allows you to buy cows and sets the type of cow.
```renpy
def add_cow(type):
    global cow_list
    if type == 'fresh':
        cow_list.append(Cow(False, False))
    if type == 'used':
        cow_list.append(Cow(True, False))
    if type == 'pregnant':
        cow_list.append(Cow(True, True))
    return
```

<br>
<br>

When a player tries to breed cows we need to make sure that the player has the type of cow they want to breed first. This function will return a bool to determine if the player owns a type of cow.
```renpy
def check_for_cow_type(type):
    global cow_list
    if type == 'fresh':
        for num in range(0, len(cow_list)):
            if cow_list[num].has_been_pregnant == False:
                return True
        return False
    if type == 'used':
        for num in range(0, len(cow_list)):
            if cow_list[num].has_been_pregnant == True and cow_list[num].is_pregnant == False:
                return True
        return False
    if type == 'pregnant':
        for num in range(0, len(cow_list)):
            if cow_list[num].is_pregnant:
                return True
        return False
```
