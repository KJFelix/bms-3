import csv
from model.string_message import StringMessage
from model.module_message import ModuleMessage

class Parser:
    STRING_TYPE = 'S'
    MODULE_TYPE = 'M'
    
    message_array_memo = []
    reader_memo = None

    def __init__(self, message_string):
        self.message_string = message_string

    def reader(self):
        if self.reader_memo is None:
            self.reader_memo = csv.reader([self.message_string], delimiter=',')
        return self.reader_memo

    def message_array(self):
        if len(self.message_array_memo) <= 0:
            self.message_array_memo = next(self.reader())
        return self.message_array_memo

    def message_type(self):
        return self.message_array()[1].strip()

    def message_dict(self):
        if self.message_type() == self.STRING_TYPE:
            return dict(zip(StringMessage.ATTRIBUTE_KEYS, self.message_array()))
        else if self.message_type() == self.MODULE_TYPE:
            return dict(zip(ModuleMessage.ATTRIBUTE_KEYS, self.message_array()))

    def message(self):
        print(self.message_type)
        if self.message_type() == self.STRING_TYPE:
            return StringMessage(self.message_dict())
        else if self.message_type() == self.MODULE_TYPE:
            return ModuleMessage(self.message_dict())
