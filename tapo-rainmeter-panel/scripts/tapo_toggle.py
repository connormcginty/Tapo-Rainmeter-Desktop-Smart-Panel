import asyncio
import json
import sys
from pathlib import Path

from tapo import ApiClient

BASE_DIR = Path(__file__).resolve().parent
CONFIG_FILE = BASE_DIR / "config.json"


def load_config():
    if not CONFIG_FILE.exists():
        raise FileNotFoundError(
            f"Missing {CONFIG_FILE}. Copy config.example.json to config.json and edit it."
        )

    with CONFIG_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_status(device_name, status):
    status_file = BASE_DIR / f"{device_name}_status.txt"
    status_file.write_text(status, encoding="utf-8")


async def toggle_device(device_name):
    config = load_config()

    email = config["email"]
    password = config["password"]
    devices = config["devices"]

    if device_name not in devices:
        available = ", ".join(devices.keys())
        raise ValueError(f"Unknown device '{device_name}'. Available devices: {available}")

    plug_ip = devices[device_name]

    client = ApiClient(email, password)
    plug = await client.p100(plug_ip)

    info = await plug.get_device_info()
    is_on = info.device_on

    if is_on:
        await plug.off()
        new_status = "OFF"
    else:
        await plug.on()
        new_status = "ON"

    write_status(device_name, new_status)
    print(f"{device_name} turned {new_status}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python tapo_toggle.py <device_name>")
        print("Example: python tapo_toggle.py officefan")
        raise SystemExit(1)

    device_name = sys.argv[1].strip().lower()
    asyncio.run(toggle_device(device_name))


if __name__ == "__main__":
    main()
