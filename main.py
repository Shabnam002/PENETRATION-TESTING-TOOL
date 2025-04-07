import argparse
from modules import port_scanner, brute_forcer

def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")
    parser.add_argument("-m", "--module", help="Select a module: port_scan, brute_force")
    parser.add_argument("-t", "--target", help="Target IP or URL")
    parser.add_argument("-w", "--wordlist", help="Wordlist file (for brute-force)")

    args = parser.parse_args()

    if args.module == "port_scan":
        print("[DEBUG] Running port scan module...")
        port_scanner.scan(args.target)

    elif args.module == "brute_force":
        print("[DEBUG] Running brute-force module...")
        if args.wordlist:
            brute_forcer.run(args.target, args.wordlist)
        else:
            print("Please provide a wordlist file with -w")

    else:
        print("Invalid module. Use: port_scan, brute_force")

if __name__ == "__main__":
    main()
