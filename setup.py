from cx_Freeze import setup, Executable

build_exe_options = {
    "excludes": ["tkinter", "unittest"],
    "zip_include_packages": ["matplotlib", "numpy", "PyQt5", "markdown", "pandas", "scikit-learn", "openpyxl"],
}
# options = {
#     'build_exe': {
#         'packages': ['package1', 'package2'],  # Python packages that should be included
#         'include_files': ['data_file1', 'data_file2'],  # Non-Python files that should be included
#     },
# }


setup(
    name="Kraken",
    version="0.7.7",
    description="Program that helps with pressure and temperature analysis!",
    author="André Albano",  # Add your name here
    author_email="geof.aalbano@gmail.com",  # Add your email here
    options={"build_exe": build_exe_options},
    url="http://albano-dev.netlify.app",  # Add your website or project URL here
    executables=[Executable("src/kraken.py", base="gui", icon="src/icon.ico")],
)
