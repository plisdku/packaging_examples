# Building Trogdor with pip

## As Python Extension

Note that `setuptools.build_ext` inherits from `distutils.build_ext` or something.  It's really quite a tangly web of things.

`distutils` is built in to the Python distribution I have, but I think `setuptools` is in my local `site-packages` for some reason.  My `distutils` has specializations for Mac compilers.  Somehow it knows about `clang` and `clang++` and it has language identification and such.  I hope I can accomplish my goals without becoming an expert on `distutils`.


## From Python docs

> A C extension for CPython is a shared library (_e.g._ a `.so` file on Linux, `.pyd` on Windows), which exports an _initialization function._  To be importable, the shared library must be available on `PYTHONPATH`, and must be named after the module name, with an appropriate extension.  When using distutils, the correct filename is generated automatically.

It seems like usually an Extension module will include ``Python.h``.  Ohh.  So maybe I don't actually know what a Python extension module is, or how it differs from Python code using `ctypes`.

According to https://docs.python.org/3/extending/extending.html, the C extension interface is specific to CPython; in many cases you can avoid writing C extensions.  For instance if you just want C library functions or system calls, try `ctypes` or `cffi` instead.  These let you write Python code to interface with C code and are more portable between implementations of Python than writing and compiling a C extension module.  Ok.

According to the `cffi` docs, on non-Windows platforms, C libraries typically have a specified C API but not an ABI (_e.g._ they may document a struct as having at least certain fields, but maybe more).  So `cffi`, based on the LuaJIT's FFI, calls the C compiler from the declarations you write to validate and link to the C language constructs.

## Cython, pybind11, cffi

http://blog.behnel.de/posts/cython-pybind11-cffi-which-tool-to-choose.html

It is sugested that a general shortcoming of all wrapper generators is that many users eventually reach the limit of their capabilities in performance, features, language integration from one side or the other, etc.  Then the users are fighting the tools after that, and sometimes will start over from scratch with a new tool.

Wrapper generators are like SWIG, shiboken.

So most projects are thought to be better starting off directly with a manually-written wrapper, at least as long as they don't have to wrap a huge API.

* `Cython` is a static Python compiler.  It translates Python into C.  For wrapping native libraries, it's great for designing a Python API, and keeps attention focused on usage from the Python side.

* `pybind11` is modern C++ with Python integration.  It provides a C++ API that wraps native functions and classes into Python representations using the compile time introspection features added to C++11.  The user is focused on the C++ side of things.  `pybind11` creates a Python API.

* `CFFI` is Python with a dynamic runtime interface to native code.  It is similar to `ctypes`, but generally faster and easier to use.  Runtime overhead keep it from matching the performance of Cython and pybind11 in CPython.  Also because it needs a well-defined ABI, C++ support is mostly lacking.  (Hm.)

## Ctypes

The `find_library` function in `ctypes` used to have some issues on Linux due to not searching the `LD_LIBRARY_PATH` or something, but this was fixed in 2016 for Python 3.6.  Ok.  What I learn here is, maybe I should use `find_library`.

https://docs.python.org/3/library/ctypes.html#finding-shared-libraries

When progarmming in a compiled language, shared libraries are accessed when compiling/linking a program, and when the program is run.

The purpose of the `find_library()` function is to locate a library in a way similar to what the compiler or runtime loader does, _i.e._ load the most recent version on platforms with several versions.

On Linux, `find_library()` tries to run external programs `/sbin/ldconfig`, `gcc`, `objdump` and `ld` to find the library file, as well as using `LD_LIBRARY_PATH` if the library cannot be found by other means.  It will return the FILENAME _e.g._ `libc.so.6`.

On OS X, `find_library()` tries several predefined naming schemes and paths, and will return the FULL PATHNAME, _e.g._ `/usr/lib/libc.dylib`.

On Windows, `find_library()` searches along system search paths, and returns the full pathname, but because there is no predefined naming scheme you can't say just `find_library("c")` like on Linux or Mac.

So they say it may be better (maybe) to determine the shared library name at development time and hardcode it into the wrapper module instead of using `find_library`.


## scikit-build

Roughly, they say:

Replacement for `distutils.core.Extension` with some advantages:
- better support for additional compilers and build systems
- first-class cross-compilation support
- location of dependencies and their associated build requirements

You must add a `pyproject.toml` to the build system requirements.

```
[build-system]
requires = ["setuptools", "wheel", "scikit-build", "cmake", "ninja"]
```

By default, a CMakeLists.txt is expected at the top level.

### Without CMake

The standard C++ extension.