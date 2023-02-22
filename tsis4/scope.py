//
def myfunc():
  x = 300
  print(x)

myfunc()

//
def myfunc():
  global x
  x = 300

myfunc()

print(x)

//
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)
