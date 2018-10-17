# RenPy
- artstation animations

<br>

[**Labels and Control Flow**](https://github.com/maim-lain/renpy/blob/master/notes/labels.md)

[**Dialog and Narration**](https://github.com/maim-lain/renpy/blob/master/notes/dialog.md)

[**Displaying Images**](https://github.com/maim-lain/renpy/blob/master/notes/images.md)

[**Python**](https://github.com/maim-lain/renpy/blob/master/notes/python.md)

<br>

#### Music
The play music statement takes a filename that is interpreted as an audio file to play. Audio files should be in opus, ogg vorbis, or mp3 format.
```renpy
    play music "illurock.ogg"
```
When changing music, one can supply a fadeout and a fadein clause, which are used to fade out the old music and fade in the new music.
```renpy
    play music "illurock.ogg" fadeout 1.0 fadein 1.0
```
The queue music statement plays an audio file after the current file finishes playing.
```renpy
    queue music "next_track.opus"
```
Music can be stopped with the stop music statement, which can also optionally take a fadeout clause.
```renpy
    stop music
```
Sound effects can be played with the play sound statement. Unlike music, sound effects do not loop.
```renpy
    play sound "effect.ogg"
```

<br>

#### Pause Statement
The pause statement causes Ren'Py to pause until the mouse is clicked. If a number is given, the pause will end when that number of seconds have elapsed.
```renpy
pause

pause 3.0
```

<br>

#### Supporting Flags using the Default, Python and If Statements
While some games can be made by only using the statements given above, other games requires data to be stored and recalled later. For example, it might make sense for a game to remember a choice a player has made, return to a common section of the script, and act on the choice later. This is one of the reasons why Ren'Py has embedded Python support.

To initialize a variable, use the default statement, before label start.
```renpy
default book = False

label book:
    $ book = True
    m "It's like an interactive book that you can read on a computer or a console."
    jump marry
```
Lines beginning with a dollar-sign are interpreted as Python statements. The assignment statement here assigns a value to a variable. Ren'Py has support for other ways of including Python, such as a multi-line Python statement, that are discussed in other sections of this manual.

#### Disable Quick Menu
```renpy
# in screens.rpy change find and change to:

default quick_menu = False
```
