class duck:
    def quack(self):
        print("Quack quack")
class goose:
    def quack(self):
        print("Quack quack")
class dog:
    def bark(self):
        print("Quack quack")
class homie:
    def code(self,behave):
        behave.quack()
behave=duck()
obj=homie()
obj.code(behave)