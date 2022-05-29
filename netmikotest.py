import yaml
import sys
import time
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

my_devices = ['10.10.20.17', '10.10.20.18', '10.10.20.19'] #list of devices
device_list = list() #create an empty list to use it later

for device_ip in my_devices:
    device = {
        "device_type": "cisco_ios",
        "host": device_ip,
        "username": "cisco",
        "password": passwd, # Log in password from getpass
        "secret": passwd # Enable password from getpass
