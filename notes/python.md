# Python

<br>

```renpy
python:
    flag = True
    x = 10
    
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

Init python statements also take the hide or in clauses.

Variables that have their value set in an init python block are not saved, loaded, and do not participate in rollback. Therefore, these variables should not be changed after init is over.

<br>
<br>
