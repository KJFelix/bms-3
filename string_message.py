class StringMessage:
    ATTRIBUTE_KEYS = [
        'protocol_id',
        'message_type',
        'message_length',
        'message_id',
        'string_id',
        'state',
        'state_of_charge',
        'temperature',
        'voltage',
        'amperes',
        'alarm_and_status',
        'bms_assembly_revision',
        'bms_serial_no',
        'bms_master_software_version',
        'bms_slave_software_version',
        'watt_hours_to_discharge',
        'watt_hours_to_charge',
        'min_cell_millivolts',
        'max_cell_millivolts',
        'front_power_temperature'
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
        'bms_self_check_warning':            '0000000000000010000000000000000000000000',
        'under_volt_disable':                '0000000000000001000000000000000000000000',
        'over_volt_disable':                 '0000000000000000100000000000000000000000',
        'string_contactor_on':               '0000000000000000010000000000000000000000'
    }

    SAMPLE_DATA = {
        'message_type': 'S',
        'message_length': '122',
        'message_id': '078',
        'string_id': '00',
        'state': 'I',
        'state_of_charge': '053',
        'temperature': '020',
        'voltage': '025840',
        'amperes': '00003',
        'alarm_and_status': '00000000',
        'bms_assembly_revision': '002',
        'bms_serial_no': '1607150018800',
        'bms_master_software_version': '887',
        'bms_slave_software_version': '842',
        'watt_hours_to_discharge': '000509',
        'watt_hours_to_charge': '000451',
        'min_cell_millivolts': '003664',
        'max_cell_millivolts': '003744',
        'front_power_temperature': '020'
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

    def bms_self_check_warning(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['bms_self_check_warning']
        return (bitmask & alarm_and_status_int) > 0

    def under_volt_disable(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['under_volt_disable']
        return (bitmask & alarm_and_status_int) > 0

    def over_volt_disable(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['over_volt_disable']
        return (bitmask & alarm_and_status_int) > 0

    def string_contactor_on(self):
        bitmask = ALARM_AND_STATUS_BITMASKS['string_contactor_on']
        return (bitmask & alarm_and_status_int) > 0
