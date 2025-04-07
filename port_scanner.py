import socket

def scan(target):
    print(f"[+] Starting port scan on {target}...\n")
    for port in range(1, 11):
        print(f"Scanning port {port}...")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            sock.close()
        except Exception as e:
            print(f"[!] Error on port {port}: {e}")