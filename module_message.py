class ModuleMessage:
    ATTRIBUTE_KEYS = [
        'protocol_id',
        'message_type',
        'message_length',
        'message_id',
        'string_id',
        'module_id',
        'module_state',
        'module_state_of_change',
        'min_cell_temperature',
        'avg_cell_temperature',
        'max_cell_temperature',
        'module_voltage',
        'min_cell_voltage',
        'avg_cell_voltage',
        'max_cell_voltage',
        'module_amperes',
        'alarm_and_status',
        'module_assembly_revision',
        'module_serial_no',
        'master_software_version',
        'slave_software_version',
        'max_front_power_conn_temp'
    ]

    ALARM_AND_STATUS_BITMASKS = {
        'temperature_warning':               '1000000000000000000000000000000000000000',
        'temperature_fault':                 '0100000000000000000000000000000000000000',
        'high_current_warning':              '0010000000000000000000000000000000000000',
        'high_current_fault':                '0001000000000000000000000000000000000000',
        'high_voltage_warning':              '0000100000000000000000000000000000000000',
        'high_voltage_fault':                '0000010000000000000000000000000000000000',
        'low_voltage_warning':               '0000001000000000000000000000000000000000',
        'low_voltage_fault':                 '0000000100000000000000000000000000000000',
        'low_voltage_non_recoverable_fault': '0000000010000000000000000000000000000000',
        'charge_low_warning':                '0000000000001000000000000000000000000000',
        'module_communication_error':        '0000000000000100000000000000000000000000',
        'module_communication_fault':        '0000000000000010000000000000000000000000',
        'under_volt_disable':                '0000000000000001000000000000000000000000',
        'over_volt_disable':                 '0000000000000000100000000000000000000000',
        'cell_0_balancing':                  '0000000000000000000000000000000010000000',
        'cell_1_balancing':                  '0000000000000000000000000000000001000000',
        'cell_2_balancing':                  '0000000000000000000000000000000000100000',
        'cell_3_balancing':                  '0000000000000000000000000000000000010000',
        'cell_4_balancing':                  '0000000000000000000000000000000000001000',
        'cell_5_balancing':                  '0000000000000000000000000000000000000100',
        'cell_6_balancing':                  '0000000000000000000000000000000000000010'
    }

    SAMPLE_DATA = {
        'protocol_id': '001',
        'message_type': 'M',
        'message_length': '122',
        'message_id': '419',
        'string_id': '00',
        'module_id': '00',
        'module_state': 'R',
        'module_state_of_change': '051',
        'min_cell_temperature': '022',
        'avg_cell_temperature': '023',
        'max_cell_temperature': '027',
        'module_voltage': '025709',
        'min_cell_voltage': '003653',
        'avg_cell_voltage': '003672',
        'max_cell_voltage': '003710',
        'module_amperes': '00000',
        'alarm_and_status': '00000000',
        'module_assembly_revision': '000',
        'module_serial_no': '1311250000800',
        'master_software_version': '0501',
        'slave_software_version': '0496',
        'max_front_power_conn_temp': '029'
    }

    # Pass an options dict to instantiate.
    def __init__(self, **options):
        for key in ATTRIBUTE_KEYS:
            set_attr(self, key, options[key])

    def alarm_and_status_int(self):
        return int(self.alarm_and_status, 16)

    def temperature_warning(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['temperature_warning']
        return (bitmask & alarm_and_status_int) > 0

    def temperature_fault(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['temperature_fault']
        return (bitmask & alarm_and_status_int) > 0

    def high_current_warning(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['high_current_warning']
        return (bitmask & alarm_and_status_int) > 0

    def high_current_fault(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['high_current_fault']
        return (bitmask & alarm_and_status_int) > 0

    def high_voltage_warning(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['high_voltage_warning']
        return (bitmask & alarm_and_status_int) > 0

    def high_voltage_fault(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['high_voltage_fault']
        return (bitmask & alarm_and_status_int) > 0

    def low_voltage_warning(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['low_voltage_warning']
        return (bitmask & alarm_and_status_int) > 0

    def low_voltage_fault(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['low_voltage_fault']
        return (bitmask & alarm_and_status_int) > 0

    def low_voltage_non_recoverable_fault(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['low_voltage_non_recoverable_fault']
        return (bitmask & alarm_and_status_int) > 0

    def charge_low_warning(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['charge_low_warning']
        return (bitmask & alarm_and_status_int) > 0

    def module_communication_error(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['module_communication_error']
        return (bitmask & alarm_and_status_int) > 0

    def module_communication_fault(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['module_communication_fault']
        return (bitmask & alarm_and_status_int) > 0

    def under_volt_disable(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['under_volt_disable']
        return (bitmask & alarm_and_status_int) > 0

    def over_volt_disable(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['over_volt_disable']
        return (bitmask & alarm_and_status_int) > 0

    def cell_0_balancing(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['cell_0_balancing']
        return (bitmask & alarm_and_status_int) > 0

    def cell_1_balancing(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['cell_1_balancing']
        return (bitmask & alarm_and_status_int) > 0

    def cell_2_balancing(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['cell_2_balancing']
        return (bitmask & alarm_and_status_int) > 0

    def cell_3_balancing(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['cell_3_balancing']
        return (bitmask & alarm_and_status_int) > 0

    def cell_4_balancing(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['cell_4_balancing']
        return (bitmask & alarm_and_status_int) > 0

    def cell_5_balancing(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['cell_5_balancing']
        return (bitmask & alarm_and_status_int) > 0

    def cell_6_balancing(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['cell_6_balancing']
        return (bitmask & alarm_and_status_int) > 0

