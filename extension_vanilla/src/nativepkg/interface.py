import ctypes
import pathlib
import glob
import os

parent_dir = os.path.join(os.path.dirname(__file__), os.path.pardir)
print("parent dir:", parent_dir)
path_to_dylib = glob.glob(f"{parent_dir}/*nativepkg*so")
print(path_to_dylib)

ctypes.cdll.LoadLibrary(path_to_dylib[0])
_lib = ctypes.CDLL(path_to_dylib[0])

add = _lib.add
add.argtypes = [ctypes.c_int, ctypes.c_int]
add.restype = ctypes.c_int

subtract = _lib.subtract
subtract.argtypes = [ctypes.c_int, ctypes.c_int]
subtract.restype = ctypes.c_int
