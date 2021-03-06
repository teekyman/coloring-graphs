## coloring-graphs
[![pipeline status](https://aalok-sathe.gitlab.io/coloring-graphs/build.svg?v=3965593111571346127)](https://gitlab.com/aalok-sathe/coloring-graphs/)

a coloring graphs library written in C++ for speedy computation and wrapped in
Python for ease of development and extension!

### what
this library provides support to construct graphs and their coloring graphs.
a coloring graph is a metagraph representing all the valid colorings of a graph.
each vertex of a coloring graph represents a coloring of the base graph.

in this project, we represent a coloring as an integer, which, when converted to
base k (for a k-coloring), represents the vertex-wise colors [0,k).

the library is under development being written using Python and C/C++.
for documentation, feel free to take a look inside `lib/` and read the docstrings.
for examples, see the files in `test/`.
for questions, reach out.

### how
1. installation:

    - manual installation

        clone the repository
        - ssh:
        `git clone git@github.com:aalok-sathe/coloring-graphs`
        - https:
        `git clone https://github.com/aalok-sathe/coloring-graphs`

        go into the repository

        `cd coloring-graphs`

        install

        `make install`
        
    
    - [pypi](https://pypi.org/project/libcolgraph/) (under construction! NOT recommended)

        `python3 -m pip install libcolgraph`

        issues:
        - currently a binary wheel is available only for `manylinux`
          enabled distributions
          e.g. centOS
        - if your distribution is not one of these, then pip will want to
          compile locally using `setup.py`. in that case,
          make sure you have [swig](http://www.swig.org/download.html)
          installed, as it will be needed for compilation.


2. quickstart:

    - usage:

    `import libcolgraph`

    - run a test suite!
    `make test`

    - try the sandbox file (`test/sandbox.py`) to see how plotting works (python-only)
        - `python3 test/sandbox.py 3`
        - `python3 test/sandbox.py 3 test/input/g1.in`


### help

full documentation coming soon


### who

Coloring Graphs lab, University of Richmond. Multiple contributors.


