# Dialog and Narration


## Define a Character
```renpy
define e = Character('Ellen', color="#c8c8ff", image="ellen")
```

<br>

## Say with Image Attributes
When a character is defined with an associated image tag, say statement involving that character may have image attributes placed between the character name and the second string.

In this form, if an image with the given tag is showing, Ren'Py will issue a show command involving the character tag and the attributes.
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

