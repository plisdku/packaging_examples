# Vanilla Extension Example

Build and install a native C++ extension package and a normal Python package.  Uses standard C extension stuff, no CMake.

Make sure that `python setup.py sdist` puts everything where it belongs and it works on Linux.

This example uses `ctypes` and figures out where to load the DLL from.

## Authors
Paul Hansen
January 8, 2020

## Structure

The structure is inspired by [Benjamin Jack](https://www.benjack.io/2018/02/02/python-cpp-revisited.html) who was inspired by [Ionel Cristian Mărieș](https://blog.ionelmc.ro/2014/05/25/python-packaging/).

The key observation of Mr. Jack is to make sure nothing outside `src/` is accidentally added to the global namespace on installation.  In `setup.py` we use `find_packages('src')`  and `package_dir=('':'src')` for this reason.

```
extension_vanilla
├── MANIFEST.in
├── README.md
├── setup.py
├── src
│   ├── nativepkg
│   │   ├── interface.cpp
│   │   ├── interface.hpp
│   │   └── interface.py
│   └── pythonpkg
│       └── hello.py
└── tests
    └── test_smoke.py
```

I think I used a minimal set of files given what I attempted:
- `MANIFEST.in` puts **header files** and **tests** in the distribution.  (damn, no other way?)
- `README.md` is this document
- `setup.py` is sufficient for installation but we also need `MANIFEST.in` for distribution
- `src` is home to the Python packages.  One is Python, one has a C++ extension.
- `tests` has a smoke test.  Try `py.test .` and see if the binary got built and all.

If I hadn't mentioned the `.hpp` files in the manifest then they would not have been included in the sdist.
If you want to make do without the header file when you build the extension, just put the `extern "C"` function declarations into the `.cpp` file.  Well, it works for one file at least.  I tried it.

# Installation

```
pip install -e .       # development-mode installation
pip install .          # "real" installation
python3 setup.py sdist # make a tarball with everything in it
```









#
