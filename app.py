a = 150
b = 3
c = a + b

name = "Lucas"
surname = "Mercier"

full_name = name + " " + surname

print(c)
print(full_name)

#Task
#1. Write if else statement to validate if x is larger than y. Return true if yes

x = 10
y = 9

def compare (x,y):
  if x>y :
    return True
  return False

print(compare(10,9))

#2. Write if else statement to validate if x is larger than y and less than b Return true if yes

def compare2 (x,y,b):
  if (x>y) and (x<b):
    return True
  return False

print(compare2(10,9,300)
