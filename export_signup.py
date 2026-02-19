
#!/usr/bin/env python3
"""
Script to export SignUpGenius signup data to CSV.

Copyright (C) 2026  [Your Name]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import requests
import csv
import sys
import argparse

import os

BASE_URL = "https://api.signupgenius.com/v2/k"

def list_signups(api_key):
    url = f"{BASE_URL}/signups/created/all/?user_key={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    signups = data.get('data', [])
    if not signups:
        print("No signups found.")
        return
    
    print("Available signups:")
    for signup in signups:
        print(f"- {signup.get('title')} (ID: {signup.get('signupid')})")

def export_signup_report(api_key, signup_id, output_file):
    url = f"{BASE_URL}/signups/report/all/{signup_id}/?user_key={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    # The report data is under data['data']['signup']
    records = data.get('data', {}).get('signup', [])
    if not records:
        print("No data found for this signup.")
        return
    
    # Get field names from the first record
    fieldnames = records[0].keys()
    
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    
    print(f"Data exported to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Export SignUpGenius signup data to CSV")
    parser.add_argument("api_key", nargs="?", help="Your SignUpGenius API key (or set SIGNUPGENIUS_API_KEY env var)")
    parser.add_argument("--list", action="store_true", help="List all available signups and exit")
    parser.add_argument("signup_name", nargs="?", help="Name of the signup to export (required unless --list is used)")
    parser.add_argument("output_file", nargs="?", help="Output CSV file path (required unless --list is used)")
    
    args = parser.parse_args()
    
    api_key = args.api_key or os.getenv("SIGNUPGENIUS_API_KEY")
    if not api_key:
        parser.error("API key is required. Provide as argument or set SIGNUPGENIUS_API_KEY environment variable")
    
    if args.list:
        list_signups(api_key)
        return
    
    if not args.signup_name or not args.output_file:
        parser.error("signup_name and output_file are required unless --list is used")
    
    try:
        signup_id = get_signup_id(api_key, args.signup_name)
        export_signup_report(api_key, signup_id, args.output_file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()