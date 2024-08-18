class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second
    
    def display(self):
        print(f"code : {self.code}")
        print(f"color : {self.color}")
        print(f"second : {self.second}")
    

code, color, second = input().split()
bomb = Bomb(code, color, second)
bomb.display()