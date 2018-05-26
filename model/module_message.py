from sqlalchemy import Column, Boolean, String, Integer, Date, DateTime, func
from base import Base

class ModuleMessage(Base):
    __tablename__ = "module_message"
    
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    protocol_id = Column(String)
    message_type = Column(String)
    message_length = Column(Integer)
    message_id = Column(String)
    string_id = Column(String)
    module_id = Column(String)
    module_state = Column(String)
    module_state_of_change = Column(Integer)
    min_cell_temperature = Column(Integer)
    avg_cell_temperature = Column(Integer)
    max_cell_temperature = Column(Integer)
    module_voltage = Column(Integer)
    min_cell_voltage = Column(Integer)
    avg_cell_voltage = Column(Integer)
    max_cell_voltage = Column(Integer)
    module_amperes = Column(Integer)
    alarm_and_status = Column(Integer)
    module_assembly_revision = Column(String)
    module_serial_no = Column(String)
    master_software_version = Column(String)
    slave_software_version = Column(String)
    max_front_power_conn_temp = Column(Integer)

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
    module_communication_fault = Column(Boolean)
    under_volt_disable = Column(Boolean)
    over_volt_disable = Column(Boolean)
    cell_0_balancing = Column(Boolean)
    cell_1_balancing = Column(Boolean)
    cell_2_balancing = Column(Boolean)
    cell_3_balancing = Column(Boolean)
    cell_4_balancing = Column(Boolean)
    cell_5_balancing = Column(Boolean)
    cell_6_balancing = Column(Boolean)

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
        'module_communication_fault':        '00000000000000100000000000000000',
        'under_volt_disable':                '00000000000000001000000000000000',
        'over_volt_disable':                 '00000000000000000100000000000000',
        'cell_0_balancing':                  '00000000000000000000000010000000',
        'cell_1_balancing':                  '00000000000000000000000001000000',
        'cell_2_balancing':                  '00000000000000000000000000100000',
        'cell_3_balancing':                  '00000000000000000000000000010000',
        'cell_4_balancing':                  '00000000000000000000000000001000',
        'cell_5_balancing':                  '00000000000000000000000000000100',
        'cell_6_balancing':                  '00000000000000000000000000000010'
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
        'alarm_and_status': '80000000',
        'module_assembly_revision': '000',
        'module_serial_no': '1311250000800',
        'master_software_version': '0501',
        'slave_software_version': '0496',
        'max_front_power_conn_temp': '029'
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
