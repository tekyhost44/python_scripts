#!/usr/bin/python3

import subprocess
import sys

def main():
        service_status()

def service_status():
        status_mariadb = subprocess.call(["systemctl", "is-active", "--quiet", "mariadb"])
        status_httpd = subprocess.call(["systemctl", "is-active", "--quiet", "httpd"])
        if status_mariadb != 0:
                subprocess.call(["systemctl", "start", "mariadb"])
        if status_httpd != 0:
                subprocess.call(["systemctl", "start", "httpd"])

if __name__=="__main__":
        main()
