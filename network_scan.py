from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    """
    Scans the network for active devices within the specified IP range.

    Args:
        ip_range (str): The IP range to scan, e.g., "192.168.1.0/24".
    
    Returns:
        list: A list of dictionaries containing IP and MAC addresses of discovered devices.
    """
    # Create an ARP request packet
    arp_request = ARP(pdst=ip_range)  # pdst: IP range to target

    # Create an Ethernet frame to encapsulate the ARP request
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast to all devices

    # Combine the Ethernet frame and ARP request
    packet = broadcast / arp_request

    # Send the packet
