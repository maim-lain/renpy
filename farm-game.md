# Animal farm gameplay mechanics

<br>

In the main way you earn gold in Four Elements Trainer - Book 2 is by managing an 'animal farm' and breeding cows. I'll be explaining how I coded this gameplay mechanic that allows you to buy and breed animals.

<br>
<br>

#### The cow class:
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

#### Buying cows:
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

#### Checking a cow's type:
When a player tries to breed cows we need to make sure that the player has the type of cow they want to breed first. This function will return a bool that will be used to determine if the player owns a type of cow.
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

<br>
<br>

#### Breeding a cow:
Now we use the method from the Cow class to set a cow's pregnant field to true.
```renpy
def breed_cow(type):
    global cow_list
    if type == 'fresh':
        for num in range(0, len(cow_list)):
            if cow_list[num].has_been_pregnant == False:
                cow_list[num].breed()
                return
    if type == 'used':
        for num in range(0, len(cow_list)):
            if cow_list[num].has_been_pregnant == True and cow_list[num].is_pregnant == False:
                cow_list[num].breed()
                return
```

<br>
<br>

#### Giving birth:
At the end of every day if a cow is pregnant the amount of days it has been pregnant will increase. If a cow has been pregnant for a certain amount of days it then gives birth and is no longer pregnant and can be bred again.
```renpy
def end_day_cows():
    global cow_list
    global baby_cows

    for num in range(0, len(cow_list)):
        if cow_list[num].is_pregnant:
            cow_list[num].days_pregnant += 1

            if cow_list[num].days_pregnant >= 3:
                baby_cows += 1
                cow_list[num].is_pregnant = False
                cow_list[num].days_pregnant = 0
    return
```

<br>
<br>

#### Buying and breeding menus:
Here are the menus the player will use to select what type of cow they want to buy and which type of cow they want to breed.
```renpy
label buy_cows:
    menu:
        'Buy fresh cow':
            $ add_cow('fresh')
        'Buy used cow':
            $ add_cow('used')
        'Buy pregnant cow':
            $ add_cow('pregnant')
    return

label breed_cows:
    $ have_fresh = check_for_cow_type('fresh')
    $ have_used = check_for_cow_type('used')

    if have_fresh or have_used:
        menu:
            'Breed fresh cow' if have_fresh:
                $ breed_cow('fresh')
            'Breed used cow' if have_used:
                $ breed_cow('used')
    else:
        'You have no cows to breed.'
    return
```

<br>
<br>

#### Starting the game:
Finally the last thing to do is initialize our variables and create a way for the player to interact with the farm.
```renpy
default cow_list = []
default baby_cows = 0


label start:
    jump main_loop

label main_loop:
    call buy_cows
    call breed_cows
    $ end_day_cows()
    $ num_cows = len(cow_list)

    'You have [num_cows] cows and [baby_cows] babies.'

    if cow_list[0].is_pregnant:
        'Your 1st cow is pregnant. It has been pregnant for [cow_list[0].days_pregnant] days.'
    else:
        'Your 1st cow is not pregnant.'

    jump main_loop
```

<br>
<br>
<br>
<br>

## Full game example:
Here is the code for the full game:
```renpy
init python:
    class Cow():
        def __init__(self, has_been, is_preg):
            self.has_been_pregnant = has_been
            self.is_pregnant = is_preg
            self.days_pregnant = 0

        def breed(self):
            self.has_been_pregnant = True
            self.is_pregnant = True


    def add_cow(type):
        global cow_list
        if type == 'fresh':
            cow_list.append(Cow(False, False))
        if type == 'used':
            cow_list.append(Cow(True, False))
        if type == 'pregnant':
            cow_list.append(Cow(True, True))
        return

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

    def breed_cow(type):
        global cow_list
        if type == 'fresh':
            for num in range(0, len(cow_list)):
                if cow_list[num].has_been_pregnant == False:
                    cow_list[num].breed()
                    return
        if type == 'used':
            for num in range(0, len(cow_list)):
                if cow_list[num].has_been_pregnant == True and cow_list[num].is_pregnant == False:
                    cow_list[num].breed()
                    return

    def end_day_cows():
        global cow_list
        global baby_cows

        for num in range(0, len(cow_list)):
            if cow_list[num].is_pregnant:
                cow_list[num].days_pregnant += 1

                if cow_list[num].days_pregnant >= 3:
                    baby_cows += 1
                    cow_list[num].is_pregnant = False
                    cow_list[num].days_pregnant = 0
        return


label buy_cows:
    menu:
        'Buy fresh cow':
            $ add_cow('fresh')
        'Buy used cow':
            $ add_cow('used')
        'Buy pregnant cow':
            $ add_cow('pregnant')
    return

label breed_cows:
    $ have_fresh = check_for_cow_type('fresh')
    $ have_used = check_for_cow_type('used')

    if have_fresh or have_used:
        menu:
            'Breed fresh cow' if have_fresh:
                $ breed_cow('fresh')
            'Breed used cow' if have_used:
                $ breed_cow('used')
    else:
        'You have no cows to breed.'
    return


default cow_list = []
default baby_cows = 0


label start:
    jump main_loop

label main_loop:
    call buy_cows
    call breed_cows
    $ end_day_cows()
    $ num_cows = len(cow_list)

    'You have [num_cows] cows and [baby_cows] babies.'

    if cow_list[0].is_pregnant:
        'Your 1st cow is pregnant. It has been pregnant for [cow_list[0].days_pregnant] days.'
    else:
        'Your 1st cow is not pregnant.'

    jump main_loop
```
