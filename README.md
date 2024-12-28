# System Status & Update Script 

This script checks and displays various system information on a Debian-based system including:

* **ExpressVPN Status:** Checks if ExpressVPN is connected.
* **Network Port Scan:** Performs a basic nmap scan of localhost (or a specified target).
* **Battery Health:** Checks the battery level and charging status.
* **System Updates:** Prompts the user to perform system updates using 'apt'.

## Prerequisites

* **Python 3.x:** Make sure you have Python 3 installed on your system.
* **Required Packages:**  `psutil` (install with `pip install psutil`)
* **ExpressVPN (Optional):** If you want to use the ExpressVPN status check, make sure ExpressVPN is installed.
* **nmap (Optional):**  Install nmap (`sudo apt install nmap`) for the port scanning functionality.

## How to Use

1. **Clone the repository:** `git clone <repository_url>`
2. **Install required packages:** `pip install psutil`
3. **Make the script executable:** ` chmod +x system_status.py`  
4. **Run the script:** `./system_status.py`

You can create and alias in the ~/.bashrc: 
`sudo nano ~/.bashrc`
And add a line at the bottom of the page: 
`alias sys_stat=python3 <path/to/script>`


The script will display the gathered system information and prompt you to confirm if you want to proceed with system updates. If you choose to proceed with updates, you'll be prompted for your sudo password by the system.

## Disclaimer

* Use this script at your own risk.
* This script is provided as-is and should be used responsibly. Make sure you understand the implications of running commands like `nmap` and `sudo apt update/upgrade` on your system. 
* Ensure you have proper backups before running system updates.
* This script is intended for Debian-based systems. It may not work on other Linux distributions.
