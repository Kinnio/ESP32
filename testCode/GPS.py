from machine import UART, Pin
import time

if __name__=='__main__':
    gps = UART(0, baudrate=9600, bits=8, parity=None, stop=1, timeout=1000)
    for i in range(1000):
        if gps.any(): 							# 检查是否有数据收到
            data = gps.readline() 				# 读取一行数据
            print(data.decode('utf-8').strip()) # 转换为字符串并打印
        time.sleep(1)
