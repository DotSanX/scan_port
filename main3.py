import socket


def scan_ports(target_host, port_list):
    print(f"Scanning {target_host} for open ports...")

    for port in port_list:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((target_host, port))

            if result == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")

            sock.close()

        except socket.error:
            print(f"Could not connect to port {port}")

    print("Scan complete")

target_host = "127.0.0.1"
port_list = [22, 80, 5432]

scan_ports(target_host, port_list)