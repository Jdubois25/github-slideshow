Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> Name = "Jack"
>>> Name.swapcase()
'jACK'
>>> Name.srip()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Name.srip()
AttributeError: 'str' object has no attribute 'srip'
>>> Color_1 = ' red '
>>> Color_2 = '
SyntaxError: EOL while scanning string literal
>>> Color_2 = '       blue      '
>>> print('My favorite colors are ' + Color_1 + 'and' + Color_2)
My favorite colors are  red and       blue      
>>> print('Let\'s fix the formatting...')
Let's fix the formatting...
>>> print('My favorite colors are ' + Color_1.strip() + 'and ' + Color_2.strip())
My favorite colors are redand blue
>>> print('My favorite colors are ' + Color_1.strip() + ' and ' + Color_2.strip())
My favorite colors are red and blue
>>> [HKEY_CLASSES_ROOT\Applications\powershell.exe\shell\open\command]

@=”\ ”C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe\” –noExit \ “& \\\ “%1\\\ ”\””

[HKEY_CLASSES_ROOT\Microsoft.PowerShellScript.1\Shell\0\Command]

@=”\ “C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe\ “ –NoExit \ “-Command\” \”if ( ( Get-ExecutionPolicy ) –ne ‘AllSigned’) { Set-ExecutionPolicy –Scope Process Bypass }; & \\\ ”%1” \\\ “\””
SyntaxError: unexpected character after line continuation character
>>> 