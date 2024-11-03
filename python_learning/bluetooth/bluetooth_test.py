import bluetooth

# 搜索附近的蓝牙设备
devices = bluetooth.discover_devices(duration=8, lookup_names=True)

# 打印搜索到的设备信息
for addr, name in devices:
    print(f"Found device: {name} ({addr})")
