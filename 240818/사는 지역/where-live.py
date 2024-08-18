class User:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city
    
    def display(self):
        print(f"name {self.name}")
        print(f"addr {self.addr}")
        print(f"city {self.city}")

l = []
for i in range(int(input())):
    input_name, input_addr, input_city = input().split()
    person = User(input_name, input_addr, input_city)
    l.append(person)

slow = max(l, key = lambda p: p.name)
slow.display()