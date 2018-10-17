# Labels and Control Flow


## Label Statement

Label statements allow the given name to be assigned to a program point. They exist solely to be called or jumped to, either from Ren'Py script, Python functions, or from screens.

label sample1:
    "Here is 'sample1' label."

label sample2(a="default"):
    "Here is 'sample2' label."
    "a = [a]"

A label statement may have a block associated with it. In that case, control enters the block whenever the label statement is reached, and proceeds with the statement after the label statement whenever the end of the block is reached.

There are two kinds of labels: global and local labels. Global labels live in one global scope shared across all project files and thus should have unique names per game. Local labels logically reside inside the scope of the global label they are declared in. To declare a local label, prefix its name with a period .. For example:

label global_label:
    "Inside a global label.."
label .local_name:
    "..resides a local one."
    jump .local_name

Local labels can be referenced directly inside the same global label they are declared in or by their full name, consisting of global and local name parts:

label another_global:
    "Now lets jump inside local label located somewhere else."
    jump global_label.local_name

The label statement may take an optional list of parameters. These parameters are processed as described in PEP 3102, with two exceptions:

    The values of default parameters are evaluated at call time.
    The variables are dynamically, rather than lexically, scoped.

Jump Statement

The jump statement is used to transfer control to the given label.

If the expression keyword is present, the expression following it is evaluated, and the string so computed is used as the label name of the statement to jump to. If the expression keyword is not present, the label name of the statement to jump to must be explicitly given.

Unlike call, jump does not push the next statement onto a stack. As a result, there's no way to return to where you've jumped from.

label loop_start:

    e "Oh no! It looks like we're trapped in an infinite loop."

    jump loop_start

Call Statement

The call statement is used to transfer control to the given label. It also pushes the next statement onto the call stack, allowing the return statement to return control to the statement following the call.

If the expression keyword is present, the expression following it is evaluated, and the string so computed is used as the name of the label to call. If the expression keyword is not present, the name of the statement to call must be explicitly given.

If the optional from clause is present, it has the effect of including a label statement with the given name as the statement immediately following the call statement. An explicit label helps to ensure that saved games with return stacks can return to the proper place when loaded on a changed script.

e "First, we will call a subroutine."

call subroutine

call subroutine(2)

call expression "subroutine" pass (count=3)

# ...

label subroutine(count=1):

    e "I came here [count] time(s)."
    e "Next, we will return from the subroutine."

    return

The call statement may take arguments, which are processed as described in PEP 3102.

When using a call expression with an arguments list, the pass keyword must be inserted between the expression and the arguments list. Otherwise, the arguments list will be parsed as part of the expression, not as part of the call.
Return Statement

The return statement pops the top statement off of the call stack, and transfers control to it. If the call stack is empty, the return statement restarts Ren'Py, returning control to the main menu.

If the optional expression is given to return, it is evaluated, and it's result is stored in the _return variable. This variable is dynamically scoped to each context.
Special Labels

The following labels are used by Ren'Py:

start
    By default, Ren'Py jumps to this label when the game starts.
quit
    If it exists, this label is called in a new context when the user quits the game.
after_load
    If it exists, this label is called when a game is loaded. It can be use to fix data when the game is updated.
splashscreen
    If it exists, this label is called when the game is first run, before showing the main menu.
before_main_menu
    If it exists, this label is called before the main menu. It is used in rare cases to set up the main menu, for example by starting a movie playing in the background.
main_menu

    If it exists, this label is called instead of the main menu. If it returns, Ren'Py will start the game at the start label. For example, the following will immediately start the game without displaying the main menu.

    label main_menu:
        return

after_warp
    If it is existed, this label is called after a warp but before the warped-to statement executes. Please see Warping to a line.

Labels & Control Flow Functions

renpy.call_in_new_context(label, *args, **kwargs)

    This creates a new context, and then starts executing Ren'Py script from the given label in that context. Rollback is disabled in the new context, and saving/loading will occur in the top level context.

    This is used to begin a second interaction with the player Use this to begin a second interaction with the user while inside an interaction.

renpy.get_all_labels()

    Returns the set of all labels defined in the program, including labels defined for internal use in the libraries.

renpy.get_return_stack()

    Returns a list giving the current return stack. The return stack is a list of statement names.

    The statement names will be strings (for labels), or opaque tuples (for non-label statements).

renpy.has_label(name)

    Returns true if name is a valid label the program, or false otherwise.

    name
        Should be a string to check for the existence of a label. It can also be an opaque tuple giving the name of a non-label statement.

renpy.invoke_in_new_context(callable, *args, **kwargs)

    This function creates a new context, and invokes the given Python callable (function) in that context. When the function returns or raises an exception, control returns to the the original context. It's generally used to call a Python function that needs to display information to the player (like a confirmation prompt) from inside an event handler.

    A context maintains the state of the display (including what screens and images are being shown) and the audio system. Both are restored when the context returns.

    Additional arguments and keyword arguments are passed to the callable.

    A context created with this function cannot execute Ren'Py script. Functions that would change the flow of Ren'Py script, like renpy.jump(), are handled by the outer context. If you want to call Ren'Py script rather than a Python function, use renpy.call_in_new_context() instead.

renpy.jump_out_of_context(label)

    Causes control to leave the current context, and then to be transferred in the parent context to the given label.

renpy.seen_label(label)

    Returns true if the named label has executed at least once on the current user's system, and false otherwise. This can be used to unlock scene galleries, for example.

renpy.set_return_stack(stack)

    Sets the current return stack. The return stack is a list of statement names.

    Statement names may be strings (for labels) or opaque tuples (for non-label statements).

