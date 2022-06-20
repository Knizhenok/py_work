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

    CC301_1 = CC301(ta.CC301, 4, 1, 10)  # Котельная №1 АВР Ввод №1 1.2ВРУ
    CC301_2 = CC301(ta.CC301, 4, 2, 51)  # Котельная №1 АВР Ввод №2 2.2ВРУ
    CC301_3 = CC301(ta.CC301, 4, 3, 92)  # Насосная АВР Ввод №1.2 ВРУ
    CC301_4 = CC301(ta.CC301, 4, 4, 133)  # Насосная АВР Ввод №2.2 ВРУ
    CC301_5 = CC301(ta.CC301, 4, 5, 174)  # РУ-0.4 кВ Ввод №1
    CC301_6 = CC301(ta.CC301, 4, 6, 215)  # РУ-0.4 кВ Ввод №2
    CC301_7 = CC301(ta.CC301, 4, 7, 256)  # Ввод ШНО

    CC301_SN19092162 = CC301(ta.CC301, 1, 1, 297)
    CC301_SN19092151 = CC301(ta.CC301, 1, 2, 338)
    CC301_SN19092149 = CC301(ta.CC301, 1, 3, 379)
    CC301_SN19092153 = CC301(ta.CC301, 1, 4, 420)
    CC301_SN19092166 = CC301(ta.CC301, 1, 5, 461)
    CC301_SN19092156 = CC301(ta.CC301, 1, 6, 502)
    CC301_SN19092159 = CC301(ta.CC301, 1, 7, 543)
    CC301_SN19092158 = CC301(ta.CC301, 1, 8, 584)
    CC301_SN19092160 = CC301(ta.CC301, 1, 9, 625)
    CC301_SN19092157 = CC301(ta.CC301, 1, 10, 666)
    CC301_SN19092164 = CC301(ta.CC301, 1, 11, 707)
    CC301_SN19092161 = CC301(ta.CC301, 1, 12, 748)
    CC301_SN19092168 = CC301(ta.CC301, 1, 13, 789)
    CC301_SN19092163 = CC301(ta.CC301, 1, 14, 830)
    CC301_SN19092165 = CC301(ta.CC301, 1, 15, 871)
    CC301_SN19092167 = CC301(ta.CC301, 1, 16, 912)
    CC301_SN19092155 = CC301(ta.CC301, 1, 17, 953)
    CC301_SN19091794 = CC301(ta.CC301, 1, 18, 994)
    CC301_SN19091795 = CC301(ta.CC301, 1, 19, 1035)
    CC301_SN19092154 = CC301(ta.CC301, 1, 20, 1076)
    CC301_SN19092150 = CC301(ta.CC301, 1, 21, 1117)
    CC301_SN19092152 = CC301(ta.CC301, 1, 22, 1158)

    # for key, value in CC301_1.registers_values.items():
    #     print(key, value.get_address_modbus(), value.get_name())

    for key, value in CC301_1.registers_values.items():
        print(key, value.get_address_modbus(), value.get_name())


