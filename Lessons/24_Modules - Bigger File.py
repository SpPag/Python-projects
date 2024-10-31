'''
We may have defined some functions or created some variables in a file, that we want to use in another file. "Tutorial
guys"'s example was having coded a function to roll a die that he decided he wanted to use in a later file. I have
copied that code in the "Modules - Tools File" file. I can either go to that file and copy the code that I want to use
here (but that would be especially cumbersome if I were to need code from say 10 different files) or I can "import"
the file to this file.
'''

import z_Roll_dice
# Let's roll a d20
print(Roll_dice.roll_dice(20))

'''
Ok so I want to point something important out. We can get modules from other files we have created and written 
ourselves, yes. But we can also get them online. Google "list of python modules" and open the list (on the website
"docs.python.org for the version of Python we have installed. We can find that by going to the terminal inside PyCharm
(ether by ALT + F12 or by going to "View" -> "Tool Windows" -> "Terminal") and typing "python --version" or "python -V".
There are a ton of modules available there, all with their short descriptions as well as detailed explanations of how
they work once you click their links. I believe that all of those are inherently inside our Python installation, some
as structured "External Libraries" (which we can find inside the menu on the left side of PyCharm called "External
Libraries" and then going into the "Lib" folder as a file) or as just code inside Python.
Aside from the modules found on docs.python.org though, there are a myriad more developed by the Python community. You
can just google "Python module for doing *this*" and you have a good chance to find a module to do the thing you want
to do. A good idea might be to look up generally useful Python modules and maybe install those. Anyway, an important
thing to note here is the program "pip". It's a package manager that let's us manage modules. We install modules
through it, usually utilizing commands like "pip install blah". In order to uninstall a module we would use a very
similar command, like "pip uninstall blah". Tutorial guy said that Python 3 comes with pip preinstalled. We can check
if we have "pip" preinstalled the same way as we checked for our Python version. ALT + F12 to open the terminal and type
in "pip --version" or "pip -V". I can see that I do indeed have pip preinstalled. When we install a third party module,
it goes into the folder at "External Libraries" -> "Lib" -> "Site Packages".
'''
