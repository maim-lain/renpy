# RenPy
- artstation animations

<br>

[**Labels and Control Flow**](https://github.com/maim-lain/renpy/blob/master/notes/labels.md)

[**Dialog and Narration**](https://github.com/maim-lain/renpy/blob/master/notes/dialog.md)

[**Displaying Images**](https://github.com/maim-lain/renpy/blob/master/notes/images.md)

<br>

#### Python
```renpy
python:
    flag = True
    x = 10
    
$ flag = True
$ x = 10
```

#### Init
The init python statement runs Python at initialization time, before the game loads. Among other things, this can be used to define classes and functions, or to initialize styles, config variables, or persistent data.
```renpy
init python:
    if persistent.endings is None:
        persistent.endings = set()

init 1 python:
    # The bad ending is always unlocked.
    persistent.endings.add("bad_ending")
```

Init python statements also take the hide or in clauses.

Variables that have their value set in an init python block are not saved, loaded, and do not participate in rollback. Therefore, these variables should not be changed after init is over.


<br>
<br>

#### While Statement
```renpy
$ count = 10

while count > 0:
    "T-minus [count]."
    $ count -= 1

"Liftoff!"
```
Ren'Py does not have continue, break, or for statements. Continue and break statements can be replaced by jumps to labels placed before or after the while loop, respectively. The first example of a while loop, above, shows how a while loop can replace a for statement.

<br>
<br>

#### Images
```renpy
    scene bg meadow
    
    m "Hey... Umm..."

    show sylvie green smile

    "I'll ask her...!"

    show sylvie green surprised
```
The scene statement clears all images and displays a background image. The show statements display a sprite on top of the background, and change the displaying sprite, respectively.

In Ren'Py, each image has a name. The name consists of a tag, and optionally one or more attributes. Both the tag and attributes should begin with a letter, and can  contain letters, numbers, and underscores. For example:
- the tag is "bg", and the attribute is "meadow." By convention, background images should use the tag bg.
- the tag is "sylvie", and the attributes are "green" and "smile".
- the tag is "sylvie", and the attributes are "green" and "surprised".

Only one image with a given tag can be shown at the same time. When a second image with the same tag is show, it replaces the first image.

Ren'Py searches for image files in the images directory. Ren'Py expects character art to be an PNG or WEBP file, while background art should be a JPG, JPEG, PNG, or WEBP file. The name of a file is very important – the extension is removed, the file name is forced to lowercase, and that's used as the image name.

For example, the following files, placed in the images directory, define the following images.
- "bg meadow.jpg" -> bg meadow
- "sylvie green smile.png" -> sylvie green smile
- "sylvie green surprised.png" -> sylvie green surprised

Images can be placed in subdirectories (subfolders) under the images directory. The directory name is ignored and only the filename is used to define the image name.

Hide Statement. Ren'Py also supports a hide statement, which hides the given image.

It's actually pretty rare that you'll need to use hide. Show can be used when a character is changing emotions, while scene is used when everyone leaves. You only need to use hide when a character leaves and the scene stays the same.

<br>

#### Transition
Above, pictures pop in and out instantaneously. Ren'Py supports transitions that allow effects to be applied when what is being shown changes.

Transitions change what is displayed from what it was at the end of the last interaction (dialogue, menu, or transition – among other statements) to what it looks like after scene, show, and hide statements have run.
```renpy
    scene bg meadow with fade

    m "Hey... Umm..."

    show sylvie green smile with dissolve
```

The with statement takes the name of a transition to use. The most common one is dissolve which dissolves from one screen to the next. Another useful transition is fade which fades the screen to black, and then fades in the new screen.

When a transition is placed after multiple scene, show, or hide statements, it applies to them all at once. If you were to write:
```renpy
    scene bg meadow
    show sylvie green smile
    with dissolve
```

Both the "bg meadow" and "sylvie green smile" images would be dissolved in at the same time. To dissolve them in one at a time, you need to write two with statements:
```renpy
    scene bg meadow
    with dissolve
    show sylvie green smile
    with dissolve
```

This first dissolves in the meadow, and then dissolves in sylvie. If you wanted to instantly show the meadow, and then show sylvie, you could write:
```renpy
    scene bg meadow
    with None
    show sylvie smile
    with dissolve
```

Here, None is used to indicate a special transition that updates Ren'Py's idea of what the prior screen was, without actually showing anything to the player.

<br>

#### Positions
By default, images are shown centered horizontally, and with their bottom edge touching the bottom of the screen.
```renpy
     show sylvie green smile at right
```

To do this repositioning, add an at clause to a show statement. The at clause takes a position, and shows the image at that position. Ren'Py includes several predefined positions:
- left for the left side of the screen
- right for the right side
- center for centered horizontally (the default)
- truecenter for centered horizontally and vertically

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

#### Ending the Game
You can end the game by running the return statement, without having called anything. Before doing this, it's best to put something in the game that indicates that the game is ending, and perhaps giving the user an ending number or ending name.
```renpy
    "Good Ending."
    return
```
That's all you need to make a kinetic novel, a game without any choices in it. Now, we'll look at what it takes to make a game that presents menus to the user.

<br>

#### Menus, Labels, and Jumps
The menu statement lets presents a choice to the player:
```renpy
menu:
    "It's a videogame.":
        jump game
    "It's an interactive book.":
        jump book

label game:
    m "It's a kind of videogame you can play on your computer or a console."
    jump marry

label book:
    m "It's like an interactive book that you can read on a computer or a console."
    jump marry

label marry:
    "And so, we become a visual novel creating duo."
```
In this example, each of the two menu choices runs a single jump statement. The jump statement transfers control to the a label defined using the label statement. After a jump, script statements following the label are run.

If there is no jump statement at the end of the block associated with the label, Ren'Py will continue on to the next statement. The last jump statement here is technically unnecessary, but is included since it makes the flow of the game clearer.

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

