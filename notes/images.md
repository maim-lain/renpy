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
- behind
  - Takes a comma-separated list of one or more names. Each name is taken as an image tag. The image is shown behind all images with the given tags that are currently being shown.
- onlayer
  - Takes a name. Shows the image on the named layer.

```renpy
image mary night happy = "mary_night_happy.png"
image mary night sad = "mary_night_sad.png"
image moon = "moon.png"


# Some example show statements would be:


# Basic show.
show mary night sad

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
The show layer statement allows one to apply a transform or ATL transform to an entire layer (such as "master") by using syntax like:
```renpy
show layer master at flip
```
or:
```renpy
show layer master:
    xalign 0.5 yalign 0.5 rotate 180
```
To stop applying transforms to the layer, use:
```renpy
show layer master
```

<br>
<br>

## Scene Statement
The scene statement removes all displayables from a layer, and then shows an image on that layer. It consists of the keyword scene, followed by an image name, followed by zero or more properties. The image is shown in the same way as in the show statement, and the scene statement takes the same properties as the show statement. Like the show statement, the scene statement can take expressions instead of image names.

The scene statement is often used to show an image on the background layer. For example: `scene bg beach`

Clearing a layer. When the image name is omitted entirely, the scene statement clears all displayables from a layer without showing another displayable. `scene`

<br>
<br>

## Hide Statement
The hide statement removes an image from a layer. It consists of the keyword hide, followed by an image name. The hide statement takes the image tag from the image name, and then hides any image on the layer with that tag.

Hide statements are rarely necessary. If a sprite represents a character, then a hide statement is only necessary when the character leaves the scene. When the character changes her emotion, it is preferable to use the show statement instead, as the show statement will automatically replace an image with the same tag.

<br>
<br>

## With Statement
The with statement is used to apply a transition effect when the scene is changed, making showing and hiding images less abrupt. The with statement consists of the keyword with, followed by a simple expression that evaluates either to a transition object or the special value None.

The transition effect is applied between the contents of the screen at the end of the previous interaction (with transient screens and displayables hidden), and the current contents of the scene, after the show and hide statements have executed.

The with statement causes an interaction to occur. The duration of this interaction is controlled by the user, and the user can cause it to terminate early.




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
<br>

### Text Displayables
```renpy
show text "Hello, World" at truecenter with dissolve
pause 1
hide text with dissolve


show text "The last thing you could remember was everything fading to white." at truecenter with fade
pause 5
hide text with Dissolve(1.0)
```

<br>
<br>

## Displayables
A displayable is an object that can be shown to the user. Ren'Py displayables can be used in many ways.
- Assignment to an image name using the image statement.
- Added to a screen using the screen language add statement.
- Assignment to certain config variables.
- Assignment to certain style properties.

Strings may have one or more square-bracket substitutions in them, such as "eileen [mood]" or "eileen_[outfit]_[mood].png".

<br>

#### Applying Transforms to Displayables
The At function produces a displayable from a displayable and one or more transforms.
```renpy
transform birds_transform:
     xpos -200
     linear 10 xpos 800
     pause 20
     repeat

image birds = At("birds.png", birds_transform)
```

<br>

#### Layout Boxes and Grids
Layout boxes are displayables that lay out their children on the screen. They can lay out the children in a horizontal or vertical manner, or lay them out using the standard positioning algorithm.

- Fixed(\*args, \*\*properties)
  - A box that fills the screen. Its members are laid out from back to front, with their position properties controlling their position.
- HBox(\*args, \*\*properties)
  - A box that lays out its members from left to right.
- VBox(\*args, \*\*properties)
  - A layout that lays out its members from top to bottom.
- layeredimage.Fixed(\*args, \*\*properties)
  - A box that fills the screen. Its members are laid out from back to front, with their position properties controlling their position.
- Grid(cols, rows, \*args, \*\*properties)
  - Lays out displayables in a grid. The first two positional arguments are the number of columns and rows in the grid. This must be followed by columns * rows positional arguments giving the displayables that fill the grid.

<br>

```renpy
# Display two logos, to the left and right of each other.
image logo hbox = HBox("logo.png", "logo.png")

# Display two logos, one on top of the other.
image logo vbox = VBox("logo.png", "logo.png")

# Display two logos. Since both default to the upper-left corner of the screen, we need to use Image to place
# those logos on the screen.
image logo fixed = Fixed(
    Image("logo.png", xalign=0.0, yalign=0.0),
    Image("logo.png", xalign=1.0, yalign=1.0))
```

<br>

#### Placeholders
The Placeholder displayable is used to display background or character images as appropriate. Placeholders are used automatically when an undefined image is used in developer mode. Placeholder displayables can also be used manually when the defaults are inappropriate.
```renpy
# Arguments: "boy", "girl", "bg"

image sue = Placeholder("girl")

label start:
     show sue angry
     "Sue" "How do you do? Now you gonna die!"
```

<br>
<br>

## Transforms
A transform can be applied to a displayable to yield another displayable. The built-in transforms are used to control where an object is placed on the screen, while user-defined transforms can cause more complex effects, like motion, zoom, and rotation.

Transforms can be applied by giving the at clause to the scene and show statements. Multiple transforms can be applied by separating them with commas. These transforms are applied from left-to-right, with the rightmost transform taking precedence in the case of conflicts.
```renpy
show eileen happy at right
show eileen happy at halfsize, right
```

<br>

#### Default Transforms
- center
  - Centers horizontally, and aligns to the bottom of the screen.
- default
  - Centers horizontally, and aligns to the bottom of the screen. This can be redefined to change the default placement of images shown with the show or scene statements.
- left
  - Aligns to the bottom-left corner of the screen.
- offscreenleft
  - Places the displayable off the left side of the screen, aligned to the bottom of the screen.
- offscreenright
  - Places the displayable off the left side of the screen, aligned to the bottom of the screen.
- reset
  - Resets the transform. Places the displayable in the top-left corner of the screen, and also eliminates any zoom, rotation, or other effects.
- right
  - Aligns to the bottom-right corner of the screen.
- top
  - Centers horizontally, and aligns to the top of the screen.
- topleft
  - Aligns to the top-left corner of the screen.
- topright
  - Aligns to the top-right corner of the screen.
- truecenter
  - Centers both horizontally and vertically.

<br>

```
+-----------------------------------------------------------+
|topleft, reset               top                   topright|
|                                                           |
|                                                           |
|                                                           |
|                                                           |
|                          truecenter                       |
|                                                           |
|                                                           |
|                                                           |
|                                                           |
|left                   center, default                right|
+-----------------------------------------------------------+
```
