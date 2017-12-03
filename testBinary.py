import addressbook_pb2

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
  f = open("out", "wb")
  f.write(obj.SerializeToString())
  f.close()

def read():
  f = open("out", "rb")
  p = addressbook_pb2.Person()
  p.ParseFromString(f.read())
  f.close()
  return p

p = create_person()
write(p)
p = read()
print p
