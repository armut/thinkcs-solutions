# exercise 15.6

class SMS(object):
    has_been_viewed = False
    from_number = ''
    time_arrived = ''
    text_of_SMS = ''

    def __init__(self, from_number, time_arrived, text_of_SMS):
        self.has_been_viewed = False
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_SMS = text_of_SMS

    def __str__(self):
        return self.from_number + " " + self.time_arrived + " "  + self.text_of_SMS


class SMS_store(object):

    messages = []
    size = 0

    def __init__(self):
        self.messages = []
        self.size = 0

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.messages.append(SMS(from_number, time_arrived, text_of_SMS))
        self.size += 1

    def message_count(self):
        return self.size

    def get_unread_indexes(self):
        return [i for i in range(self.size) if not self.messages[i].has_been_viewed]

    def get_message(self, i):
        if i > self.size:
            return None
        print(self.messages[i])
        self.messages[i].has_been_viewed = True

    def delete(self, i):
        del self.messages[i]
        self.size -= 1

    def clear(self):
        del self.messages[:]
        self.size = 0
           

my_inbox = SMS_store()
my_inbox.add_new_arrival("11", "11", "asd")
my_inbox.add_new_arrival("111", "11", "assd")
my_inbox.add_new_arrival("111", "11", "qwer")
my_inbox.add_new_arrival("11", "11", "asda")
my_inbox.delete(2)
my_inbox.get_message(2)
my_inbox.clear()
print("Unread messages: ", my_inbox.get_unread_indexes())
#Although the book recommended to use tuples, here no tuples used.
