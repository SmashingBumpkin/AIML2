# AIML2
 Work from AI & ML course

For the packages used on the course:
download and install python 3.8 64 bit:
https://www.python.org/downloads/release/python-380/
create directory
open cmd/powershell, navigate to directory and run:
virtualenv --python="C:\Users\Charl\AppData\Local\Programs\Python\Python38\python.exe" python38  (edit this to your python 3.8 path)
Activate the virtual environment (do this whenever working on stuff for this course in python) python38\Scripts\activate.ps1 (.bat in cmd)
pip install numpy
pip install matplotlib
pip install -U scikit-learn
(If it doesn't work because:
      The following exception(s) were encountered:
      Running `ifort --version` gave "[WinError 2] The system cannot find the file specified"
      Running `ifort -V` gave "[WinError 2] The system cannot find the file specified"
      Running `gfortran --version` gave "[WinError 2] The system cannot find the file specified"
      ...etc
You need a fortran compiler. Try installing MinGW 8.1: https://sourceforge.net/projects/mingw-w64/files/
When installing mingw, you only need the mingw32-gcc-fortran package
Restart CMD, if it doesn't work add "[install location]\MinGW\bin" to your PATH environment variable

And for the thing he uses to make the course's slides:
pip install traitlets==5.9.0
pip install notebook==6.4.12
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
