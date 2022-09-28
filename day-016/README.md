# The `turtle` module

---
## Notes
- Pay attention to `mode`: “standard”/”world” or “logo”
- It uses `tkinter` for the underlying graphics, it needs a version of Python installed with `Tk` support.
- The object-oriented interface uses essentially two+two classes:
    1. The `TurtleScreen` class defines graphics windows as a playground for the drawing turtles. Its constructor needs a `tkinter.Canvas` or a `ScrolledCanvas` as argument. It should be used when `turtle` is used as part of some application.
    The function `Screen()` returns a singleton object of a `TurtleScreen` subclass. This function should be used when `turtle` is used as a standalone tool for doing graphics. As a singleton object, inheriting from its class is not possible.
    2. `RawTurtle` (alias: `RawPen`) defines `Turtle` objects which draw on a `TurtleScreen`. Its constructor needs a `Canvas`, `ScrolledCanvas` or `TurtleScreen` as argument, so the `RawTurtle` objects know where to draw. 
    Derived from `RawTurtle` is the subclass `Turtle` (alias: `Pen`), which draws on “the” `Screen` instance which is automatically created, if not already present.

## Overview of available Turtle and Screen methods
### Turtle methods
#### Turtle motion
##### Move and draw
- [x] `forward() | fd()`
    Move the turtle forward by the specified *distance*, in the direction the turtle is headed.
- [x] `backward() | bk() | back()`
    Move the turtle backward by *distance*, opposite to the direction the turtle is headed. Do not change the turtle’s heading.
- [x] `right() | rt()`
    Turn turtle right by angle units. (Units are by default `degrees`, but can be set via the `degrees()` and `radians()` functions.) Angle orientation depends on the turtle `mode`.
- [x] `left() | lt()`
    Turn turtle left by angle units. (Units are by default `degrees`, but can be set via the `degrees()` and `radians()` functions.) Angle orientation depends on the turtle `mode`.
- [x] `goto() | setpos() | setposition()`
    Move turtle to an absolute position. If the pen is down, draw line. Do not change the turtle’s orientation.
    **Notes** By default the `(0,0)` position is in the middle, center of the rectangle `Canvas`, with 4 quadrant counter-clockwise just like Eucleadean geometry.
- [x] `setx()`
    Set the turtle’s first coordinate to x, leave second coordinate unchanged.
- [x] `sety()`
    Set the turtle’s second coordinate to y, leave first coordinate unchanged.
- [x] `setheading() | seth()`
    Set the orientation of the turtle to `to_angle`.
- [x] `home()`
    Move turtle to the origin – coordinates (0,0) – and set its heading to its start-orientation. (which depends on the mode, see `mode()`).
- [x] `circle()`
    ```python
    turtle.circle(radius, extent=None, steps=None)
    ```
    Draw a circle with given `radius`. The center is `radius` units left of the turtle (**the heading of the turtle**); `extent` – an angle – determines which part of the circle is drawn. If `extent` is not given, draw the entire circle. If `extent` is not a full circle, one endpoint of the arc is the current pen position. Draw the arc in counterclockwise direction if `radius` is positive, otherwise in clockwise direction. Finally the direction of the turtle is changed by the amount of `extent`.

    As the circle is approximated by an inscribed regular polygon, steps determines the number of steps to use. If not given, it will be calculated automatically. May be used to draw regular polygons.
    ```python
    >>> turtle.circle(120, 180)  # draw a semicircle
    ```
- [x] `dot()`
    ```python
    turtle.dot(size=None, *color)
    ```
    Draw a circular dot with diameter `size`, using `color`. If size is not given, the maximum of `pensize+4` and `2*pensize` is used.
- [x] `stamp()`
    Stamp a copy of the turtle shape onto the canvas at the current turtle position. Return a `stamp_id` for that stamp, which can be used to delete it by calling `clearstamp(stamp_id)`.
- [x] `clearstamp()`
    Delete stamp with given `stampid`.
- [x] `clearstamps()`
    Delete all or first/last n of turtle’s stamps. If n is `None`, delete all stamps, if n > 0 delete first n stamps, else if n < 0 delete last n stamps.
- [x] `undo()`

    Undo (repeatedly) the last turtle action(s). Number of available undo actions is determined by the size of the undobuffer.
- [x] `speed()`

    Set the turtle’s speed to an integer value in the range 0..10. If no argument is given, return current speed.

    If input is a number greater than 10 or smaller than 0.5, speed is set to 0. Speedstrings are mapped to speedvalues as follows:

    - “fastest”: 0
    - “fast”: 10
    - “normal”: 6
    - “slow”: 3
    - “slowest”: 1

    Speeds from 1 to 10 enforce increasingly faster animation of line drawing and turtle turning.
##### Tell Turtle’s state
##### Settings for measurement


#### Pen control 