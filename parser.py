class Parser:
    import csv
    import message

    def __init__(self, message_string):
        self.reader = csv.reader([message_string], delimiter=',')

    def message_array(self):
        if len(self.message_array_memo) > 0:
            return self.message_array_memo
        else:
            self.message_array_memo = next(self.reader)
            return self.message_array_memo

    def message_dict(self):
        zip(Message.ATTRIBUTE_KEYS, self.message_array)

    def message(self):
        return Message(message_dict)
