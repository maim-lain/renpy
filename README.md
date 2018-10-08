# RenPy
- mythic manor + four elements
- dating sim + time of day cycle
- fet farm
- artstation animations


The start label is special, as it's where Ren'Py scripts begin running when the user clicks "Start Game" on the main menu.

#### Character
```renpy
define m = Character('Me', color="#c8c8ff")
```

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
    scene bg meadow
    with fade

    m "Hey... Umm..."

    show sylvie green smile
    with dissolve
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
