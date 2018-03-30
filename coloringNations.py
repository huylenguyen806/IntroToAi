import random
import sys
from enum import Enum

class IndexUSA(Enum):
    WASHINGTON = 0
    OREGON = 1
    CALIFORNIA = 2
    NEVADA = 3
    IDAHO = 4
    UTAH = 5
    ARIZONA = 6
    MONTANA = 7
    WYOMING = 8
    COLORADO = 9
    NEW_MEXICO = 10
    TEXAS = 11
    OKLAHOMA = 12
    KANSAS = 13
    NEBRASKA = 14
    SOUTH_DAKOTA = 15
    NORTH_DAKOTA = 16
    MINNESOTA = 17
    IOWA = 18
    MISSOURI = 19
    ARKANSAS = 20
    LOUISIANA = 21
    MISSISSIPPI = 22
    ILLINOIS = 23
    WISCONSIN = 24
    MICHIGAN = 25
    INDIANA = 26
    KENTUCKY = 27
    TENNESSEE = 28
    ALABAMA = 29
    FLORIDA = 30
    GEORGIA = 31
    SOUTH_CAROLINA = 32
    NORTH_CAROLINA = 33
    VIRGINIA = 34
    WEST_VIRGINIA = 35
    OHIO = 36
    PENNSYLVANIA = 37
    MARYLAND = 38
    DELAWARE = 39
    NEW_JERSEY = 40
    NEW_YORK = 41
    CONNECTICUT = 42
    RHODE_ISLAND = 43
    MASSACCHUSETTS = 44
    VERMONT = 45
    NEW_HAMPSHIRE = 46
    MAINE = 47
    ALASKA = 48
    HAWAII = 49

#class IndexVN(Enum):



class Nation:
    NStates = None
    list_states = None
    value = None

    def __init__(self, n, color_code):
        self.NStates = n
        self.list_states = [color_code for i in range(n)]

    def changeColor(self, index, color_code):
        if(self.list_states[index] == color_code):
            return False
        self.list_states[index] = color_code
        return True
    def calValueUSA(self):
        count = 0
        if(self.list_states[IndexUSA.WASHINGTON] == self.list_states[IndexUSA.OREGON]):
            count += 1
        if(self.list_states[IndexUSA.WASHINGTON] == self.list_states[IndexUSA.IDAHO]):
            count += 1
        if(self.list_states[IndexUSA.OREGON] == self.list_states[IndexUSA.CALIFORNIA]):
            count += 1
        if(self.list_states[IndexUSA.OREGON] == self.list_states[IndexUSA.IDAHO]):
            count += 1
        if(self.list_states[IndexUSA.OREGON] == self.list_states[IndexUSA.NEVADA]):
            count += 1
        if(self.list_states[IndexUSA.CALIFORNIA] == self.list_states[IndexUSA.NEVADA]):
            count += 1
        if(self.list_states[IndexUSA.CALIFORNIA] == self.list_states[IndexUSA.ARIZONA]):
            count += 1
        if(self.list_states[IndexUSA.NEVADA] == self.list_states[IndexUSA.IDAHO]):
            count += 1
        if(self.list_states[IndexUSA.NEVADA] == self.list_states[IndexUSA.UTAH]):
            count += 1
        if(self.list_states[IndexUSA.NEVADA] == self.list_states[IndexUSA.ARIZONA]):
            count += 1
        if(self.list_states[IndexUSA.IDAHO] == self.list_states[IndexUSA.MONTANA]):
            count += 1
        if(self.list_states[IndexUSA.IDAHO] == self.list_states[IndexUSA.UTAH]):
            count += 1
        if(self.list_states[IndexUSA.IDAHO] == self.list_states[IndexUSA.WYOMING]):
            count += 1
        if(self.list_states[IndexUSA.UTAH] == self.list_states[IndexUSA.WYOMING]):
            count += 1
        if(self.list_states[IndexUSA.UTAH] == self.list_states[IndexUSA.COLORADO]):
            count += 1
        if(self.list_states[IndexUSA.UTAH] == self.list_states[IndexUSA.ARIZONA]):
            count += 1
        if(self.list_states[IndexUSA.ARIZONA] == self.list_states[IndexUSA.NEW_MEXICO]):
            count += 1
        if(self.list_states[IndexUSA.NEW_MEXICO] == self.list_states[IndexUSA.COLORADO]):
            count += 1
        if(self.list_states[IndexUSA.NEW_MEXICO] == self.list_states[IndexUSA.OKLAHOMA]):
            count += 1
        if(self.list_states[IndexUSA.NEW_MEXICO] == self.list_states[IndexUSA.TEXAS]):
            count += 1
        if(self.list_states[IndexUSA.COLORADO] == self.list_states[IndexUSA.WYOMING]):
            count += 1
        if(self.list_states[IndexUSA.COLORADO] == self.list_states[IndexUSA.NEBRASKA]):
            count += 1
        if(self.list_states[IndexUSA.COLORADO] == self.list_states[IndexUSA.KANSAS]):
            count += 1
        if(self.list_states[IndexUSA.COLORADO] == self.list_states[IndexUSA.OKLAHOMA]):
            count += 1
        if(self.list_states[IndexUSA.WYOMING] == self.list_states[IndexUSA.MONTANA]):
            count += 1
        if(self.list_states[IndexUSA.WYOMING] == self.list_states[IndexUSA.NEBRASKA]):
            count += 1
        if(self.list_states[IndexUSA.WYOMING] == self.list_states[IndexUSA.SOUTH_DAKOTA]):
            count += 1
        if(self.list_states[IndexUSA.MONTANA] == self.list_states[IndexUSA.SOUTH_DAKOTA]):
            count += 1
        if(self.list_states[IndexUSA.MONTANA] == self.list_states[IndexUSA.NORTH_DAKOTA]):
            count += 1
        if(self.list_states[IndexUSA.NORTH_DAKOTA] == self.list_states[IndexUSA.SOUTH_DAKOTA]):
            count += 1
        if(self.list_states[IndexUSA.NORTH_DAKOTA] == self.list_states[IndexUSA.MINNESOTA]):
            count += 1
        if(self.list_states[IndexUSA.SOUTH_DAKOTA] == self.list_states[IndexUSA.MINNESOTA]):
            count += 1
        if(self.list_states[IndexUSA.SOUTH_DAKOTA] == self.list_states[IndexUSA.NEBRASKA]):
            count += 1
        if(self.list_states[IndexUSA.SOUTH_DAKOTA] == self.list_states[IndexUSA.IOWA]):
            count += 1
        if(self.list_states[IndexUSA.NEBRASKA] == self.list_states[IndexUSA.KANSAS]):
            count += 1
        if(self.list_states[IndexUSA.NEBRASKA] == self.list_states[IndexUSA.IOWA]):
            count += 1
        if(self.list_states[IndexUSA.NEBRASKA] == self.list_states[IndexUSA.MISSOURI]):
            count += 1
        if(self.list_states[IndexUSA.KANSAS] == self.list_states[IndexUSA.OKLAHOMA]):
            count += 1
        if(self.list_states[IndexUSA.KANSAS] == self.list_states[IndexUSA.MISSOURI]):
            count += 1
        if(self.list_states[IndexUSA.OKLAHOMA] == self.list_states[IndexUSA.TEXAS]):
            count += 1
        if(self.list_states[IndexUSA.OKLAHOMA] == self.list_states[IndexUSA.MISSOURI]):
            count += 1
        if(self.list_states[IndexUSA.OKLAHOMA] == self.list_states[IndexUSA.ARKANSAS]):
            count += 1
        if(self.list_states[IndexUSA.TEXAS] == self.list_states[IndexUSA.LOUISIANA]):
            count += 1
        if(self.list_states[IndexUSA.TEXAS] == self.list_states[IndexUSA.ARKANSAS]):
            count += 1
        if(self.list_states[IndexUSA.LOUISIANA] == self.list_states[IndexUSA.ARKANSAS]):
            count += 1
        if(self.list_states[IndexUSA.LOUISIANA] == self.list_states[IndexUSA.MISSISSIPPI]):
            count += 1
        if(self.list_states[IndexUSA.ARKANSAS] == self.list_states[IndexUSA.MISSISSIPPI]):
            count += 1
        if(self.list_states[IndexUSA.ARKANSAS] == self.list_states[IndexUSA.MISSOURI]):
            count += 1
        if(self.list_states[IndexUSA.ARKANSAS] == self.list_states[IndexUSA.TENNESSEE]):
            count += 1
        if(self.list_states[IndexUSA.MISSOURI] == self.list_states[IndexUSA.IOWA]):
            count += 1
        if(self.list_states[IndexUSA.MISSOURI] == self.list_states[IndexUSA.ILLINOIS]):
            count += 1
        if(self.list_states[IndexUSA.MISSOURI] == self.list_states[IndexUSA.KENTUCKY]):
            count += 1
        if(self.list_states[IndexUSA.MISSOURI] == self.list_states[IndexUSA.TENNESSEE]):
            count += 1
        if(self.list_states[IndexUSA.IOWA] == self.list_states[IndexUSA.MINNESOTA]):
            count += 1
        if(self.list_states[IndexUSA.IOWA] == self.list_states[IndexUSA.WISCONSIN]):
            count += 1
        if(self.list_states[IndexUSA.IOWA] == self.list_states[IndexUSA.ILLINOIS]):
            count += 1
        if(self.list_states[IndexUSA.MINNESOTA] == self.list_states[IndexUSA.WISCONSIN]):
            count += 1
        if(self.list_states[IndexUSA.WISCONSIN] == self.list_states[IndexUSA.ILLINOIS]):
            count += 1
        if(self.list_states[IndexUSA.WISCONSIN] == self.list_states[IndexUSA.MICHIGAN]):
            count += 1
        if(self.list_states[IndexUSA.ILLINOIS] == self.list_states[IndexUSA.INDIANA]):
            count += 1
        if(self.list_states[IndexUSA.ILLINOIS] == self.list_states[IndexUSA.KENTUCKY]):
            count += 1
        if(self.list_states[IndexUSA.MISSISSIPPI] == self.list_states[IndexUSA.TENNESSEE]):
            count += 1
        if(self.list_states[IndexUSA.MISSISSIPPI] == self.list_states[IndexUSA.ALABAMA]):
            count += 1
        if(self.list_states[IndexUSA.ALABAMA] == self.list_states[IndexUSA.TENNESSEE]):
            count += 1
        if(self.list_states[IndexUSA.ALABAMA] == self.list_states[IndexUSA.GEORGIA]):
            count += 1
        if(self.list_states[IndexUSA.ALABAMA] == self.list_states[IndexUSA.FLORIDA]):
            count += 1
        if(self.list_states[IndexUSA.TENNESSEE] == self.list_states[IndexUSA.GEORGIA]):
            count += 1
        if(self.list_states[IndexUSA.TENNESSEE] == self.list_states[IndexUSA.NORTH_CAROLINA]):
            count += 1
        if(self.list_states[IndexUSA.TENNESSEE] == self.list_states[IndexUSA.KENTUCKY]):
            count += 1
        if(self.list_states[IndexUSA.TENNESSEE] == self.list_states[IndexUSA.VIRGINIA]):
            count += 1
        if(self.list_states[IndexUSA.KENTUCKY] == self.list_states[IndexUSA.INDIANA]):
            count += 1
        if(self.list_states[IndexUSA.KENTUCKY] == self.list_states[IndexUSA.OHIO]):
            count += 1
        if(self.list_states[IndexUSA.KENTUCKY] == self.list_states[IndexUSA.WEST_VIRGINIA]):
            count += 1
        if(self.list_states[IndexUSA.KENTUCKY] == self.list_states[IndexUSA.VIRGINIA]):
            count += 1
        if(self.list_states[IndexUSA.INDIANA] == self.list_states[IndexUSA.OHIO]):
            count += 1
        if(self.list_states[IndexUSA.INDIANA] == self.list_states[IndexUSA.MICHIGAN]):
            count += 1
        if(self.list_states[IndexUSA.MICHIGAN] == self.list_states[IndexUSA.OHIO]):
            count += 1
        if(self.list_states[IndexUSA.OHIO] == self.list_states[IndexUSA.PENNSYLVANIA]):
            count += 1
        if(self.list_states[IndexUSA.OHIO] == self.list_states[IndexUSA.WEST_VIRGINIA]):
            count += 1
        if(self.list_states[IndexUSA.WEST_VIRGINIA] == self.list_states[IndexUSA.VIRGINIA]):
            count += 1
        if(self.list_states[IndexUSA.WEST_VIRGINIA] == self.list_states[IndexUSA.MARYLAND]):
            count += 1
        if(self.list_states[IndexUSA.WEST_VIRGINIA] == self.list_states[IndexUSA.PENNSYLVANIA]):
            count += 1
        if(self.list_states[IndexUSA.VIRGINIA] == self.list_states[IndexUSA.MARYLAND]):
            count += 1
        if(self.list_states[IndexUSA.VIRGINIA] == self.list_states[IndexUSA.NORTH_CAROLINA]):
            count += 1
        if(self.list_states[IndexUSA.NORTH_CAROLINA] == self.list_states[IndexUSA.GEORGIA]):
            count += 1
        if(self.list_states[IndexUSA.NORTH_CAROLINA] == self.list_states[IndexUSA.SOUTH_CAROLINA]):
            count += 1
        if(self.list_states[IndexUSA.SOUTH_CAROLINA] == self.list_states[IndexUSA.GEORGIA]):
            count += 1
        if(self.list_states[IndexUSA.GEORGIA] == self.list_states[IndexUSA.FLORIDA]):
            count += 1
        if(self.list_states[IndexUSA.MARYLAND] == self.list_states[IndexUSA.PENNSYLVANIA]):
            count += 1
        if(self.list_states[IndexUSA.MARYLAND] == self.list_states[IndexUSA.DELAWARE]):
            count += 1
        if(self.list_states[IndexUSA.DELAWARE] == self.list_states[IndexUSA.PENNSYLVANIA]):
            count += 1
        if(self.list_states[IndexUSA.DELAWARE] == self.list_states[IndexUSA.NEW_JERSEY]):
            count += 1
        if(self.list_states[IndexUSA.PENNSYLVANIA] == self.list_states[IndexUSA.NEW_JERSEY]):
            count += 1
        if(self.list_states[IndexUSA.PENNSYLVANIA] == self.list_states[IndexUSA.NEW_YORK]):
            count += 1
        if(self.list_states[IndexUSA.NEW_YORK] == self.list_states[IndexUSA.NEW_JERSEY]):
            count += 1
        if(self.list_states[IndexUSA.NEW_YORK] == self.list_states[IndexUSA.CONNECTICUT]):
            count += 1
        if(self.list_states[IndexUSA.NEW_YORK] == self.list_states[IndexUSA.MASSACCHUSETTS]):
            count += 1
        if(self.list_states[IndexUSA.NEW_YORK] == self.list_states[IndexUSA.VERMONT]):
            count += 1
        if(self.list_states[IndexUSA.CONNECTICUT] == self.list_states[IndexUSA.MASSACCHUSETTS]):
            count += 1
        if(self.list_states[IndexUSA.CONNECTICUT] == self.list_states[IndexUSA.RHODE_ISLAND]):
            count += 1
        if(self.list_states[IndexUSA.MASSACCHUSETTS] == self.list_states[IndexUSA.RHODE_ISLAND]):
            count += 1
        if(self.list_states[IndexUSA.MASSACCHUSETTS] == self.list_states[IndexUSA.VERMONT]):
            count += 1
        if(self.list_states[IndexUSA.MASSACCHUSETTS] == self.list_states[IndexUSA.NEW_HAMPSHIRE]):
            count += 1
        if(self.list_states[IndexUSA.VERMONT] == self.list_states[IndexUSA.NEW_HAMPSHIRE]):
            count += 1
        if(self.list_states[IndexUSA.NEW_HAMPSHIRE] == self.list_states[IndexUSA.MAINE]):
            count += 1
        self.value = count
        return count
        


def ChooseNation():
    choice = 0
    nation = None
    while(choice != 1 or choice != 2):
        print("Choose one of these nations:")
        print("1) America")
        print("2) Viet Nam")
        choice = int(input("Your choice: "))
        if(choice != 1 or choice != 2):
            print("Please choose again!")
    if(choice == 1):
        nation = Nation(50, 1)
    else: nation = Nation(63, 1)
    return nation
    
def HillClimbing(nation):

def GreedySearch(nation):

def AstarSearch(nation):

def main():
    nation = ChooseNation()
