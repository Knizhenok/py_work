class Value:
    def __init__(self, name='', value=0, address_modbus=0):
        self.name = name
        self.value = value
        self.address_modbus = address_modbus

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_address_modbus(self, address_modbus):
        self.address_modbus = address_modbus

    def get_address_modbus(self):
        return self.address_modbus


CC301 = {
           'curr_active_power_total': Value(name='200.4.1.1'),
           'curr_active_power_phase1': Value(name='200.4.1.2'),
           'curr_active_power_phase2': Value(name='200.4.1.3'),
           'curr_active_power_phase3': Value(name='200.4.1.4'),

           'total_curr_reactive_power': Value(name='200.4.1.5'),
           'curr_reactive_power_phase1': Value(name='200.4.1.6'),
           'curr_reactive_power_phase2': Value(name='200.4.1.7'),
           'curr_reactive_power_phase3': Value(name='200.4.1.8'),

           'curr_voltage_average_for_phases': Value(name='200.4.1.9'),
           'curr_voltage_phase1': Value(name='200.4.1.10'),
           'curr_voltage_phase2': Value(name='200.4.1.11'),
           'curr_voltage_phase3': Value(name='200.4.1.12'),

           'curr_average_for_phases': Value(name='200.4.1.13'),
           'curr_phase1': Value(name='200.4.1.14'),
           'curr_phase2': Value(name='200.4.1.15'),
           'curr_phase3': Value(name='200.4.1.16'),

           'cos_f_phase1': Value(name='200.4.1.18'),
           'cos_f_phase2': Value(name='200.4.1.19'),
           'cos_f_phase3': Value(name='200.4.1.20'),
           'frequency': Value(name='200.4.1.21'),

           'the_amount_of_active_direct_energy': Value(name='200.4.1.22'),
           'the_amount_of_active_reverse_energy': Value(name='200.4.1.23'),
           'tum_of_reactive_direct_energy': Value(name='200.4.1.24'),
           'tum_of_reactive_reverse_energy': Value(name='200.4.1.25'),

           'active_direct_energy_at_tariff1': Value(name='200.4.1.26'),
           'active_reverse_energy_at_tariff1': Value(name='200.4.1.27'),
           'reactive_direct_energy_at_tariff1': Value(name='200.4.1.28'),
           'reactive_reverse_energy_at_tariff1': Value(name='200.4.1.29'),

           'active_direct_energy_at_tariff2': Value(name='200.4.1.30'),
           'active_reverse_energy_at_tariff2': Value(name='200.4.1.31'),
           'reactive_direct_energy_at_tariff2': Value(name='200.4.1.32'),
           'reactive_reverse_energy_at_tariff2': Value(name='200.4.1.33'),

           'active_direct_energy_at_tariff3': Value(name='200.4.1.34'),
           'active_reverse_energy_at_tariff3': Value(name='200.4.1.35'),
           'reactive_direct_energy_at_tariff3': Value(name='200.4.1.36'),
           'reactive_reverse_energy_at_tariff3': Value(name='200.4.1.37'),

           'active_direct_energy_at_tariff4': Value(name='200.4.1.38'),
           'active_reverse_energy_at_tariff4': Value(name='200.4.1.39'),
           'reactive_direct_energy_at_tariff4': Value(name='200.4.1.40'),
           'reactive_reverse_energy_at_tariff4': Value(name='200.4.1.41'),

           'current_date_time_device': Value(name='200.4.1.42')
           }

ventilation_real = {
            'moto_hours_of_supply_p1': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1R44597'),
            'moto_hours_of_supply_p2': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1R44599'),
            'moto_hours_of_supply_p3': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1R44601'),
            'moto_hours_of_supply_p4': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1R44603'),
            'moto_min_supply_p1': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1R44617'),
            'moto_min_supply_p2': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1R44619'),
            'moto_min_supply_p3': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1R44621'),
            'moto_min_supply_p4': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1R44623')
}

ventilation_boolean = {
            'alarm_p1': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2049'),
            'work_p1': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2050'),
            'alarm_p2': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2051'),
            'work_p2': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2052'),
            'alarm_p3': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2053'),
            'work_p3': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2054'),
            'alarm_p4': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2055'),
            'work_p4': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2056'),
            'work_p_1_10': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2057'),
            'work_fan1': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2058'),
            'work_fan2': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2059'),
            'work_fan3': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2060'),
            'work_fan4': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2061'),
            'work_fan5': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2062'),
            'work_fan10': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2063'),
            'working_light_line1_1': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2064'),
            'working_light_line1_2': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2065'),
            'working_light_line2_1': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2066'),
            'working_light_line2_2': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2067'),
            'working_light_line3_1': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2068'),
            'working_light_line3_2': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2069'),

            'alarm_light_line1_1': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2070'),
            'alarm_light_line2_1': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2071'),
            'alarm_light_line3_1': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2072'),
            '1RP_AVR_work_input1': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2073'),
            '1RP_AVR_work_input2': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2074'),
            '2RP_AVR_work_input1': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2075'),
            '2RP_AVR_work_input2': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2076'),

            'alarm_reset_p1': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2149'),
            'alarm_reset_p2': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2150'),
            'alarm_reset_p3': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2151'),
            'alarm_reset_p4': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2152'),
            'general_alarm_p1_10': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2099'),
            'general_working_light': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2100'),
            'general_working_alarm_light': Value(name='Kamenb_korpys_m1_mdbs_A/dev/ttyS3_A1C2101'),

}



