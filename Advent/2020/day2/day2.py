def part_one():
  vaild = 0
  with open('rules.txt', 'r') as f:
    rules = f.readlines()
  for rule in rules:
    ru,password = rule.split(":")
    minmax, char = ru.split(" ")
    minc,maxc = minmax.split("-")
    count = password.count(char)
    if int(minc) <= count and count <= int(maxc):
      vaild = vaild+1
  print(vaild)
def part_two():
  vaild = 0
  with open('rules.txt', 'r') as f:
    rules = f.readlines()
  for rule in rules:
    ru,password = rule.split(":")
    minmax, char = ru.split(" ")
    minc,maxc = minmax.split("-")
    if password[int(minc)] == char:
      if password[int(maxc)] != char:
        vaild = vaild+1
    if password[int(maxc)] == char:
      if password[int(minc)] != char:
        vaild = vaild+1
  print(vaild)
if __name__ == "__main__":
  part_one()
  part_two()
