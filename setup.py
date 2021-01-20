import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
from cx_Freeze.samples.distutils.setup import buildOptions
from setuptools import glob

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "BotMHI",
        version = "0.1",
        description = "BotMHI!",
        executables=[Executable(i) for i in glob.glob('mhiv2.py')],
        options=dict(build_exe=buildOptions),
        )
        # options = {"build_exe": build_exe_options},
        # executables = [Executable("main.py", base=base)])