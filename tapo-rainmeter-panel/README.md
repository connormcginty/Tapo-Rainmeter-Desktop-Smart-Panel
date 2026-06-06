# Tapo Rainmeter Panel

A simple Windows/Rainmeter desktop control panel for TP-Link Tapo P100 smart plugs.

It uses Python to toggle plugs on/off and Rainmeter to display clickable desktop buttons with ON/OFF status.

## Features

- Toggle Tapo P100 plugs from the Windows desktop
- Rainmeter panel with status text
- Green ON / red OFF status indicators
- Silent execution with `pythonw.exe`
- Uses a separate config file so credentials and IPs are not stored in scripts

## Requirements

- Windows
- Python 3.12+
- Rainmeter
- Tapo P100 plugs
- Third-party control enabled in the Tapo app
- Static/reserved IPs for your plugs

## Install Python library

```powershell
pip install tapo
```

## Setup

1. Copy the `scripts` folder to:

```text
C:\TapoControl
```

2. Rename:

```text
config.example.json
```

to:

```text
config.json
```

3. Edit `config.json` with your own Tapo account and plug IPs.

Example:

```json
{
  "email": "your-tapo-email@example.com",
  "password": "your-tapo-password",
  "devices": {
    "officefan": "STATIC IP HERE",
    "officeleds": "STATIC IP HERE",
    "officelamp": "STATIC IP HERE"
  }
}
```

4. Test from PowerShell:

```powershell
cd C:\TapoControl
python tapo_toggle.py officefan
```

5. Copy the Rainmeter skin folder:

```text
rainmeter\TapoPanel
```

to:

```text
Documents\Rainmeter\Skins\TapoPanel
```

6. Refresh Rainmeter and load `TapoPanel.ini`.

## Notes

- This project uses local IPs, so reserve/static-assign your plug IPs in your router.
- If the buttons stop working, try toggling third-party control off/on in the Tapo app.
- `config.json` is ignored by Git so credentials are not uploaded accidentally.

## Safety

Do not commit your real `config.json`.
