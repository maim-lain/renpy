# Ren'Py Dating Sim

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

Now here's how to do the exact same thing in only 3 lines of code:
```renpy
default alice = Girl("Alice", a_events)
default heather = Girl("Heather", h_events)
default rebecca = Girl("Rebecca", r_events)
```

<br>

The way this is done is by creating a Girl class that will contain all the stats and logic, and we will only need to write everything once instead of rewriting everything for **every.single.character.**

<br>

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
