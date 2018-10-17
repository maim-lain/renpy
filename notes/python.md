# Python

<br>

Multi-line python:
```renpy
python:
    flag = True
    x = 10
```

<br>

Single line python:
```renpy
$ flag = True
$ x = 10
```

<br>
<br>

## Init
The init python statement runs Python at initialization time, before the game loads. Among other things, this can be used to define classes and functions, or to initialize styles, config variables, or persistent data.
```renpy
init python:
    if persistent.endings is None:
        persistent.endings = set()

init 1 python:
    # The bad ending is always unlocked.
    persistent.endings.add("bad_ending")
```
Variables that have their value set in an init python block are not saved, loaded, and do not participate in rollback. Therefore, these variables should not be changed after init is over.

<br>
<br>

## Define Statement
The define statement sets a single variable to a value at init time.
```renpy
define e = Character("Eileen")
```
is equivalent to:
```renpy
init python:
    e = Character("Eileen")
```

<br>
<br>

## Default Statement
The default statement sets a single variable to a value if that variable is not defined when the game starts, or after a new game is loaded.

When the variable points is not defined at game start, these statement are equivalent:
```renpy
default points = 0

label start:
    $ points = 0

# When the variable points is not defined at game load, it's equivalent to:
label after_load:
    $ points = 0
```

<br>
<br>

## Loops
You can do any loop in Python, but can only do a while loop with Ren'Py.

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

## Pass Statement
The pass statement can be used when a block is required, but no statement is suitable. It does nothing.
```renpy
elif points >= 1:
    pass
```
