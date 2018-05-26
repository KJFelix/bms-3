from sqlalchemy import Column, Boolean, String, Integer, Date, DateTime, func
from base import Base

class StringMessage(Base):
    __tablename__ = "string_message"
    
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=func.now())

    protocol_id = Column(String)
    message_type = Column(String)
    message_length = Column(Integer)
    message_id = Column(String)
    string_id = Column(String)
    state = Column(String)
    state_of_charge = Column(Integer)
    temperature = Column(Integer)
    voltage = Column(Integer)
    amperes = Column(Integer)
    alarm_and_status = Column(Integer)
    bms_assembly_revision = Column(Integer)
    bms_serial_no = Column(String)
    bms_master_software_version = Column(String)
    bms_slave_software_version = Column(String)
    watt_hours_to_discharge = Column(Integer)
    watt_hours_to_charge = Column(Integer)
    min_cell_millivolts = Column(Integer)
    max_cell_millivolts = Column(Integer)
    front_power_temperature = Column(Integer)

    temperature_warning = Column(Boolean)
    temperature_fault = Column(Boolean)
    high_current_warning = Column(Boolean)
    high_current_fault = Column(Boolean)
    high_voltage_warning = Column(Boolean)
    high_voltage_fault = Column(Boolean)
    low_voltage_warning = Column(Boolean)
    low_voltage_fault = Column(Boolean)
    low_voltage_non_recoverable_fault = Column(Boolean)
    charge_low_warning = Column(Boolean)
    module_communication_error = Column(Boolean)
    bms_self_check_warning = Column(Boolean)
    under_volt_disable = Column(Boolean)
    over_volt_disable = Column(Boolean)
    string_contactor_on = Column(Boolean)

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
        'temperature_warning':               '10000000000000000000000000000000',
        'temperature_fault':                 '01000000000000000000000000000000',
        'high_current_warning':              '00100000000000000000000000000000',
        'high_current_fault':                '00010000000000000000000000000000',
        'high_voltage_warning':              '00001000000000000000000000000000',
        'high_voltage_fault':                '00000100000000000000000000000000',
        'low_voltage_warning':               '00000010000000000000000000000000',
        'low_voltage_fault':                 '00000001000000000000000000000000',
        'low_voltage_non_recoverable_fault': '00000000100000000000000000000000',
        'charge_low_warning':                '00000000000010000000000000000000',
        'module_communication_error':        '00000000000001000000000000000000',
        'bms_self_check_warning':            '00000000000000100000000000000000',
        'under_volt_disable':                '00000000000000010000000000000000',
        'over_volt_disable':                 '00000000000000001000000000000000',
        'string_contactor_on':               '00000000000000000100000000000000'
    }

    SAMPLE_DATA = {
        'protocol_id': '001',
        'message_type': 'S',
        'message_length': '122',
        'message_id': '078',
        'string_id': '00',
        'state': 'I',
        'state_of_charge': '053',
        'temperature': '020',
        'voltage': '025840',
        'amperes': '00003',
        'alarm_and_status': '80000000',
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
    def __init__(self, options):
        for key in self.ATTRIBUTE_KEYS:
            setattr(self, key, options[key].strip())

        setattr(self, 'alarm_and_status', int(options["alarm_and_status"].strip(), 16))

        for key in self.ALARM_AND_STATUS_BITMASKS:
            setattr(self, key, self.parse_alarm_or_status_by_name(key))

    def parse_alarm_or_status_by_name(self, code):
        bitmask = int(self.ALARM_AND_STATUS_BITMASKS[code], 2)
        return (bitmask & self.alarm_and_status) > 0
