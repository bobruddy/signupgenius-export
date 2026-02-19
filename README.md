# SignUpGenius Export Tool

This tool allows you to export signup data from SignUpGenius to a CSV file.

## Prerequisites

- SignUpGenius Premium account
- API key from your SignUpGenius account (found in Pro Tools > API Management)

## Installation

1. Clone or download this repository.
2. Install the package: `pip install .`
3. Or for development: `pip install -e .`
4. For isolated installation: `pipx install .` (recommended for production)

If you get "externally-managed-environment" error, use:
```bash
pip install --user .
# or
pipx install .
```

## Usage

### Set API key (recommended for security)
```bash
export SIGNUPGENIUS_API_KEY=your_api_key_here
```

### List available signups
```bash
signupgenius-export --list
```

### Export a specific signup
```bash
signupgenius-export "<signup_name>" <output_file>
```

Or without env var:
```bash
signupgenius-export <api_key> "<signup_name>" <output_file>
```

- `signup_name`: The exact title of the signup to export (use quotes if it contains spaces)
- `output_file`: Path to the output CSV file

## What it does

1. Fetches all your created signups
2. Finds the signup matching the provided name
3. Downloads the full report data (all signups, including past dates)
4. Saves the data to a CSV file with all available fields

## Cron Setup

To run automatically from cron, set the API key in your crontab:

```bash
# Edit crontab
crontab -e

# Add line like (runs daily at 2 AM):
0 2 * * * SIGNUPGENIUS_API_KEY=your_api_key_here signupgenius-export "Your Signup Name" /path/to/output.csv
```

Or create a script:

```bash
#!/bin/bash
export SIGNUPGENIUS_API_KEY=your_api_key_here
signupgenius-export "Your Signup Name" /path/to/output.csv
```

Make it executable and add to cron:
```bash
chmod +x /path/to/export_script.sh
# In crontab:
0 2 * * * /path/to/export_script.sh
```

## Notes

- The script exports all fields available in the API response.
- Make sure the signup name matches exactly (case-sensitive).
- For large signups, the API may have rate limits; premium accounts have higher limits.