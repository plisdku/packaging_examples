# .dylib and .so

https://stackoverflow.com/questions/2339679/what-are-the-differences-between-so-and-dylib-on-osx

Mac OS X distinguishes between shared libraries and dynamically loaded modules.  ELF systems like Linux do not distinguish between the two.

Use `otool -hv some_file` and it should tell you the type.

Mach-O shared libraries have the type MH_DYLIB and have the extension `.dylib`.  They can be linked against with the usual static linker flags e.g. `-lfoo`.  They can be created by passing the `-dynamiclib` flag to the compiler.  `-fPIC` is the default and needn't be specified.  (Does this mean that `-dynamiclib` turns on `-fPIC`?  Probably?)

Loadable modules are called "bundles" in Mach-O speak.  They have the file type MH_BUNDLE.  The extension `.bundle` is recommended by Apple, but most ported software uses `.so` for compatibility.  Bundles are used for plugins that extend an application.  They can be created by passing `-bundle` to the compiler.  Bundles cannot be linked against like shared libraries, but a bundle may be linked against real shared libraries.

Of course, confusingly, a "bundle" on Mac OS X can also be a directory with a standardized structure with executable code and resources together...

Both dylibs and bundles can be dynamically loaded using the `dl` APIs (`dlopen`, `dlclose`).

History
-------

In Mac OS 10.0, there was no way to dynamically load libraries.  10.1 introduced dyld APIs to load and unload bundles but they didn't work for dylibs.  10.3 added `dlopen` compatibility with bundles, 10.4 made `dlopen` a native part of dyld and added support for loading but not unloading dylibs.  10.5 added `dlclose` and deprecated the old APIs.


My observation
--------------

A C extension built by `setuptools` is a `.so` file on Mac, which makes it a bundle, so it can't be linked against.


#