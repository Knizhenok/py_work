import table_address as ta


class CC301:
    registers_values = {}
    temp_stroke = ''

    def __init__(self, table_address, opc_address1, opc_address2, start_number_modbus_registers=0):
        self.opc_address1 = str(opc_address1)
        self.opc_address2 = str(opc_address2)
        self.start_number_modbus_registers = start_number_modbus_registers
        self.registers_values = table_address

        for temp in self.registers_values.values():
            a = temp.get_name()
            a = a[:4] + self.opc_address1 + '.' + self.opc_address2 + a[7:]
            temp.set_name(a)
            temp.set_address_modbus(self.start_number_modbus_registers)
            self.start_number_modbus_registers += 1


class TM104:
    pass


class TM104M:
    pass


class Ventilation:
    pass


if __name__ == '__main__':

    CC301_1 = CC301(ta.CC301, 5, 3, 10)

    for key, value in CC301_1.registers_values.items():
        print(key, value.get_address_modbus(), value.get_name())

