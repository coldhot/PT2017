import pickle
import datetime
note = {}
note['to'] = 'Tove'
note['from'] = 'Jani'
note['heading'] = 'Reminder'
note['body'] = "Don't forget me this weekend!"
note['price'] = 123.3
note['list'] = [1, 2, 3, 'asd']

message = {}
message['to'] = '+77015209278'
message['from'] = '+77010420001'
message['text'] = 'hello'
message['date'] = str(datetime.datetime.now())

l = []
l.append(note)
l.append(message)

pickle.dump(l, open( "list.pickle", "wb" ) )
