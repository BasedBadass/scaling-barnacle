#!/usr/bin/env python3

"""
system_status.py

This script checks and displays various system information, 
including ExpressVPN status, network port scan results, battery health,
and performs system updates.

Date: December 28, 2024
"""


import subprocess
import psutil
import os

def get_expressvpn_status():
    """
    Checks ExpressVPN status using the 'expressvpn status' command.
    Returns a string indicating the connection status.
    """
    try:
        # Replace 'expressvpn' with the actual command used by your VPN client
        process = subprocess.run(['expressvpn', 'status'], capture_output=True, text=True)
        if "Connected" in process.stdout:
            return "ExpressVPN: Connected"
        else:
            return "ExpressVPN: Disconnected"
    except FileNotFoundError:
        return "ExpressVPN: Not installed or command not found"
    
def nmap_scan(target="localhost"):
    """
    Performs an nmap scan on the specified target.
    Uses -T4 for faster scan -F for a fast scan with limited port selection.
    Returns the output from nmap.
    """
    try:
        command = ["nmap", "-T4", "-F", target] 
        process = subprocess.run(command, capture_output=True, text=True)
        return process.stdout
    except FileNotFoundError:
        return "nmap: Command not found. Please install nmap."
    except Exception as e:
        return f"An error occured: {e}"

def get_battery_health():
    """
    Checks battery health using psutil.
    Returns a string indicating the battery status.
    """
    battery = psutil.sensors_battery()
    if battery.power_plugged:
        return "Battery is charging"
    if battery.percent < 30:
        return "Battery is running low"
    return "Battery is OK"

def perform_system_updates():
    """
    Prompts the user and performs system updates.
    Uses 'sudo apt update' and 'sudo apt full-upgrade -y' to update the system.
    Reads the sudo password from the SUDO_PASSWORD enviroment variable.
    """
    user = os.getlogin()
    answer = input(f"{user}: Would you like to perform System Updates? (yes/no) [yes]: ")
    if answer.lower() in ["", "y", "yes"]:
        try:
            # Run the update commands, prompting for password
            subprocess.run(['sudo', 'apt', 'update'], input=os.environ.get('SUDO_PASSWORD'), text=True, check=True) 
            subprocess.run(['sudo', 'apt', 'full-upgrade', '-y'], input=os.environ.get('SUDO_PASSWORD'), text=True, check=True)
            print("System updates complete.")
        except subprocess.CalledProcessError as e:
            print(f"Error updating system: {e}")
    else:
        print("System updates skipped.")


if __name__ == "__main__":
    print(nmap_scan()) 
    print(get_expressvpn_status())
    print(get_battery_health())
    print(perform_system_updates()) 
    print("Have a great day Colin! Remember to tell yourself: I can do it!!")
 
 ## The code above is a simple example of a system status checker. 
 ## It has four functions:  get_expressvpn_status() ,  port_scan() , 
 ## get_battery_health() and perform_system_updates() . 
