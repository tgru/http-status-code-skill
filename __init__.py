from mycroft import MycroftSkill, intent_file_handler


class HttpStatusCodeSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.register_entity_file('code.entity')

    @intent_file_handler('code.intent')
    def handle_code_status_http(self, message):
        self.speak_dialog('not.implemented.yet')

def create_skill():
    return HttpStatusCodeSkill()