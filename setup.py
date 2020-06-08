from cx_Freeze import setup, Executable
import sys

sys.argv.append("build")
base = None    

executables = [Executable("main.py", base=base)]

packages = ["requests", "pandas", "bs4", "pyrebase", "httplib2", "oauth2client"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Web Scraper",
    options = options,
    version = "1.0",
    description = '',
    executables = executables
)