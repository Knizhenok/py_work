# import UNIT as UNIT
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder
from pymodbus.constants import Endian

UNIT = 0x1

IP_Address = '127.0.0.1'
temp = 0
client_modbus = ModbusTcpClient(IP_Address)

if client_modbus.connect():
    try:

        # запись в holding регистр числа Word 16 bit
        wr = client_modbus.write_register(102, 102)
        print(wr)

        # считывание 4-х holding регистров Word 16 bit
        res = client_modbus.read_holding_registers(101, 4)
        print(res.registers[0])
        print(res.registers[1])
        print(res.registers[2])

        # считывание real из 2-х holding регистров Word 16 bit
        read_value = client_modbus.read_holding_registers(0, 2)
        # read_value = client_modbus.read_input_registers(0, 2)
        real_decoder = BinaryPayloadDecoder.fromRegisters(read_value.registers, byteorder=Endian.Big,
                                                          wordorder=Endian.Little)
        value = real_decoder.decode_32bit_float()
        print(value)

        builder = BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Little)
        builder.add_32bit_float(789.56)
        payload = builder.build()
        client_modbus.write_registers(0, payload, skip_encode=True)

    except BaseException as e:
        print(e)

    client_modbus.close()
    # print(dict_temp)
else:
    print(f'not connections {IP_Address}')
