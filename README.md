surfacemapper
=============
Rovers squad for mapping Martian surface.

Installation
____________
```bash
$ git clone https://github.com/kabhinav/surfacemapper.git

$ cd surfacemapper

$ python setup.py install

$ nosetests

If all the tests successfully pass then program can be executed by running:

$ surfacemapper

Follow the program instructions for entering input. To see results, press
Enter (return) when you are prompt to enter co-ordinates of another rover.

OR

$ cat surfacemapper/data/input.txt | python surfacemapper/mapper.py
```

Note: During the installation if you get following error:
```python
from distribute_setup import use_setuptools
     use_setuptools()
ImportError: No module named distribute_setup
```
then the system is missing distribute package. It can be installed by:
```bash
$ wget http://python-distribute.org/distribute_setup.py

$ python distribute_setup.py

after installation of distribute, try again:

$ python setup.py install
```

PROBLEM: MARS ROVERS
____________________
A squad of robotic rovers are to be landed by NASA on a plateau on Mars.
This plateau, which is curiously rectangular, must be navigated by the
rovers so that their on­board cameras can get a complete view of the
surrounding terrain to send back to Earth.

A rover's position and location is represented by a combination of x and
y co­ordinates and a letter representing one of the four cardinal compass
points. The plateau is divided up into a grid to simplify navigation.

An example position might be 0, 0, N, which means the rover is in the bottom
left corner and facing North. In order to control a rover, NASA sends a simple
string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes
the rover spin 90 degrees left or right respectively, without moving from its
current spot. 'M' means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).

INPUT
____
The first line of input is the upper­right coordinates of the plateau, the lower­left
coordinates are assumed to be 0,0. The rest of the input is information pertaining to
the rovers that have been deployed. Each rover has two lines of input. The first line
gives the rover's position, and the second line is a series of instructions telling
the rover how to explore the plateau.

The position is made up of two integers and a letter separated by spaces, corresponding
to the x and y co­ordinates and the rover's orientation. Each rover will be finished
sequentially, which means that the second rover won't start to move until the first
one has finished moving.

OUTPUT
_____
The output for each rover should be its final co­ordinates and heading.

Test Input:
<br>5 5
<br>1 2 N
<br>LMLMLMLMM
<br>3 3 E
<br>MMRMMRMRRM

Expected Output:
<br>1 3 N
<br>5 1 E
