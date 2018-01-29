# rolympics

```
╔═══╗ ╔═══╗ ╔═══╗  
║  ╔║══╗ ╔║══╗  ║  
╚══║╝ ╚══║╝ ╚═══╝  
   ╚═══╝ ╚═══╝  
```

## Installation

Dependencies:
  * Python 3
  * pyglet

Rolympics requires Python 3. On Linux, use [pyenv](https://github.com/pyenv/pyenv) (recommended) or your package manager, to install Python 3. On Mac and Windows, it is recommended to install the [Anaconda](https://www.anaconda.com/download/) environment.

Before starting the program, [pyglet](https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/) must be installed. The easiest way to achieve this is through pip.

    pip install pyglet

Read on to find out how to run pip in your terminal in Mac/Windows.

### Windows

This assumes you have Anaconda (see above) installed. Start the *Anaconda Prompt*. At the command prompt, type:

    C:\Users\S> pip install pyglet

(You have to typ `pip install pyglet` only, then press <Enter>; the `C:\Users\S>` is part of the prompt).

### Mac

Open a Terminal and install pyglet typing:

    $ pip install pyglet
    
(You have to type `pip install piglet` only, then press <Enter>; the `$` sign is part of Terminal).
   
## Running

To run the simulation, open a terminal (see above), navigate into the project directory, and type

    python run.py
    
The simulation should appear.

On Windows, the terminal to use is called *Anaconda Prompt*; in Mac, use the *Terminal* App; in Linux, you know where the terminal is... ;)

To change into the project directory in a terminal, use the `cd` command.

For example, in Windows, after opening the terminal the prompt may read `C:\Users\S\Documents`. You are in the directory `Documents`, which itself is inside `S`, which itself is inside `Users`.

    C:
      |-- Users
          |-- S
              |-- Documents
              |-- Desktop
                  |-- rolympics-master
                 
To get into the project directory `rolympics-master`, you need to type:

    C:\Users\S\Documents> cd ..
    C:\Users\S> cd Desktop
    C:\Users\S\Desktop> cd rolympics-master
    C:\Users\S\Desktop\rolympics-master>  python run.py
    
You are now inside the project directory, type `python run.py` to start!
