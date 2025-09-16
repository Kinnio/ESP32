# ESP32-基于MicroPython

**异常恢复方式**
1. 在本机电脑Python已经安装的前提下，进入cmd命令行模式
2. 运行pip install esptool安装esptool工具
3. 使用pip show -f esptool | findstr Location查看esptool工具的绝对地址（以D:\Python\Python313\Lib\site-packages举例，取D:\Python\Python313\ + Scripts\esptool.exe就是esptool工具的绝对地址）
4. 输入D:\Python\Python313\Scripts\esptool.exe version查看安装是否成功以及esptool是否可以正常运行
5. ESP32先同时按下IO0和EN按键，然后将Type-C线连接电脑和ESP32，再先松开EN键，最后松开IO0键
6. 输入D:\Python\Python313\Scripts\esptool.exe --port COM9 write_flash -z 0x1000 C:\Users\Administrato\Downloads\ESP32_GENERIC-20250911-v1.26.1.bin重新烧写固件
   （注：COM9为设备管理器下ESP32的串口号；C:\Users\Administrato\Downloads\ESP32_GENERIC-20250911-v1.26.1.bin是要烧写的固件的绝对地址；固件可以从https://micropython.org/download/ESP32_GENERIC/上下载最新的）
