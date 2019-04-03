# RenPy

<br>

[**Labels and Control Flow**](https://github.com/maim-lain/renpy/blob/master/notes/labels.md)

[**Dialog and Narration**](https://github.com/maim-lain/renpy/blob/master/notes/dialog.md)

[**Displaying Images**](https://github.com/maim-lain/renpy/blob/master/notes/images.md)

[**Python**](https://github.com/maim-lain/renpy/blob/master/notes/python.md)

[**Audio**](https://github.com/maim-lain/renpy/blob/master/notes/audio.md)

<br>
<br>
<br>

## Useful RenPy Stuff

<br>

#### Imagebutton Animation
```renpy
imagebutton pos (332, 1251) idle "btn_idle.png" hover Transform("btn_play", easein=0.4, zoom=1.3) action Start()
```

<br>

#### Screen Transition
```renpy
action Show("screen", fade)
```

<br>

#### Pop-up Notification
```renpy
$ renpy.notify("This will create a pop-up notification.")
```




<br>
<br>
<br>

https://www.renpy.org/doc/html/#customizing-ren-py

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
# in screens.rpy find and change to:

default quick_menu = False
```

#### Text color and cool text outline
```renpy
define gui.text_color = '#ffffff'
define gui.dialogue_text_outlines = [ (0, "#000000", 2, 2) ]
```
- artstation animations
