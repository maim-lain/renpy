# Dialog and Narration

<br>

## Define a Character
```renpy
define e = Character("Ellen", color="#c8c8ff", image="ellen")
define p = Character("[player_name]")
```

<br>

## Say with Image Attributes
When a character is defined with an associated image tag, the say statement involving that character may have image attributes placed between the character name and the second string.
```renpy
label start:
    e mad "I'm a little upset at you."
    e happy "But it's just a passing thing."
```
is equivalent to:
```renpy
label start:
    show eileen mad
    e "I'm a little upset at you."
    show eileen happy
    e "But it's just a passing thing."
```

<br>




The { character begins a text tag, and the [ character begins a substitution.

