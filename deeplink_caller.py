#!/usr/bin/env python3
"""
Facebook Deeplink Caller Utility
Easily launch any Facebook Katana Deeplink on a connected Android device via ADB.
"""
import sys
import subprocess
import argparse

def launch_deeplink(uri, device_id=None):
    cmd = ["adb"]
    if device_id:
        cmd.extend(["-s", device_id])
    cmd.extend(["shell", "am", "start", "-a", "android.intent.action.VIEW", "-d", uri])
    
    print(f"[+] Executing: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print("[✓] Successfully launched intent!")
        if res.stdout.strip():
            print(res.stdout.strip())
    else:
        print(f"[✗] Error: {res.stderr.strip()}")

def main():
    parser = argparse.ArgumentParser(description="Launch Facebook Deeplinks via ADB")
    parser.add_argument("uri", help="Facebook Deeplink URI (e.g. fb://marketplace)")
    parser.add_argument("-s", "--serial", help="Target ADB device serial")
    args = parser.parse_args()

    launch_deeplink(args.uri, args.serial)

if __name__ == "__main__":
    main()
