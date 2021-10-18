## Refactoring Practice

Copy this template repository to your own Github account. Then clone it to your computer and do the refactorings.  Push your work to Github.

Each subdirectory contains some code that needs refactoring.

1. In this README, write one line describing each refactoring you apply and why.
2. Perform the refactoring in the subdirectory code.


## `time/timestamp.py`

**Changes made:**
1. Changed the function name to conform to the snake case naming convention.
3. Fixed the return value's syntax.
4. Gave meaningful variable names to `args[...]`.
5. Removed redundant else statement.
6. Extracted a method for timestamp validity check.

## `game_framework/gamelib.py`

**Changes made:**
1. Removed redundant parenthesis from `GameCanvasElement`.
2. `create_canvas` no longer creates a canvas via side effect, it instead returns the canvas object.
3. `create_canvas` no longer access the width and height class attributes directly, it takes in parameters instead.
4. Replaced a string literal (`"news"`) with a named constant (`tk.NSEW`).
5. Encapsulated the process adding and removing game elements.
6. Created constant variables for `GameApp` constructor's default values.

## `recipe/recipe.py` and `recipe/main.py`

**Change made:** Created a method for recipe creation process.


## Resources

* <https://refactoringguru.com/refactoring> 
* *Refactoring - Improving the Design of Existing Code* by Martin Fowler.  The bible on refactoring.  The first 4 chapters explain the fundamentals.
* <https://refactoring.com> Online version of Fowler's book, but lacks explanation of the refactorings.
