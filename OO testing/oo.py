class Sportsman:
    name = ""
    def __init__(self):
        print("In Base Class")
    def get_score(self):
        print("Score")
        pass

class Cricketer(Sportsman):
    matches = 0
    skill = 0 
    def __init__(self,n,c,s):
        self.name=n
        self.matches=c
        self.skill=s
    def print_info(self):
        print("name : "+ str(self.name))
        print("matches : "+ str(self.matches))
        print("skill : "+ str(self.skill))
    def get_score(self):
        return  int((self.matches*self.skill*2)/1.33)

class Footballer(Sportsman):
    matches = 0
    skill = 0
    def __init__(self,n,c,s):
        self.name=n
        self.matches=c
        self.skill=s
    def print_info(self):
        print("name : "+ str(self.name))
        print("matches : "+ str(self.matches))
        print("skill : "+ str(self.skill))
    def get_score(self):
        return int((self.matches+self.skill)/3)

class HockeyPlayer(Sportsman):
    matches = 0
    skill = 0
    def __init__(self,n,c,s):
        self.name=n
        self.matches=c
        self.skill=s
    def print_info(self):
        print("name : "+ str(self.name))
        print("matches : "+ str(self.matches))
        print("skill : "+ str(self.skill))
    def get_score(self):
        return int((self.matches+self.skill+2)/4)

def main():
    c1=Cricketer('Sachin',10,10)
    c1.print_info()
    print("Score : ",c1.get_score())

    f1=Footballer('Ronaldo',10,10)
    f1.print_info()
    print("Goal : ",f1.get_score())
    
    h1=HockeyPlayer('Dhyan Chand',10,10)
    h1.print_info()
    print("Goal : ",h1.get_score())

if __name__=='__main__':
    main()