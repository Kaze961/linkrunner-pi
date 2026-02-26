import psutil
import socket

def get_port_data():
    interface = "end0"
    
    # DHCP-Info
    stats = psutil.net_if_stats()[interface]
    addrs = psutil.net_if_addrs()[interface]
    ipv4_addresses = [a.address for a in addrs if a.family == socket.AF_INET]
    my_ip = ipv4_addresses[0] if ipv4_addresses else "Keine IP"

    # Get Gateway-Info
    with open("/proc/net/route") as f:
        lines = f.readlines()
        gw_hex = lines[1].split()[2]
        gw_ip = socket.inet_ntoa(int(gw_hex, 16).to_bytes(4, 'little'))

    # Output
    print(f"Interface: {interface} | Speed: {stats.speed}Mbit | Link: {'YES' if stats.isup else 'NO'}")
    print(f"My-IP: {my_ip}")
    print(f"Connected to: {gw_ip}")

if __name__ == "__main__":
    get_port_data()