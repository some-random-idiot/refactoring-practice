## Refactoring Practice

Copy this template repository to your own Github account. Then clone it to your computer and do the refactorings.  Push your work to Github.

Each subdirectory contains some code that needs refactoring.

1. In this README, write one line describing each refactoring you apply and why.
2. Perform the refactoring in the subdirectory code.


## `time/timestamp.py`

**Changes made:**
1. Changed the function name to conform to the snake case naming convention.
2. Add one more blank line between the function and the import statement.
3. Fixed the return value's syntax.
4. Gave meaningful variable names to `args[...]`.
5. Removed redundant else statement.
6. Extracted a method for timestamp validity check.

## `game_framework/gamelib.py`

**Changes made:**
1. Added one more blank line between the class `GameCanvasElement` and the import statements.
2. Removed redundant parenthesis from `GameCanvasElement`.
3. `create_canvas` no longer creates a canvas via side effect, it instead returns the canvas object.
4. `create_canvas` no longer access the width and height class attributes directly, it takes in parameters instead.
5. Replaced a string literal (`"news"`) with a named constant (`tk.NSEW`).
6. Encapsulated the process adding and removing game elements.
7. Created constant variables for `GameApp` constructor's default values.

## `recipe/recipe.py` and `recipe/main.py`

**Changes made:**


This uses a `dataclass`, which requires Python 3.7.

The Recipe class defines a recipe for a hot beverage with attributes:
* name - name of the recipe
* coffee - units of coffee
* chocolate - units of chocolate
* milk - units of milk
* sugar - units of sugar
* price - (float) price in Baht

Refactor `main.py`.  What can you do to eliminate the long, boring code?






## Resources

* <https://refactoringguru.com/refactoring> 
* *Refactoring - Improving the Design of Existing Code* by Martin Fowler.  The bible on refactoring.  The first 4 chapters explain the fundamentals.
* <https://refactoring.com> Online version of Fowler's book, but lacks explanation of the refactorings.
