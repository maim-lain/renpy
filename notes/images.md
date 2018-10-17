# Displaying Images

The four statements that work with images are:
- image - Defines a new image
- show - Shows an image on a layer
- scene - Clears a layer, and optionally shows an image on that layer
- hide - Removes an image from a layer

Ren'Py also has the with statement, which allows effects to be applied when the scene is changed.

<br>
<br>

## Concepts
### Image
An image is something that can be show to the screen using the show statement. An image consists of a name and a displayable. When the image is shown on a layer, the displayable associated with it is displayed on that layer.

The first word of the image name is called the image tag. The second and later words of the name are the image attributes.

For example: `mary beach night happy` The image tag is mary, while the image attributes are beach, night, and happy.

A displayable is something that can be shown on the screen. The most common thing to show is a static image, which can be specified by giving the filename of the image, as a string. However, an image may refer to any displayable Ren'Py supports. The same statements that are used to display images can also be used for animations, solid colors, and the other types of displayables.

<br>

### Layer (ignore)
A layer is a list of displayables that are shown on the screen. Ren'Py supports multiple layers, including user-defined layers. The order of the layers is fixed within a game (controlled by the config.layers variable), while the order of displayables within a layer is controlled by the order in which the scene and show statements are called, and the properties given to those statements.

The following layers are defined as part of Ren'Py:
- master
  - This is the default layer that is used by the scene, show, and hide statements. It's generally used for backgrounds and character sprites.
- transient
  - The default layer used by ui functions. This layer is cleared at the end of each interaction.
- screens
  - This layer is used by the screen system.
- overlay
  - The default layer used when a ui function is called from within an overlay function. This layer is cleared when an interaction is restarted.

Additional layers can be defined by updating config.layers, and the various other layer-related config variables. Using renpy.layer_at_list(), one or more transforms can be applied to a layer.

<br>
<br>

## Defining Images
There are two ways to define images. You can either place an image file in the image directory, or an image can be defined using the image statement. The former is simple, as it involves placing properly named files in a directory, while the latter a allows more control over how the image is defined, and allows images that are not image files.

<br>

### Images Directory
The image directory is named "images", and is placed under the game directory. When a file with the .jpg or .png extension is placed underneath this directory, the extension is stripped, the rest of the filename is forced to lower case, and the resulting filename is used as the image name if an image with that name has not been previously defined.

This process takes place in all directories underneath the image directory. For example, all of these files will define the image eileen happy:
```
game/images/eileen happy.png
game/images/Eileen Happy.jpg
game/images/eileen/eileen happy.png
```

<br>

### Image Statement
The image statement is used to define an image. An image statement consists of the keyword image, followed by an image name, an equals sign, and a displayable. For example:
```renpy
image eileen happy = "eileen_happy.png"
image black = "#000"
image bg tiled = LiveTile("tile.jpg")

image eileen happy question = VBox(
    "question.png",
    "eileen_happy.png",
    )
```

<br>

When an image is not directly in the game directory, you'll need to give the directories underneath it. For example, if the image is in game/eileen/happy.png, then you can write:
```renpy
image eileen happy = "eileen/happy.png"
```

<br>
<br>

## Show Statement
The show statement is used to display an image on a layer. A show statement consists of a the keyword show, followed by an image name, followed by zero or more properties.

If the show statement is given the exact name of an existing image, that image is the one that is shown. Otherwise, Ren'Py will attempt to find a unique image that:
- Has the same tag as the one specified in the show statement.
- Has all of the attributes given in the show statement.
- If an image with the same tag is already showing, shares the largest number of attributes with that image.

If an image with the same image tag is already showing on the layer, the new image replaces it. Otherwise, the image is placed above all other images in the layer. (That is, closest to the user.) This order may be modified by the zorder and behind properties.

The show statement does not cause an interaction to occur. For the image to actually be displayed to the user, a statement that causes an interaction (like the say, menu, pause, and with statements) must be run.

The show statement takes the following properties:
- as
  - The as property takes a name. This name is used in place of the image tag when the image is shown. This allows the same image to be on the screen twice.
- at
  - The at property takes one or more comma-separated simple expressions. Each expression must evaluate to a transform. The transforms are applied to the image in left-to-right order.
  - If no at clause is given, Ren'Py will retain any existing transform that has been applied to the image. If no transform exists, the image will be displayed using the default transform.
behind
  - Takes a comma-separated list of one or more names. Each name is taken as an image tag. The image is shown behind all images with the given tags that are currently being shown.
onlayer
  - Takes a name. Shows the image on the named layer.
- zorder
  - Takes an integer. The integer specifies the relative ordering of images within a layer, with larger numbers being closer to the user. This isn't generally used by Ren'Py games, but can be useful when porting visual novels from other engines.

Assuming we have the following images defined:
```renpy
image mary night happy = "mary_night_happy.png"
image mary night sad = "mary_night_sad.png"
image moon = "moon.png"
```

<br>

Some example show statements are:
```renpy
# Basic show.
show mary night sad

# Since 'mary night happy' is showing, the following statement is
# equivalent to:
# show mary night happy
show mary happy

# Show an image on the right side of the screen.
show mary night happy at right

# Show the same image twice.
show mary night sad as mary2 at left

# Show an image behind another.
show moon behind mary, mary2

# Show an image on a user-defined layer.
show moon onlayer user_layer
```

<br>

#### Show Expression
A variant of the show statement replaces the image name with the keyword expression, followed by a simple expression. The expression must evaluate to a displayable, and the displayable is shown on the layer. To hide the displayable, a tag must be given with the as statement.

For example: `show expression "moon.png" as moon`

#### Show Layer
The show layer statement allows one to apply a transform or ATL transform to an entire layer (such as "master"), using syntax like:

show layer master at flip

or:

show layer master:
    xalign 0.5 yalign 0.5 rotate 180

To stop applying transforms to the layer, use:

show layer master





<br>
<br>
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
