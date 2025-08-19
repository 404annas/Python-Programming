# print('''When you run pip install pyjokes, the message says "Requirement already satisfied". This means the pyjokes module is already installed on your system, so pip doesn’t download it again. The “Defaulting to user installation” line just shows that it was installed in your user’s local directory. This is normal and not an error.

# To confirm it works, you can open Python by typing python in your terminal. Once inside, try importing the module using import pyjokes. Then run print(pyjokes.get_joke()) to see if it prints a random joke. If a joke is displayed, the installation is successful.

# Sometimes, the problem is having multiple versions of Python on your computer. Pip might install pyjokes for one version, while you run another version where it isn’t installed. To fix this, use python -m pip install pyjokes so pip installs into the exact Python version you are running.

# If you are using an IDE like PyCharm or VS Code, make sure it uses the same Python interpreter where pyjokes is installed. Otherwise, you’ll get a “module not found” error even if the package is installed. Matching the pip environment with your Python interpreter solves this issue.''')

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Kesa hey beyh bhai")
# engine.runAndWait()

import os;

directory_path = "/"

contents_path = os.listdir(directory_path)
# print(contents_path)
for items in contents_path:
    print(items)