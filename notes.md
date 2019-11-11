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

#### Performance
```renpy
config.predict_statements = 48
config.image_cache_size_mb = 512


$ renpy.free_memory()


$ renpy.start_predict("images/aut_mast_*.*") # Match files
$ renpy.start_predict("aut_mast_*") # Match declared images
$ renpy.stop_predict()
```

<br>

#### Build
```renpy
build.archive("audio", "all")
build.archive("images", "all")
build.archive("scripts", "all")
build.archive("videos", "all")


# default exclusions here
build.classify("game/**.rpy", None)


build.classify("game/audio/**", "audio")

build.classify("game/**.jpg", "images")
build.classify("game/**.png", "images")

build.classify("game/**.rpyc", "scripts")

build.classify("game/videos/**", "videos")
```

<br>

#### Properly use italics and bold font
```renpy
init python:
    config.font_replacement_map["fonts/DejaVuSans.ttf", False, True] = ("fonts/DejaVuSans-Italic.ttf", False, False)
    config.font_replacement_map["fonts/DejaVuSans.ttf", True, False] = ("fonts/DejaVuSans-Bold.ttf", False, False)
    config.font_replacement_map["fonts/DejaVuSans.ttf", True, True] = ("fonts/DejaVuSans-Bold-Italic.ttf", False, False)
```

<br>

#### Android detection
```renpy
# Always use this one, Works on emulator
renpy.variant("mobile"):


# Doesn't work on emulator
renpy.mobile:
```

<br>

#### Right way to jump after doing menu choices
```renpy
menu my_menu:
    "Choice 1" if not done_c1:
        $ done_c1
        jump my_menu
    "Choice 2" if not done_c2:
        $ done_c2
        jump my_menu
    "Choice 3" if not done_c3:
        $ done_c3
        jump my_menu

jump after_menu




# DO NOT DO:
label my_label:
    if done_c1 and done_c2 and done_c3:
        jump after_menu

    menu:
        "Choice 1" if not done_c1:
            $ done_c1
            jump my_label
        "Choice 2" if not done_c2:
            $ done_c2
            jump my_label
        "Choice 3" if not done_c3:
            $ done_c3
            jump my_label
```

<br>

#### Shake with black screen behind
```renpy
label start:
    scene black with None
    show my_image at vshake


transform vshake:
    linear 0.05 yoffset 0
    linear 0.05 yoffset 10
    linear 0.05 yoffset -10
    linear 0.05 yoffset 10
    linear 0.05 yoffset -10
    linear 0.05 yoffset 10
    linear 0.05 yoffset -10
    linear 0.05 yoffset 0
```

<br>

#### Button sounds
```renpy
# gui.rpy
style button:
    properties gui.button_properties("button")
    hover_sound "sounds/hover.ogg"
    activate_sound "sounds/click.ogg"
```

<br>

#### Important! (1080p screen)
```renpy
imagebutton:
    idle Fixed(Transform("image.png", size=(352, 198)), Color((0, 0, 0, 190)), mod_completed_text, maximum=(352, 198))
```

<br>

#### Set style for every displayable on a screen
```renpy
screen example:
    style_prefix "mystyle"

    text "Line 1"
    text "Line 2"
    text "Line 3"

style mystyle_text:
    size 30
```

<br>

#### Imagebutton Animation
```renpy
transform example:
    on hover:
        easein 0.3 zoom 1.2
    on idle:
        easein 0.3 zoom 1.0


imagebutton align (0.5, 0.42) anchor (0.5, 0.5) idle "gui/btn_play.png" at example action NullAction()




transform example:
    on hover, idle:
        easein 0.4 zoom 1.5
        easein 0.4 zoom 1.0


imagebutton idle "btn_idle.png" hover "btn_hover.png" at example
```

#### Transform() and im.MatrixColor()
<br>

```renpy
imagebutton idle Transform("example.png", zoom=0.4) hover Transform(im.MatrixColor("example.png", im.matrix.brightness(0.20)), zoom=0.4)
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

#### Auto-hide screens
```renpy
tag tag_name
tag menu
```

<br>

#### Fixed
An invisible frame. (A frame without the background and borders)
```renpy
screen fast_travel:
    fixed:
         text "Fast travel to.." align (0.5, 0.3)
         textbutton "Floor 1" align (0.25, 0.5) action Jump("floor1")
         textbutton "Floor 2" align (0.50, 0.5) action Jump("floor2")
         textbutton "Back" align (0.75, 0.5) action Hide("fast_travel")
```



<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

---

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
