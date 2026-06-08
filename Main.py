import snap7
import time
import serial
from snap7.util import get_bool,set_bool,get_int,set_int,set_string
com='COM5'
ip=('192.168.0.1')
rack=0
slot=1
kho={}
UID=''
esp32=serial.Serial(com,115200,timeout=1)
plc=snap7.client.Client()
def readbool(DB,byte,bit):
    data=plc.db_read(DB,byte,1)
    return get_bool(data,0,bit)
def writebool(DB,byte,bit,value):
    data=plc.db_read(DB,byte,1)
    set_bool(data,0,bit,value)
    plc.db_write(DB,byte,data)
def readint(DB,byte):
    data=plc.db_read(DB,byte,2)
    return get_int(data,0)
def writeint(DB,byte,value):
    data=plc.db_read(DB,byte,2)
    set_int(data,0,value)
    plc.db_write(DB,byte,data)
def writestring(DB, byte, value):
    # --- CẤU HÌNH ---
    max_len = 14  # Khai báo String[14]
    total_size = 16  # 14 ký tự + 2 byte header

    # 1. Xử lý chuỗi Python: Encode sang ASCII và cắt nếu quá dài
    # Nếu value là chuỗi rỗng, nó vẫn hoạt động tốt
    if value is None: value = ""
    string_content = value.encode('ascii')[:max_len]
    actual_len = len(string_content)

    # 2. Tạo mảng byte mới tinh (16 byte toàn số 0)
    data = bytearray(total_size)

    # 3. Ghi Header chuẩn Siemens (Bắt buộc phải có để S_MOVE chạy)
    data[0] = max_len  # Byte 0: Độ dài tối đa (14)
    data[1] = actual_len  # Byte 1: Độ dài thực tế

    # 4. Ghi nội dung chuỗi vào (Từ byte số 2 trở đi)
    data[2: 2 + actual_len] = string_content

    # 5. Ghi thẳng xuống PLC (Không cần read trước)
    plc.db_write(DB, byte, data)
    print(f"Da ghi xuong DB{DB} tai offset {byte}: {value}")  # In ra để debug
try:
    plc.connect(ip,rack,slot)
    if plc.get_connected():
        print('connected')
    while True:
        if readbool(45,18,3)==False:
            if esp32.in_waiting>0:
                UID = esp32.readline().decode('utf-8').strip()
                writebool(6,0,5,1)
                time.sleep(0.5)
                writebool(6,0,5,0)
                if readbool(6,0,0)==False and readbool(6,0,1)==False:
                    print('Vui long nhan nut')
                else:
                    if UID not in kho and readbool(6,0,0)==True:
                        PasscodePlc=readint(14,4)
                        print(PasscodePlc)
                        if PasscodePlc>10:
                            print(f'Dang gui xe UID={UID} co passcode={PasscodePlc}')
                            kho[UID]=PasscodePlc
                            floor=kho[UID]//10
                            location=kho[UID]%10
                            writeint(14,0,floor)
                            writeint(14,2,location)
                            writestring(14,198,UID)
                    elif UID in kho:
                        print('the co trong kho')
                        if readbool(6,0,1)==True:
                            floor=kho[UID]//10
                            location=kho[UID]%10
                            writeint(14, 0, floor)
                            writeint(14, 2, location)
                            print(f'dang lay xe UID={UID} voi passcode={PasscodePlc}')
                            kho.pop(UID)
                    else:
                        print('vui long chon lai thao tac')
        else:
            print('Busy')
            print('Waiting')
            time.sleep(1)
except KeyboardInterrupt:
    print('Exit')
    kho.clear()
except Exception as e:
    print('kiem tra configuration')
