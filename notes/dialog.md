# Dialog and Narration

<br>

- { } is for a text tag
- \[ \] is for variable substitution

<br>
<br>

## Define a Character
```renpy
define e = Character("Ellen", color="#c8c8ff", image="ellen")
define p = Character("[player_name]")
```

<br>
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
<br>

## Special Characters
- nvl
 - A kind of Character that causes dialogue to be displayed in NVL-Mode, with multiple lines of text on the screen at once.
- centered
  - A character that causes what it says to be displayed centered, in the middle of the screen, outside of any window.
- extend
  - A character that causes the last character to speak to say a line of dialogue consisting of the last line of dialogue spoken and the dialogue given to extend. This can be used to have the screen change over the course of dialogue.

For example:
```renpy
# Show the first line of dialogue, wait for a click, change expression, and show the rest.

e concerned "Sometimes, I feel sad."
show eileen happy
extend " But I usually quickly get over it!"
```

<br>
<br>

## Monologue Mode
To cover these cases, Ren'Py supports monologue mode. When dialogue is inside triple-quoted strings, Ren'Py will break the dialogue up into blocks at blank lines. Each block is then used to create its own say statement. If you'd like to omit the spaces between the blocks, write rpy monologue single at the top level of the file, before the first monologue line.
```renpy
# global scope
rpy monologue single

"""
This is the first line of dialogue.
This is the second line of dialogue.
This is the third line of dialogue.
"""
```
