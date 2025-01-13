# network-scanner
A Python-based ARP network scanner that identifies active devices within a specified IP range. This tool uses the Scapy library to send ARP requests, broadcast them across the local network, and retrieve responses from connected devices. It outputs a list of active devices with their IP and MAC addresses.

# Output Description for network_scan.py
This script scans the local network to find active hosts. The output provides details about:

IP Address: The local machine's IP address used during the scan.
Active Hosts: A list of devices on the local network, including their IP addresses and device names (if available).
Scanning Duration: The time taken to complete the network scan.
