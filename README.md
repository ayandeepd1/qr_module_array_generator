# qr_module_array_generator
generate qr code image and array consisting of qr code modules through command line

Example(windows):  
python txpr.py \<data\> \<version\>

tool generates: 
image file->out.png   
text file->out.txt

example to run on windows is provided as a .cmd file

For more information on valid \<data\> and \<version\> fields check segno library:
https://segno.readthedocs.io/en/latest/make.html#qr-code-version

requirements:
1. Python3
2. Segno
3. Internet connection if segno not installed, script auto installs segno
