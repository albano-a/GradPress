import sys
import os
import requests
from cx_Freeze import setup, Executable

# Add the 'src' directory to the PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

build_exe_options = {
    "packages": ["os", "requests", "sklearn"],  # Include necessary packages
    "include_files": [
        ("src/uploads", "uploads"),
        ("C:/Windows/SysWOW64/vcomp140.dll", "vcomp140.dll"),
        ("C:/Windows/SysWOW64/msvcp140.dll", "msvcp140.dll"),
        ("src/functions", "functions"),
        ("src/images", "images"),
        ("src/interface", "interface"),
        ("src/modules", "modules"),
        ("src/scripts", "scripts"),
        "LICENSE",
    ],
}
setup(
    name="Kraken",
    version="0.7.7",
    description="Program that helps with pressure and temperature analysis!",
    author="André Albano",  # Add your name here
    author_email="geof.aalbano@gmail.com",  # Add your email here
    options={"build_exe": build_exe_options},
    url="http://albano-dev.netlify.app",  # Add your website or project URL here
    executables=[Executable("src/kraken.py", base="Win32GUI", icon="src/icon.ico")],
)
