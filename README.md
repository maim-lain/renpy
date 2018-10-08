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
https://www.renpy.org/doc/html/quickstart.html#transitions
