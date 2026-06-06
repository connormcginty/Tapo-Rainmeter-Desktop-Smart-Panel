# Tapo Rainmeter Control Panel

A simple Windows desktop control panel for TP-Link Tapo P100 smart plugs using Python and Rainmeter.

It gives you clickable desktop buttons that can toggle your plugs on/off, with ON/OFF status shown inside the button.

## Features

* Toggle Tapo P100 plugs from your desktop
* Works with Rainmeter
* Silent operation using `pythonw.exe`
* Shows ON/OFF status
* Green = ON
* Red = OFF
* Uses local IP addresses
* No Google Home or browser window needed

## Requirements

* Windows
* Python 3.12+
* Rainmeter
* Tapo P100 smart plugs
* Tapo third-party control enabled

Install the Python Tapo library:

```powershell
pip install tapo
```

## Setup

### 1. Reserve static IP addresses

In your router settings, reserve a fixed IP for each Tapo plug.

Example:

```text
Office Fan  → 192.168.1.XXX
Office LEDs → 192.168.1.XXX
Office Lamp → 192.168.1.XXX
```

This stops the plugs changing IP address later.

### 2. Enable third-party control in the Tapo app

Open the Tapo app and make sure third-party compatibility/control is enabled.

If it is already enabled but the scripts do not work, toggle it OFF and back ON again.

### 3. Copy the project

Place the project folder somewhere simple, for example:

```text
C:\TapoControl
```

### 4. Create your config file

Copy:

```text
config.example.json
```

Rename the copy to:

```text
config.json
```

Edit `config.json` and add your own Tapo email, password, and plug IP addresses.

Do not upload `config.json` to GitHub.

### 5. Test the scripts

Open PowerShell:

```powershell
cd C:\TapoControl
python officefan_toggle.py
python officeleds_toggle.py
python officelamp_toggle.py
```

Each command should toggle the matching plug.

### 6. Install the Rainmeter skin

Copy the Rainmeter skin folder into:

```text
Documents\Rainmeter\Skins
```

Example:

```text
Documents\Rainmeter\Skins\TapoPanel\TapoPanel.ini
```

Then:

1. Open Rainmeter.
2. Click **Refresh all**.
3. Load `TapoPanel.ini`.

You should now see the desktop control panel.

## Silent mode

Rainmeter uses `pythonw.exe` so no command window appears when clicking a button.

Example:

```ini
LeftMouseUpAction=["C:\Users\YOURNAME\AppData\Local\Microsoft\WindowsApps\pythonw.exe" "C:\TapoControl\officefan_toggle.py"]
```

Change `YOURNAME` and paths if needed.

## Status display

Each toggle script writes an ON/OFF value to a status text file.

Example:

```text
officefan_status.txt
officeleds_status.txt
officelamp_status.txt
```

Rainmeter reads those files and changes the status colour:

```text
ON  = green
OFF = red
```

## Start with Windows

To start Rainmeter with Windows:

1. Press `Win + R`
2. Type:

```text
shell:startup
```

3. Add a shortcut to:

```text
C:\Program Files\Rainmeter\Rainmeter.exe
```

Rainmeter should remember and reload the panel automatically.

## Troubleshooting

If the buttons suddenly stop working:

1. Check the plug IP address.
2. Ping the plug.
3. Test the Python script directly.
4. Verify third-party control is enabled in the Tapo app.

## Firmware Updates

After a Tapo firmware update, local control may occasionally stop working even if **Third-Party Control** is still shown as enabled in the Tapo app.

Symptoms may include:

* Rainmeter buttons stop responding
* Python scripts fail to control the plug
* Status updates stop working

A common fix is:

1. Open the Tapo app.
2. Go to **Me → Third-Party Services** (wording may vary by app version).
3. Turn **Third-Party Control/Compatibility** OFF.
4. Wait a few seconds.
5. Turn it back ON.

This forces the plug and Tapo account to refresh third-party access permissions.

In testing, this immediately restored local control after a firmware update without requiring any changes to the Python scripts or Rainmeter configuration.

## Notes

This project uses an unofficial Python library for Tapo devices, so future TP-Link/Tapo updates could potentially break compatibility.

If issues occur after an update, the first thing to try is toggling Third-Party Control OFF and back ON in the Tapo app before making any changes to the scripts.
