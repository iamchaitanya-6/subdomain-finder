import socket
from concurrent.futures import ThreadPoolExecutor

def resolve_subdomain(sub, domain):
    subdomain = f"{sub}.{domain}"
    try:
        ip = socket.gethostbyname(subdomain)
        print(f"[+] Found: {subdomain} --> {ip}")
        return (subdomain, ip)
    except socket.gaierror:
        return None

def scan_subdomains(domain, wordlist_file="list.txt", threads=50):
    found = []
    with open(wordlist_file, "r") as f:
        words = [line.strip() for line in f if line.strip()]

    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(lambda sub: resolve_subdomain(sub, domain), words)
        for res in results:
            if res:
                found.append(res)
    return found

if __name__ == "__main__":
    print("=== Subdomain & IP Scanner ===")
    domain = input("👉 Enter target domain (e.g. example.com): ").strip()
    
    wordlist_file = "list.txt"  

    print(f"\n[*] Scanning {domain} using {wordlist_file}...\n")
    results = scan_subdomains(domain, wordlist_file)

    if results:
        print("\n=== Found Subdomains and IPs ===")
        for subdomain, ip in results:
            print(f"{subdomain} --> {ip}")
    else:
        print("[-] No subdomains found.")
