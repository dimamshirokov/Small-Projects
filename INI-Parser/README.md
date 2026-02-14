<h1 align='center'> INI-Parser </h1>

___

## 🌀 Description

The project is a simple parser of INI format files.

### 👋 Introduction

INI files are plain text files that can be edited and viewed with any text editor. INI files have gained popularity in Windows, although they can be used in any OS. The uncomplicated structure of this format allows them to be easily processed programmatically and has a clear enough appearance for human reading and modification.

### 📄 INI-files format

INI-files can contain types of strings:

Section name string - denotes the name of a new section of variables. It has the format: [section_name].
Spaces and tab characters before opening and after closing brackets are ignored.

Variable assignment string - specifies the value of the variable. It has the format: variable_name = variable_value.
The number of spaces between equality characters can be arbitrary. For simplicity, we will assume that values can be either a string or a number. Multiple values are not allowed.

Comment string. It has the format: ; comment string.
The parser should ignore such strings, nothing should be done with them.

### 🏗️ General structure of INI-file

Example of INI-file structure:

```INI
[Section1]
; section comment
var1=5.0 ; sometimes it is allowed to comment on a single parameter
var2=some string
  
[Section2]
var1=1
var2=value_2

; Sometimes there are no values, this means that there are no variables in Section3 
[Section3]
[Section4]
Mode=
Vid=

; Sections may be repeated
[Section1]
var3=value
var1=1.0 ; reassign value
```

## 👟 Run the program

In the folder /Small-Projects/INI-Parser/src, run the commands below.

```console
make run # Starts the program
```
```console
make clean # Clean the assembly after program execution
```

## 🎓 Author 

**Dima M. Shirokov**
- [GitHub](https://github.com/dimamshirokov)