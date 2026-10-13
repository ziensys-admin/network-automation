from datetime import datetime

devices = [
    {
        "hostname": "R1",
        "ip_address": "192.0.2.1",
        "device_type": "router",
        "vendor": "Cisco",
    },
    {
        "hostname": "SW1",
        "ip_address": "192.0.2.2",
        "device_type": "switch",
        "vendor": "Cisco",
    },
    {
        "hostname": "FW1",
        "ip_address": "192.0.2.3",
        "device_type": "firewall",
        "vendor": "Fortinet",
    },
]

print("NETWORK DEVICE INVENTORY")
print(f"Generated: {datetime.now():%Y-%m-%d %H:%M:%S}")
print("-" * 65)

for device in devices:
    print(
        f"{device['hostname']:6} "
        f"{device['ip_address']:15} "
        f"{device['device_type']:10} "
        f"{device['vendor']}"
    )

print("-" * 65)
print(f"Total devices: {len(devices)}")

Mytest -github
