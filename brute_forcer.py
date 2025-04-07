def run(target, wordlist_file):
    print(f"[+] Starting brute-force on {target} using {wordlist_file}\n")

    try:
        with open(wordlist_file, 'r') as file:
            passwords = file.read().splitlines()
    except FileNotFoundError:
        print(f"[ERROR] Wordlist file '{wordlist_file}' not found.")
        return

    for pwd in passwords:
        print(f"Trying password: {pwd}")
        if pwd == "admin123":
            print(f"[SUCCESS] Password found: {pwd}")
            break
    else:
        print("[FAILURE] No valid password found.")
