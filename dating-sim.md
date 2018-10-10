# Ren'Py Dating Sim

<br>

## The Wrong Way
There's an easy way, and a hard way to code a 'dating sim' style game in Ren'Py. Almost every game that I've seen does it the hard way, so I'm going to explain how to do it properly. But first, let's look at the wrong way to code a game:
```renpy
# Do NOT code your game like this.

default alice_level = 1
default alice_location = "room"
default alice_current_event = "a_event_1"

label alice_level_up:
    if alice_level <= 5:
        $ alice_level += 1
    if alice_current_event == "a_event_1":
        $ alice_current_event = "a_event_2"
    elif alice_current_event == "a_event_2":
        $ alice_current_event = "a_event_3"
    elif alice_current_event == "a_event_3":
        $ alice_current_event = "a_event_4"

default heather_level = 1
default heather_location = "room"
default heather_current_event = "h_event_1"

label heather_level_up:
    if heather_level <= 5:
        $ heather_level += 1
    if heather_current_event == "h_event_1":
        $ heather_current_event = "h_event_2"
    elif heather_current_event == "h_event_2":
        $ heather_current_event = "h_event_3"
    elif heather_current_event == "h_event_3":
        $ heather_current_event = "h_event_4"

default rebecca_level = 1
default rebecca_location = "room"
default rebecca_current_event = "r_event_1"

label rebecca_level_up:
    if rebecca_level <= 5:
        $ rebecca_level += 1
    if rebecca_current_event == "r_event_1":
        $ rebecca_current_event = "r_event_2"
    elif rebecca_current_event == "r_event_2":
        $ rebecca_current_event = "r_event_3"
    elif rebecca_current_event == "r_event_3":
        $ rebecca_current_event = "r_event_4"
```

<br>

It's a lot of lines, there's lots of repeated code, and making simple changes would be a lot of work. All of these are bad things. Now here's how we'll be initializing all 3 of those girls and all their stats instead, and in only 3 lines of code:
```renpy
default alice = Girl("Alice", a_events)
default heather = Girl("Heather", h_events)
default rebecca = Girl("Rebecca", r_events)
```

<br>
<br>
<br>

## The Right Way
The way that this is done is by creating a Girl class that will contain all the stats and logic for a girl character. By using a class we will only need to write everything once instead of rewriting/copy-pasting all the code for every single character.
```python
class Girl():
    def __init__(self):
        # Constructor

    # This is the empty Girl class.
    # All a girl's stats and info will go here.
```

<br>

In the constructor you will want to add all the fields that make up the information about a girl. For example: her relationship level, location (if it's an open world game), the relationship event that will occur when you interact with her, etc. In this example the only arguments that will need to be passed when creating a Girl object is 'name' and 'event_list'.
```renpy
def __init__(self, name, event_list):
    self.name = name
    self.level = 1
    self.location = "room"
    self.event_list = event_list
    self.current_event = event_list[1]
```

<br>

Next you'll want to add a method to the class that will level up a girl and set her next event, instead of creating verbose level_up labels for each girl.
```renpy
def level_up(self):
    if self.level <= 5:
        self.level += 1
    self.current_event = self.event_list[self.level]
```

<br>
<br>

The completed Girl class should look like this:
```renpy
init python:
    class Girl():
        def __init__(self, name, event_list):
            self.name = name
            self.level = 1
            self.location = "room"
            self.event_list = event_list
            self.current_event = event_list[1]

        def level_up(self):
            if self.level <= 5:
                self.level += 1
            self.current_event = self.event_list[self.level]
```

<br>
<br>

Instantiating the girls is now super simple and only requires their name and a list of their relationship event label names.
```renpy
default a_events = ["null", "a_event_1", "a_event_2", "a_event_3"]
default h_events = ["null", "h_event_1", "h_event_2", "h_event_3"]
default r_events = ["null", "r_event_1", "r_event_2", "r_event_3"]

default alice = Girl("Alice", a_events)
default heather = Girl("Heather", h_events)
default rebecca = Girl("Rebecca", r_events)
```

<br>

The code for the game is now simple, short, and everything about a character can be accessed directly from her object instead of a dozen different variables and labels.

<br>
<br>
<br>

## Example Game
Finally here's an example of how you would use a girl's fields and methods in a game.
```renpy
label start:
    jump heathers_room


label heathers_room:
    "You enter [heather.name]'s room. Her relationship level is [heather.level]."

    if heather.location == "room":
        menu:
            "Would you like to hang out with Heather?"
            "Yes":
                jump expression heather.current_event
            "No":
                return
    else:
        "Me" "Looks like no one is here. Heather must be at [heather.location]."
        return


label h_event_1:
    "You introduce yourself to Heather."
    $ heather.level_up()
    jump heathers_room

label h_event_2:
    "Heather" "Nice to meet you again. I have to go to work now though."
    $ heather.level_up()
    $ heather.location = "work"
    jump heathers_room
```
