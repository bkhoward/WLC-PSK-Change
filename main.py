#!/usr/bin/env python
#
#  Author:   Brian Howard
#  Date:     02Feb2021
#  Version:  1.0
#  Abstract: Create SSH connection to corporate Cisco WLCs and change the PSK used for ONEguest SSID
#            - Find the WLAN_ID for the ONEguest SSID
#            - Disable the WLAN_ID for ONEguest
#            - Modify the existing PSK for the ONEguest SSID
#            - Re-Enable the WLAN_ID for ONEguest
#            - Save the config
#            - Create logfiles for all SSH transactions
#
#  Source Files:
#           main.py - main python script
#           credentials.py - file to store login credentials
#           ios_wlan_id-finder.py - logs into an ios host and finds the WLAN_ID associated with the ONEguest SSID
#           aireos_wlan_id-finder.py - logs into an aireos host and finds the WLAN_ID associated with the ONEguest SSID
#           host_file.py - python list containing ip addresses of Cisco WLCs
#           cmd_file.py - python list containing Cisco commands to run within the script
#                   Note: 'show run | include hostname' must be element 0
#
#  Output Files:
#           log.txt - log file containing all information from the SSH channel.
#                     This is an all inclusive file for all hosts connected to
#           {hostname}.txt - each host connected to has an individual log file of commands only.
#                            this log is not as detailed as the log.txt file.
# ------------------------------------------------------------------------------------------------#

# ------------------------------------------------------------------------------------------------#
# Function definitions
# ------------------------------------------------------------------------------------------------#

import logging
import coloredlogs
from netmiko import ConnectHandler
from ntc_templates.parse import parse_output
from host_file import host
from credentials import credentials
from cmd_file import cmd
from pprint import pprint

##### Begin Logging section #####
# Basic logging allows Netmiko detailed logging of the ssh stream written to a file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger('Netmiko')

# Create a console handler object for the console Stream
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# # Create a ColoredFormatter to use as formatter for the Console Handler
formatter = coloredlogs.ColoredFormatter(fmt='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
ch.setFormatter(formatter)
# assign console handler to logger
logger.addHandler(ch)
# ##### End Logging section #####


if __name__ == '__main__':
    # Capture new PSK
    print()
    PSK = input("Please enter New PSK: ")
    print()

    for wlc in host:
        logfile = wlc['hostname'] + '.log'

        # Netmiko SSH connection
        ssh_connect = ConnectHandler(ip=wlc['ip'], username=credentials['username'], password=credentials['password'],
                                     device_type=wlc['device_type'], session_log=logfile)
        # Netmiko connection sends show command
        # use_textfsm automatically looks in the \venv\Lib\site-packages\ntc_templates\templates directory
        # for a template matching the device type + command name to convert the unstructured output of the show
        # command to structured data (list of dictionaries)
        # Note: ntc_templates and fsmtext are automatically installed with Netmiko
        show_wlan_raw = ssh_connect.send_command(cmd['get_wlan'])
        show_wlan = parse_output(platform=wlc['device_type'], command="show wlan sum", data=show_wlan_raw)

        for wlan in show_wlan:

            if wlan['ssid'] == 'ONEguest':
                print()
                print('*******************************************************************************')
                print()
                # Connect to host and Show current state of WLANs
                logger.critical('Connecting to ' + wlc['hostname'])
                logger.warning(ssh_connect.send_command(cmd['get_wlan']))

                # Disable ONEguest WLAN and Show current state of WLANs
                logger.critical('Disabling WLAN on ' + wlan['ssid'] + ' for WLAN-ID: ' + wlan['wlanid'])
                if wlc['device_type'] == 'cisco_wlc_ssh':
                    ssh_connect.send_command(cmd['aireos_wlan_disable'] + ' ' + wlan['wlanid'])
                    logger.warning(ssh_connect.send_command(cmd['get_wlan']))
                    print()
                else:
                    # change to wlan profile sub menu for ONEguest SSID and shutdown SSID
                    # send_config_set automatically enters config mode, executes a list of commands,
                    # then exits config mode. Note if only one command is in the list it does not stay in config mode
                    ssh_connect.send_config_set(['wlan ' + wlan['profile'], cmd['ios_shutdown']])
                    logger.warning(ssh_connect.send_command(cmd['get_wlan']))
                    print()

                # Change PSK
                logger.critical('Changing PSK on ' + wlc['hostname'] + ' for WLAN-ID: ' + wlan['wlanid'])
                if wlc['device_type'] == 'cisco_wlc_ssh':
                    ssh_connect.send_command(cmd['aireos_psk'] + ' ' + PSK + ' ' + wlan['wlanid'])
                    logger.warning('New PSK is: ' + PSK)
                    print()

                else:
                    ssh_connect.enable()
                    # change to wlan profile sub menu for ONEguest SSID and chnage PSK
                    ssh_connect.send_config_set(['wlan ' + wlan['profile'], cmd['ios_psk'] + ' ' + PSK])
                    logger.warning('New PSK is: ' + PSK)
                    print()


                # Enable ONEguest WLAN and Show current state of WLANs
                logger.critical('Enabling WLAN on ' + wlan['ssid'] + ' for WLAN-ID: ' + wlan['wlanid'])
                if wlc['device_type'] == 'cisco_wlc_ssh':
                    ssh_connect.send_command(cmd['aireos_wlan_enable'] + ' ' + wlan['wlanid'])
                    logger.warning(ssh_connect.send_command(cmd['get_wlan']))
                    print()
                else:
                    ssh_connect.enable()
                    # change to wlan profile sub menu for ONEguest SSID and enable it
                    ssh_connect.send_config_set(['wlan ' + wlan['profile'], cmd['ios_no_shutdown']])
                    logger.warning(ssh_connect.send_command(cmd['get_wlan']))
                    print()

                # Save Config
                logger.critical('Saving Config on host: ' + wlc['hostname'])
                if wlc['device_type'] == 'cisco_wlc_ssh':
                    ssh_connect.save_config(cmd['aireos_save'], confirm_response='y')
                    print()
                    print('*******************************************************************************')
                    print()
                else:
                    ssh_connect.save_config()
                    print()
                    print('*******************************************************************************')
                    print()

        ssh_connect.disconnect()


