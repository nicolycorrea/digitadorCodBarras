import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter", "pdf2image", "pyzbar", "pyautogui", "threading", "time"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Digitador CodBarras",
    version="0.1",
    description="Digitador automático de Código de Barras",
    options={"build_exe": build_exe_options},
    executables=[Executable("digitadorCodBarras.py", base=base)]
)