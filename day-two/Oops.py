class Team:
    def __init__(self,members=[],name="Noname"):
        self.members=members
        self.name=name
    
    def __add__(self,team2):
        team3=Team()
        
        team3.members.extend(self.members)
        team3.members.extend(team2.members)
        team3.name=self.name+" Combined with "+team2.name
        return team3

    def __repr__(self):
        return "Team: {} and name: {}".format(self.members,self.name)

team1=Team(["Raj","Joseph","Akshar","Arun"],"Angular Development")
print(team1)
team2=Team(["Jackson","Storm","Harry"],"Testing")
print(team2)
team3=team1+team2
print(team3)