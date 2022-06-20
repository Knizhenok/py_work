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

CC301_2 = {
           'curr_active_power_total': Value(name='200.4.2.1'),
           'curr_active_power_phase1': Value(name='200.4.2.2'),
           'curr_active_power_phase2': Value(name='200.4.2.3'),
           'curr_active_power_phase3': Value(name='200.4.2.4'),

           'total_curr_reactive_power': Value(name='200.4.2.5'),
           'curr_reactive_power_phase1': Value(name='200.4.2.6'),
           'curr_reactive_power_phase2': Value(name='200.4.2.7'),
           'curr_reactive_power_phase3': Value(name='200.4.2.8'),

           'curr_voltage_average_for_phases': Value(name='200.4.2.9'),
           'curr_voltage_phase1': Value(name='200.4.2.10'),
           'curr_voltage_phase2': Value(name='200.4.2.11'),
           'curr_voltage_phase3': Value(name='200.4.2.12'),

           'curr_average_for_phases': Value(name='200.4.2.13'),
           'curr_phase1': Value(name='200.4.2.14'),
           'curr_phase2': Value(name='200.4.2.15'),
           'curr_phase3': Value(name='200.4.2.16'),

           'cos_f_phase1': Value(name='200.4.2.18'),
           'cos_f_phase2': Value(name='200.4.2.19'),
           'cos_f_phase3': Value(name='200.4.2.20'),
           'frequency': Value(name='200.4.2.21'),

           'the_amount_of_active_direct_energy': Value(name='200.4.2.22'),
           'the_amount_of_active_reverse_energy': Value(name='200.4.2.23'),
           'tum_of_reactive_direct_energy': Value(name='200.4.2.24'),
           'tum_of_reactive_reverse_energy': Value(name='200.4.2.25'),

           'active_direct_energy_at_tariff1': Value(name='200.4.2.26'),
           'active_reverse_energy_at_tariff1': Value(name='200.4.2.27'),
           'reactive_direct_energy_at_tariff1': Value(name='200.4.2.28'),
           'reactive_reverse_energy_at_tariff1': Value(name='200.4.2.29'),

           'active_direct_energy_at_tariff2': Value(name='200.4.2.30'),
           'active_reverse_energy_at_tariff2': Value(name='200.4.2.31'),
           'reactive_direct_energy_at_tariff2': Value(name='200.4.2.32'),
           'reactive_reverse_energy_at_tariff2': Value(name='200.4.2.33'),

           'active_direct_energy_at_tariff3': Value(name='200.4.2.34'),
           'active_reverse_energy_at_tariff3': Value(name='200.4.2.35'),
           'reactive_direct_energy_at_tariff3': Value(name='200.4.2.36'),
           'reactive_reverse_energy_at_tariff3': Value(name='200.4.2.37'),

           'active_direct_energy_at_tariff4': Value(name='200.4.2.38'),
           'active_reverse_energy_at_tariff4': Value(name='200.4.2.39'),
           'reactive_direct_energy_at_tariff4': Value(name='200.4.2.40'),
           'reactive_reverse_energy_at_tariff4': Value(name='200.4.2.41'),

           'current_date_time_device': Value(name='200.4.2.42')
           }
CC301_3 = {
           'curr_active_power_total': Value(name='200.4.3.1'),
           'curr_active_power_phase1': Value(name='200.4.3.2'),
           'curr_active_power_phase2': Value(name='200.4.3.3'),
           'curr_active_power_phase3': Value(name='200.4.3.4'),

           'total_curr_reactive_power': Value(name='200.4.3.5'),
           'curr_reactive_power_phase1': Value(name='200.4.3.6'),
           'curr_reactive_power_phase2': Value(name='200.4.3.7'),
           'curr_reactive_power_phase3': Value(name='200.4.3.8'),

           'curr_voltage_average_for_phases': Value(name='200.4.3.9'),
           'curr_voltage_phase1': Value(name='200.4.3.10'),
           'curr_voltage_phase2': Value(name='200.4.3.11'),
           'curr_voltage_phase3': Value(name='200.4.3.12'),

           'curr_average_for_phases': Value(name='200.4.3.13'),
           'curr_phase1': Value(name='200.4.3.14'),
           'curr_phase2': Value(name='200.4.3.15'),
           'curr_phase3': Value(name='200.4.3.16'),

           'cos_f_phase1': Value(name='200.4.3.18'),
           'cos_f_phase2': Value(name='200.4.3.19'),
           'cos_f_phase3': Value(name='200.4.3.20'),
           'frequency': Value(name='200.4.3.21'),

           'the_amount_of_active_direct_energy': Value(name='200.4.3.22'),
           'the_amount_of_active_reverse_energy': Value(name='200.4.3.23'),
           'tum_of_reactive_direct_energy': Value(name='200.4.3.24'),
           'tum_of_reactive_reverse_energy': Value(name='200.4.3.25'),

           'active_direct_energy_at_tariff1': Value(name='200.4.3.26'),
           'active_reverse_energy_at_tariff1': Value(name='200.4.3.27'),
           'reactive_direct_energy_at_tariff1': Value(name='200.4.3.28'),
           'reactive_reverse_energy_at_tariff1': Value(name='200.4.3.29'),

           'active_direct_energy_at_tariff2': Value(name='200.4.3.30'),
           'active_reverse_energy_at_tariff2': Value(name='200.4.3.31'),
           'reactive_direct_energy_at_tariff2': Value(name='200.4.3.32'),
           'reactive_reverse_energy_at_tariff2': Value(name='200.4.3.33'),

           'active_direct_energy_at_tariff3': Value(name='200.4.3.34'),
           'active_reverse_energy_at_tariff3': Value(name='200.4.3.35'),
           'reactive_direct_energy_at_tariff3': Value(name='200.4.3.36'),
           'reactive_reverse_energy_at_tariff3': Value(name='200.4.3.37'),

           'active_direct_energy_at_tariff4': Value(name='200.4.3.38'),
           'active_reverse_energy_at_tariff4': Value(name='200.4.3.39'),
           'reactive_direct_energy_at_tariff4': Value(name='200.4.3.40'),
           'reactive_reverse_energy_at_tariff4': Value(name='200.4.3.41'),

           'current_date_time_device': Value(name='200.4.3.42')
           }
CC301_4 = {
           'curr_active_power_total': Value(name='200.4.4.1'),
           'curr_active_power_phase1': Value(name='200.4.4.2'),
           'curr_active_power_phase2': Value(name='200.4.4.3'),
           'curr_active_power_phase3': Value(name='200.4.4.4'),

           'total_curr_reactive_power': Value(name='200.4.4.5'),
           'curr_reactive_power_phase1': Value(name='200.4.4.6'),
           'curr_reactive_power_phase2': Value(name='200.4.4.7'),
           'curr_reactive_power_phase3': Value(name='200.4.4.8'),

           'curr_voltage_average_for_phases': Value(name='200.4.4.9'),
           'curr_voltage_phase1': Value(name='200.4.4.10'),
           'curr_voltage_phase2': Value(name='200.4.4.11'),
           'curr_voltage_phase3': Value(name='200.4.4.12'),

           'curr_average_for_phases': Value(name='200.4.4.13'),
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

