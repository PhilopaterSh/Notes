# Author    : Ph.sh (Philopater Shenouda)
# Version   : 1
# Updated   : 2025-08-24
# LinkedIn  : https://www.linkedin.com/in/philopater-shenouda/
# VirusTotal Domain Link Generator (with pyfiglet banner + error handling + confirmation)

import sys

# --- Banner ---
def show_ascii_art():
    print("""
 _____   _        _____ _     
 |  __ \| |      / ____| |    
 | |__) | |__   | (___ | |__  
 |  ___/| '_ \   \___ \| '_ \ 
 | |    | | | |_ ____) | | | |
 |_|    |_| |_(_)_____/|_| |_|
                              
                              """)

show_ascii_art()

# 1- Ask the user for API Key
api_key = input("Enter your VirusTotal API Key: ").strip()
if not api_key:
    print("❌ Error: API Key cannot be empty!")
    sys.exit(1)

# 2- Ask for domain input method
choice = input("Do you want to (1) enter domains manually or (2) load from a file? Choose 1 or 2: ").strip()

domains = []

if choice == "1":
    print("Enter domains (one per line). Press Enter twice when done:")
    while True:
        d = input().strip()
        if d == "":
            break
        domains.append(d)

elif choice == "2":
    filepath = input("Enter the file path containing the domains: ").strip()
    try:
        with open(filepath, "r") as f:
            domains = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ Error: File '{filepath}' not found!")
        sys.exit(1)

else:
    print("❌ Error: Invalid choice! Please enter 1 or 2.")
    sys.exit(1)

# Validate domains
if not domains:
    print("❌ Error: No domains were provided!")
    sys.exit(1)

# 3- Build the links
links = []
for domain in domains:
    url = f"https://www.virustotal.com/vtapi/v2/domain/report?apikey={api_key}&domain={domain}&authuser=0"
    links.append(url)

# 4- Ask user for output filename (manual only)
filename = input("Enter output filename (example: results.txt): ").strip()
if not filename:
    print("❌ Error: Filename cannot be empty!")
    sys.exit(1)
if not filename.endswith(".txt"):
    filename += ".txt"

# 5- Show preview and ask for confirmation
print("\nPreview of generated links:")
for link in links[:5]:  # show only first 5 to avoid flooding
    print(link)
if len(links) > 5:
    print(f"... and {len(links) - 5} more links")

confirm = input(f"\nDo you want to save these links to '{filename}'? (y/n): ").strip().lower()
if confirm != "y":
    print("❌ Operation cancelled by user.")
    sys.exit(0)

# 6- Save all links to TXT
try:
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(links))
    print(f"✅ {len(links)} links saved to: {filename}")
except Exception as e:
    print(f"❌ Error saving file: {e}")
    sys.exit(1)
