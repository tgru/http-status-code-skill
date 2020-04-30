from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class HttpStatusCodeSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        return

    @intent_handler(IntentBuilder('').require('code').require('StatusNumber'))
    def handle_code_status_http(self, message):
        code = str(message.data.get('StatusNumber'))

        dialog = code + '.short'
        data = {'code': code}
        if dialog in self.dialog_renderer.templates:
            self.speak_dialog('code.means', data)
            self.speak_dialog(dialog)
        else:
            self.speak_dialog('unknown.code', data)

def create_skill():
    return HttpStatusCodeSkill()