class FlashMessage:
    def __init__(self, message, category):
        self.message = message
        self.category = category

class FlashMessageManager:
    def __init__(self):
        self.messages = []

    def add_message(self, message, category):
        flash_message = FlashMessage(message, category)
        self.messages.append(flash_message)

    def get_messages(self):
        return self.messages

    def clear_messages(self):
        self.messages = []

    def get_messages_by_category(self, category):
        return [message for message in self.messages if message.category == category]
