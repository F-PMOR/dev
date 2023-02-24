<!-- vscode-markdown-toc -->
* 1. [tested on](#testedon)
* 2. [configuration](#configuration)
* 3. [usage](#usage)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

--------------

# sortfile

##  1. <a name='testedon'></a>tested on
- Windows10
should work on linux too.

##  2. <a name='configuration'></a>configuration

1. Change the SORTDIR with the name of the directory you want to sort the file in.
You have to use the pathlib syntaxe.
 - exemple on windows : SORTDIR = HOMEDIR / "Download" / "test" -> c:\Users\username\Downloads\test
 - exemple on linux : SORTDIR = HOMEDIR / "Download" / "test" -> /home/username/Downloads/test

2. you can change the behavior of the script by adding or replacing the FILETYPE dictionnary. (this one is a french one)

##  3. <a name='usage'></a>usage

just call the script.

```
python3 sortfile.py  
```
or  
```
chmod sortfile.py  
./sortfile.py
```