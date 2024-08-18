class User:
    def __init__(self, id, code):
        self.id = id
        self.code = code
    
    def display(self):
        print(f"product {self.code} is {self.id}")

user1 = User("codetree", 50)
input_id, input_code = input().split()
user2 = User(input_id, int(input_code))

user1.display()
user2.display()