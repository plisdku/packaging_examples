# Examples of Python/C++ integration

## 20.01.10

I want to install a C++ tool with Python API using pip.  There are a couple ways to do this:
1. Use pip to distribute a C++ tool, and a Python API for it, together.  I think this is out of the scope of pip, now.
2. Use pip to distribute a Python tool with a huge C++ extension.  I think this might be doable.

I have tried a bunch of pip/CMake mashup examples and I can't get them to work on my Mac.  I need to figure it out on my own then.

## 20.01.08

Gave up on CMake at first.  Just made a bare-bones C++ example.  I built my C++ `.so` using `setuptools.Extension`, the usual way.  Learned that on Mac OS X a `.so` file is called a "bundle" and cannot be linked against, only dynamically loaded.  The `.so` file was dropped into my `src` directory adjacent to its corresponding Python package directory, and also installed in `site-packages` directly next to its Python package directory.

I used ctypes to implement my extension.  I was sensing that this may be kind of a strange approach.  Most people compiling extensions with setuptools were writing C that included `Python.h` and went from there.  So it was impossible to find examples with ctypes.  My big question with ctypes was, what is the path to the library so I can dynamically load it from Python?

## 20.01.07

Tried without success to get some CMake/setuptools integration examples to work.  I got a bunch of `clang` crashes and I could not for the life of me figure out where the erroneous build instructions were coming from.
