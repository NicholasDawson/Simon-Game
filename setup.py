from cx_Freeze import setup, Executable

target = Executable(
    script="main.py",
    base="Win32GUI",
    targetName = 'Simon.exe',
    icon="simon_icon.ico"
    )

setup(
    name="Simon",
    version="0.1.0",
    description="A clone of the popular electronic game Simon.",
    author="Nicholas Dawson",
    executables=[target]
    )
