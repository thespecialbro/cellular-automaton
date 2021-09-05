# cellular-automaton
Playing around with making a cellular automaton with pygame

![Gif of simulation](https://media3.giphy.com/media/boxTcNhNueFVJKD3Xd/giphy.gif)

This simulation currently only does Conway's Game of Life, but in the future I may add support for other cellular automata.

## Installation

This project requires python 3(.9) and pygame 2

Clone the repository to your computer

`$ git clone https://github.com/thespecialbro/cellular-automaton.git`

If not already done, install/upgrade python and pygame

[Python installation](https://www.python.org/downloads/)

`$ python -m pip install pygame==2.0.1` or simply `pip install pygame`

Navigate to the directory you cloned the repository to and run the program

`$ python pygame-cells.py`

---

If, for what ever reason, you wish not to or cannot install pygame you can run the text-based version of the simulation with `$ python cells.py`

However, with the text-based version there is no way to edit the cells 'in situ'; they can only be pre-set at the bottom of the `cells.py` file in the two-dimensional array of 1's and 0's named `cells` where 1's are 'alive' cells.
