#File IO. Useful method: "hello,world".split(",")
birthday = []
with open('birthday.txt', 'r') as file:
  for line in file:
    birthday.append (line.rstrip())

print(birthday)
