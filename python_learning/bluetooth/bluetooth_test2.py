import bluetooth

# 目标蓝牙设备的地址
target_addr = 'XX:XX:XX:XX:XX:XX'  # 请替换为实际设备的地址

# 创建蓝牙Socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((target_addr, 1))

print("Connected to device")

# 发送数据
data = "Hello, Bluetooth!"
sock.send(data)

# 接收数据
received_data = sock.recv(1024)
print(f"Received data: {received_data}")

# 关闭Socket
sock.close()
