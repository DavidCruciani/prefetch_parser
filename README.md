# prefetch-parser
A parser of Windows prefetch file.

This repo is strongly inspired from [prefetch2es](https://github.com/sumeshi/prefetch2es), I kept only the part that interest me.



## Usage

~~~bash
dacru:~/git/prefetch-parser/ $ python prefetch_parser.py -h
usage: prefetch_parser.py [-h] [-f PREFETCHFILE] [-o JSONFILE]

optional arguments:
  -h, --help            show this help message and exit
  -f PREFETCHFILE, --prefetchfile PREFETCHFILE
                        Windows Prefetch file.
  -o JSONFILE, --jsonfile JSONFILE
                        Output json file path. '-' will print command output on terminal.
~~~



