#!/usr/bin/python3
###  */30 * * * * python /usr/local/bin/restart.py
from datetime import datetime
import subprocess
import sys

def main():
        service_status()

def service_status():
        status_mariadb = subprocess.call(["systemctl", "is-active", "--quiet", "mariadb"])
        status_httpd = subprocess.call(["systemctl", "is-active", "--quiet", "httpd"])
        if status_mariadb != 0:
                subprocess.call(["systemctl", "start", "mariadb"])
                srvc = "mariadb"
                add_to_log(srvc)
        if status_httpd != 0:
                subprocess.call(["systemctl", "start", "httpd"])
                srvc = "httpd"
                add_to_log(srvc)
def add_to_log(srvc):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f = open("/var/log/tekyhost.log", "a")
        f.write(" " + '\n')
        f.write(current_time + '\n')
        f.write(srvc + " service restarted" + '\n')
        f.write("-------------------------" + '\n')
        f.write(" " + '\n')
        f.close()

if __name__=="__main__":
        main()
