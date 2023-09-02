class Emplyee :
    def __init__(self, name) -> None:
        self.name = name
    def __len__(self):
        x = 0
        for i in self.name:
            x+=1
        return x
    
emplyee  = Emplyee("Ali")
print(len(emplyee))