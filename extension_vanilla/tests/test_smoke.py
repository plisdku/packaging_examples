"""
Make sure it works.
"""

import nativepkg
import pythonpkg
    
def test_smoke():
    print("Smoke test!")
    print(pythonpkg.say_hello())
    print(nativepkg.add(1,2))
    print("Done!")
