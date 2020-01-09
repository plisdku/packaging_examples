# Vanilla Extension Example

Using `ctypes` and `setuptools.Extension`.

## Authors
Paul Hansen

## Structure

The structure is inspired by [Benjamin Jack](https://www.benjack.io/2018/02/02/python-cpp-revisited.html) who was inspired by [Ionel Cristian Mărieș](https://blog.ionelmc.ro/2014/05/25/python-packaging/).

The key observation of Jack is to make sure nothing outside `src/` is accidentally added to the global namespace on installation.  In `setup.py` we use `find_packages('src')`  and `package_dir=('':'src')` for this reason.

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

These things are here for a reason.
- `MANIFEST.in` puts **header files** and **tests** in the distribution.  (damn, no other way?)
- `README.md` is this document
- `setup.py` is sufficient for installation but we also need `MANIFEST.in` for distribution
- `src` is home to the Python packages.  One is Python, one has a C++ extension.
- `tests` has a smoke test.  Try `py.test .` and see if the binary got built and all.

If I hadn't mentioned the `.hpp` files in the manifest then they would not have been included in the sdist.
If you want to make do without the header file when you build the extension, just put the `extern "C"` function declarations into the `.cpp` file.  Well, it works for one file at least.  I tried it.

## Goal

`nativepkg` should install and run seamlessly, on my Mac first then on Linux.

I should be able to install the package with pip and it will build its C++ extension and install the `.dylib` or `.so` or whatever it is in the right place and then I can load the DLL with `ctypes` in `nativepkg` after installation.

# Installation

For development,

```
pip install -e .
```

or for real

```
pip install .
```

Note that `setuptools.find_packages` returns `['pythonpkg', 'nativepkg']`.










#
