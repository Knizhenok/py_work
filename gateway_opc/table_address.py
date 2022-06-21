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

energy_center_real = {
            'pressure_after_network_pumps': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1R44602')
}

energy_center_boolean = {
            'work_heating_unit1': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2049'),
            'work_heating_unit2': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2050'),
            'work_fan1_RPV': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2051'),
            'work_fan2_RPV': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2052'),
            'work_from_input1_SCHSV': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2053'),
            'work_from_input2_SCHSV': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2054'),
            'Turnon_street_lighting': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2561'),
            'pump_K7.1.1_on': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2149'),
            'pump_K7.1.2_on': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2150'),
            'pump_K7.2_on': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2151'),
            'pump_K7.1.1_automatic_mode': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2152'),
            'pump_K7.1.2_automatic_mode': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2153'),
            'pump_K7.2_auto_mode': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2154'),

            'alarm_pump_K7_dry_running': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2155'),
            'alarm_pump_K7.1.1_the starter_did_not_work': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2156'),
            'alarm_pump_K7.1.1_PCH': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2157'),
            'alarm_pump_K7.1.1_AWR_differential_pressure': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2158'),
            'alarm_pump_K7.1.2_not_workong_starter': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2159'),
            'larm_pump_K7.1.2_PCH': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2160'),
            'alarm_pump_K7.1.2_AWR_differential_pressure': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2161'),
            'alarm_pump_K7.2_not_workong_starter': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2162'),
            'alarm_pump_K7.2_PCH': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2163'),

            'pump_alarm_K7.1.1_general': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2164'),
            'pump_alarm_K7.1.2_general': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2165'),
            'pump_alarm_K7.2_general': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2166'),
            'signal_to_start_pumps_7.1_from_Logo': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2167'),
            'signal_to_start_pumps_7.2_from_Logo': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2168'),
            'select_main_pump_K7.1.1_K7.1.2': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2169'),

            'pump_K8.1_on': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2170'),
            'pump_K8.2_on': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2171'),
            'turn_pumps_K8': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2172'),
            'pump_K8.1_auto_mode': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2173'),
            'pump_K8.2_auto_mode': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2174'),
            'select_main_pump_K8.1_K8.2': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2175'),
            'alarm_pump_K8.1_the starter_did_not_work': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2176'),
            'alarm_pump_K8.1_motor_thermal_protection': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2177'),
            'alarm_pump_K8.1_AWR_differential_pressure': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2178'),
            'alarm_pump_K8.2_not_workong_starter': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2179'),
            'alarm_pump_K8.2_motor_thermal_protection': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2180'),
            'alarm_pump_K8.2_AWR_differential_pressure': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2181'),
            'alarm_pump_K8.1_general': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2182'),
            'alarm_pump_K8.2_general': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2183'),

            'pump_K16.1_on': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2184'),
            'pump_K16.2_on': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2185'),
            'turn_K16': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2186'),
            'pump_K16.1_auto_mode': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2187'),
            'pump K16.2_auto_mode': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2188'),
            'select_main_pump_K16.1_K16.2': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2189'),
            'alarm_pump_K16.1_the starter_did_not_work': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2190'),
            'alarm_pump_K16.1_motor_thermal_protection': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2191'),
            'alarm_pump_K16.1_AWR_differential_pressure': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2192'),
            'alarm_pump_K16.2_not_workong_starter': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2193'),
            'alarm_pump_K16.2_motor_thermal_protection': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2194'),
            'alarm_pump_K16.2_AWR_differential_pressure': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2195'),
            'alarm_pump_K16_dry_running': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2196'),
            'alarm_pump_K16.1_general': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2197'),
            'alarm_pump_K16.2_general': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2198'),
            'alarm_pressure_sensor_after_networkpumps': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C42199'),
            'alarm_no_connection_moduleA2': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2200'),
            'alarm_no_connection_moduleA3': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2201'),
            'alarm_no_connection_moduleA4': Value(name='Kamenb_kotel_eceh_mdbs_A/dev/ttyS0_A1C2202'),
}



