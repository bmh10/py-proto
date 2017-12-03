import addressbook_pb2
import google.protobuf.json_format as json_format

def create_person():
  person = addressbook_pb2.Person()
  person.id = 1
  person.name = "John Doe"
  person.email = "jdoe@example.com"
  phone = person.phones.add()
  phone.number = "555-4321"
  phone.type = addressbook_pb2.Person.HOME
  return person

def write(obj):
  f = open("outJson", "w")
  f.write(json_format.MessageToJson(obj))
  f.close()

def read():
  f = open("outJson", "r")
  p = json_format.Parse(f.read(), addressbook_pb2.Person())
  f.close()
  return p

p = create_person()
write(p)
p = read()
print p
