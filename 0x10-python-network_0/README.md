And this is the content of the README.md file:
```
cat README.md
```
> # Python Network #0
>   Welcome!
>   This is your first network code
>   With the API it's not rocket science 
>   but it can intimidating at first
>   Don't quit, you'll do great!
>   ## Learning Objectives
>   At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
>   ## General
>   What a URL is
>   What HTTP is
>   How to read a URL
>   The scheme for a HTTP URL
>   What a domain name is
>   What a sub-domain is
>   How to define a port number in a URL
>   What a query string is
>   What an HTTP request is
>   What an HTTP response is
>   What HTTP headers are
>   What the HTTP message body is
>   What an HTTP request method is
>   What an HTTP response status code is
>   What an HTTP Cookie is
>   How to make a request with cURL
>   What happens when you type google.com in your browser (Application level)
>   Requirements
>   General
>   Allowed editors: vi, vim, emacs
>   - A README.md file, at the root of the folder of the project, is mandatory
>   - All your scripts will be tested on Ubuntu 14.04 LTS
>   - All your Bash scripts should be exactly 3 lines long (wc -l file should print 3)
>   - All your files should end with a new line
>   - All your files must be executable
>   - The first line of all your bash files should be exactly #!/bin/bash
>   - The second line of all your Bash scripts should be a comment explaining what is the script doing
>   - All curl commands must have the option -s (silent mode)
>   - All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
>   - The first line of all your Python files should be exactly #!/usr/bin/python3
>   - Your code should use the PEP 8 style (version 1.7.*)
>   - All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
>   - All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'

## Task 1
> Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
>   - A header variable X-HolbertonSchool-User-Id must be sent with the value 98
>   - You must use curl
```
./1-body.sh
```
> Hello Holberton School!
```
cat 1-body.sh
```
> #!/bin/bash
>   # Script that takes in a URL, sends a GET request to the URL, and displays the body of the response
>   curl -sL "$1"
## Task 2
> Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
```
./2-delete.sh
```
> I got the DELETE request!
```
cat 2-delete.sh
```
> #!/bin/bash
>   # Script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
>   curl -sX DELETE "$1"
## Task 3
> Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
```
./3-methods.sh
```
> OPTIONS, HEAD, PUT
```
cat 3-methods.sh
```
> #!/bin/bash
>   # Script that takes in a URL and displays all HTTP methods the server will accept.
>   curl -sI "$1" | grep Allow | cut -d " " -f2-
