class Value:
    def __init__(self, name, value,  address_modbus):
        self.name = name
        self.value = value
        self.address_modbus = address_modbus


class CC301:
    """
    print(name, value, quality, time)
    >200.4.1.1: dtDouble, 0[0]	=VALUE*0.001; Текущая активная мощность суммарная, кВт
    >200.4.1.2: dtDouble, 0[1]	=VALUE*0.001; Текущая активная мощность, фаза 1, кВт
    >200.4.1.3: dtDouble, 0[2]	=VALUE*0.001; Текущая активная мощность, фаза 2, кВт
    >200.4.1.4: dtDouble, 0[3]	=VALUE*0.001; Текущая активная мощность, фаза 3, кВт
    >200.4.1.5: dtDouble, 0[4]	=VALUE*0.001; Текущая реактивная мощность суммарная, кВар
    >200.4.1.6: dtDouble, 0[5]	=VALUE*0.001; Текущая реактивная мощность, фаза 1, кВар
    >200.4.1.7: dtDouble, 0[6]	=VALUE*0.001; Текущая реактивная мощность, фаза 2, кВар
    >200.4.1.8: dtDouble, 0[7]	=VALUE*0.001; Текущая реактивная мощность, фаза 3, кВар
    >200.4.1.9: dtDouble, 0[8]	; Текущее напряжение среднее по фазам, В
    >200.4.1.10: dtDouble, 0[9]	; Текущее напряжение, фаза 1, В
    >200.4.1.11: dtDouble, 0[10]	; Текущее напряжение, фаза 2, В
    >200.4.1.12: dtDouble, 0[11]	; Текущее напряжение, фаза 3, В
    >200.4.1.13: dtDouble, 0[12]	; Текущий ток средний по фазам, А
    >200.4.1.14: dtDouble, 0[13]	; Текущий ток, фаза 1, А
    >200.4.1.15: dtDouble, 0[14]	; Текущий ток, фаза 2, А
    >200.4.1.16: dtDouble, 0[15]	; Текущий ток, фаза 3, А
    >200.4.1.17: dtDouble, 0[16]	; Не используется (=0)
    >200.4.1.18: dtDouble, 0[17]	; cos F, фаза 1
    >200.4.1.19: dtDouble, 0[18]	; cos F, фаза 2
    >200.4.1.20: dtDouble, 0[19]	; cos F, фаза 3
    >200.4.1.21: dtDouble, 0[20]	; Частота, Гц
    >200.4.1.22: dtDouble, 0[21]	=VALUE*0.001; Сумма активной прямой энергии, кВт ч
    >200.4.1.23: dtDouble, 0[22]	=VALUE*0.001; Сумма активной обратной энергии, кВт ч
    >200.4.1.24: dtDouble, 0[23]	=VALUE*0.001; Сумма реактивной прямой энергии, кВар ч
    >200.4.1.25: dtDouble, 0[24]	=VALUE*0.001; Сумма реактивной обратной энергии, кВар ч
    >200.4.1.26: dtDouble, 0[25]	=VALUE*0.001; Активная прямая энергия по тарифу 1, кВт ч
    >200.4.1.27: dtDouble, 0[26]	=VALUE*0.001; Активная обратная энергия по тарифу 1, кВт ч
    >200.4.1.28: dtDouble, 0[27]	=VALUE*0.001; Реактивная прямая энергия по тарифу 1, кВар ч
    >200.4.1.29: dtDouble, 0[28]	=VALUE*0.001; Реактивная обратная энергия по тарифу 1, кВар ч
    >200.4.1.30: dtDouble, 0[29]	=VALUE*0.001; Активная прямая энергия по тарифу 2, кВт ч
    >200.4.1.31: dtDouble, 0[30]	=VALUE*0.001; Активная обратная энергия по тарифу 2, кВт ч
    >200.4.1.32: dtDouble, 0[31]	=VALUE*0.001; Реактивная прямая энергия по тарифу 2, кВар ч
    >200.4.1.33: dtDouble, 0[32]	=VALUE*0.001; Реактивная обратная энергия по тарифу 2, кВар ч
    >200.4.1.34: dtDouble, 0[33]	=VALUE*0.001; Активная прямая энергия по тарифу 3, кВт ч
    >200.4.1.35: dtDouble, 0[34]	=VALUE*0.001; Активная обратная энергия по тарифу 3, кВт ч
    >200.4.1.36: dtDouble, 0[35]	=VALUE*0.001; Реактивная прямая энергия по тарифу 3, кВар ч
    >200.4.1.37: dtDouble, 0[36]	=VALUE*0.001; Реактивная обратная энергия по тарифу 3, кВар ч
    >200.4.1.38: dtDouble, 0[37]	=VALUE*0.001; Активная прямая энергия по тарифу 4, кВт ч
    >200.4.1.39: dtDouble, 0[38]	=VALUE*0.001; Активная обратная энергия по тарифу 4, кВт ч
    >200.4.1.40: dtDouble, 0[39]	=VALUE*0.001; Реактивная прямая энергия по тарифу 4, кВар ч
    >200.4.1.41: dtDouble, 0[40]	=VALUE*0.001; Реактивная обратная энергия по тарифу 4, кВар ч
    >200.4.1.42: dtDouble, 0[41]	; Текущие дата и время прибора
    """
    registers = {}

    def __init__(self,
                 curr_active_power_total=None,
                 curr_active_power_phase1=None,
                 curr_active_power_phase2=None,
                 curr_active_power_phase3=None,

                 total_curr_reactive_power=None,
                 curr_reactive_power_phase1=None,
                 curr_reactive_power_phase2=None,
                 curr_reactive_power_phase3=None,

                 curr_voltage_average_for_phases=None,
                 curr_voltage_phase1=None,
                 curr_voltage_phase2=None,
                 curr_voltage_phase3=None,

                 curr_average_for_phases=None,
                 curr_phase1=None,
                 curr_phase2=None,
                 curr_phase3=None,

                 cos_f_phase1=None,
                 cos_f_phase2=None,
                 cos_f_phase3=None,
                 frequency=None,

                 the_amount_of_active_direct_energy=None,
                 the_amount_of_active_reverse_energy=None,
                 tum_of_reactive_direct_energy=None,
                 tum_of_reactive_reverse_energy=None,

                 active_direct_energy_at_tariff1=None,
                 active_reverse_energy_at_tariff1=None,
                 reactive_direct_energy_at_tariff1=None,
                 reactive_reverse_energy_at_tariff1=None,

                 active_direct_energy_at_tariff2=None,
                 active_reverse_energy_at_tariff2=None,
                 reactive_direct_energy_at_tariff2=None,
                 reactive_reverse_energy_at_tariff2=None,

                 active_direct_energy_at_tariff3=None,
                 active_reverse_energy_at_tariff3=None,
                 reactive_direct_energy_at_tariff3=None,
                 reactive_reverse_energy_at_tariff3=None,

                 active_direct_energy_at_tariff4=None,
                 active_reverse_energy_at_tariff4=None,
                 reactive_direct_energy_at_tariff4=None,
                 reactive_reverse_energy_at_tariff4=None,

                 current_date_time_device=None
                 ):
        self.curr_active_power_total = curr_active_power_total,
        self.curr_active_power_phase1 = curr_active_power_phase1,
        self.curr_active_power_phase2 = curr_active_power_phase2,
        self.curr_active_power_phase3 = curr_active_power_phase3,

        self.total_curr_reactive_power = total_curr_reactive_power,
        self.curr_reactive_power_phase1 = curr_reactive_power_phase1,
        self.curr_reactive_power_phase2 = curr_reactive_power_phase2,
        self.curr_reactive_power_phase3 = curr_reactive_power_phase3,

        self.curr_voltage_average_for_phases = curr_voltage_average_for_phases,
        self.curr_voltage_phase1 = curr_voltage_phase1,
        self.curr_voltage_phase2 = curr_voltage_phase2,
        self.curr_voltage_phase3 = curr_voltage_phase3,

        self.curr_average_for_phases = curr_average_for_phases,
        self.curr_phase1 = curr_phase1,
        self.curr_phase2 = curr_phase2,
        self.curr_phase3 = curr_phase3,

        self.cos_f_phase1 = cos_f_phase1,
        self.cos_f_phase2 = cos_f_phase2,
        self.cos_f_phase3 = cos_f_phase3,
        self.frequency = frequency,

        self.the_amount_of_active_direct_energy = the_amount_of_active_direct_energy,
        self.the_amount_of_active_reverse_energy = the_amount_of_active_reverse_energy,
        self.tum_of_reactive_direct_energy = tum_of_reactive_direct_energy,
        self.tum_of_reactive_reverse_energy = tum_of_reactive_reverse_energy,

        self.active_direct_energy_at_tariff1 = active_direct_energy_at_tariff1,
        self.active_reverse_energy_at_tariff1 = active_reverse_energy_at_tariff1,
        self.reactive_direct_energy_at_tariff1 = reactive_direct_energy_at_tariff1,
        self.reactive_reverse_energy_at_tariff1 = reactive_reverse_energy_at_tariff1,

        self.active_direct_energy_at_tariff2 = active_direct_energy_at_tariff2,
        self.active_reverse_energy_at_tariff2 = active_reverse_energy_at_tariff2,
        self.reactive_direct_energy_at_tariff2 = reactive_direct_energy_at_tariff2,
        self.reactive_reverse_energy_at_tariff2 = reactive_reverse_energy_at_tariff2,

        self.active_direct_energy_at_tariff3 = active_direct_energy_at_tariff3,
        self.active_reverse_energy_at_tariff3 = active_reverse_energy_at_tariff3,
        self.reactive_direct_energy_at_tariff3 = reactive_direct_energy_at_tariff3,
        self.reactive_reverse_energy_at_tariff3 = reactive_reverse_energy_at_tariff3,

        self.active_direct_energy_at_tariff4 = active_direct_energy_at_tariff4,
        self.active_reverse_energy_at_tariff4 = active_reverse_energy_at_tariff4,
        self.reactive_direct_energy_at_tariff4 = reactive_direct_energy_at_tariff4,
        self.reactive_reverse_energy_at_tariff4 = reactive_reverse_energy_at_tariff4,

        self.current_date_time_device = current_date_time_device


class TM104:
    pass


class TM104M:
    pass


class Ventilation:
    pass
