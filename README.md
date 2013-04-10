g-code-generators
==================

Overview
--------

A series of Perl programs to generate G code for the ShapeOko CNC mill (and others)

The G Code output should be pretty generic and run on most mills.

It does not start or stop the spindle, nor turn any coolant on and off.

I make no guarantees though, so please make sure that the code that is output is
safe for your machine.

Included Programs
-----------------

generate_hole_array - generates the G code to mill a series of holes in an array
pattern. Includes ability to add a counterbore to the holes. Now includes a
spiral boring method.

License
-------

This work is licensed under the Creative Commons Attribution-ShareAlike 3.0
Unported License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/3.0/

In short this means:

You are free:

* to Share — to copy, distribute and transmit the work
* to Remix — to adapt the work
* to make commercial use of the work

Under the following conditions:

* Attribution — You must attribute the work in the manner specified by the author or licensor (but not in any way that suggests that they endorse you or your use of the work).
* Share Alike — If you alter, transform, or build upon this work, you may distribute the resulting work only under the same or similar license to this one.
