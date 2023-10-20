import datetime
class Note:
    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime('%m-%d-%Y%j:%M:%S')


note1 = Note('My first note.')
note2 = Note('My second note.')
