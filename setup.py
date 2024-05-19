import sys
import os
from cx_Freeze import setup, Executable

# Add the 'src' directory to the PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

build_exe_options = {
    "include_files": [
        ("src/uploads", "src/uploads"),
        ("C:/Windows/System32/vcomp140.dll", "vcomp140.dll"),
        ("C:/Windows/System32/msvcp140.dll", "msvcp140.dll"),
        ("src/functions", "src/functions"),
        ("src/images", "src/images"),
        ("src/interface", "src/interface"),
        ("src/modules", "src/modules"),
        ("src/scripts", "src/scripts"),
        ("src/uploads", "src/uploads"),
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
