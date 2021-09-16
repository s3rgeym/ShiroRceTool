#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
File:   :   ShiroRceTools.py
Time    :   2021/09/16 09:39:23
Author  :   Hack3rHan
Contact :   Hack3rHan@protonmail.com
"""
import argparse

from core.Checker import Checker
from core.Exploit import Exploit


banner = r"""
 ____  _     _           ____         _____           _     
/ ___|| |__ (_)_ __ ___ |  _ \ ___ __|_   _|__   ___ | |
\___ \| '_ \| | '__/ _ \| |_) / __/ _ \| |/ _ \ / _ \| |
 ___) | | | | | | | (_) |  _ < (_|  __/| | (_) | (_) | |
|____/|_| |_|_|_|  \___/|_| \_\___\___||_|\___/ \___/|_|
                        
                        By: Hack3rHan
"""


if __name__ == '__main__':
    print(banner)

    parse = argparse.ArgumentParser()
    parse.add_argument('-m', '--mode', help='exploit or check', action='store')
    parse.add_argument('-u', '--url', help='URL of the target.', action='store')
    parse.add_argument('-c', '--cmd', help='Command to execute.', action='store')
    parse.add_argument('-e', '--echo', help='Echo Command.', action='store_true')
    

    options = parse.parse_args()

    if options.mode == 'exploit':
        exp = Exploit(url=options.url, cmd=options.cmd, echo=options.echo)
        exp.run()
    elif options.mode == 'check':
        checker = Checker(url=options.url, is_tomcat=True)
        checker.run()
    else:
        parse.print_help()