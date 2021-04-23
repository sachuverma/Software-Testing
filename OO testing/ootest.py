import pytest
from oo import Cricketer, Footballer, HockeyPlayer

class TestCricketer:
    def test_info(self):
        x=Cricketer('Rohit', 10, 10)
        print("Testing info : Cricketer")
        assert ('Rohit',10,10)==(x.name,x.matches,x.skill)
    def test_score(self):
        x=Cricketer('Rohit', 10, 10)
        print("Testing score : Cricketer")
        assert x.get_score()==150

class TestFootballer:
    def test_info(self):
        x=Footballer('Neymar', 10, 10)
        print("Testing info : Footballer")
        assert ('Neymar',10,10)==(x.name,x.matches,x.skill)
    def test_score(self):
        x=Footballer('Neymar', 10, 10)
        print("Testing score : Footballer")
        assert x.get_score()==6
        
class TestHockerPlayer:
    def test_info(self):
        x=HockeyPlayer('Dhyan Chand', 10, 10)
        print("Testing info : HockerPlayer")
        assert ('Dhyan Chand',10,10)==(x.name,x.matches,x.skill)
    def test_score(self):
        x=HockeyPlayer('Dhyan Chand', 10, 10)
        print("Testing score : HockerPlayer")
        assert x.get_score()==5