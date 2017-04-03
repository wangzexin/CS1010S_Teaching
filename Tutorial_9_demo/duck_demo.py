from random import *

######################
# Class: NamedObject #
######################

class NamedObject(object):
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "<{0} : {1}>".format(self.name, self.__class__.__name__)

#######################
# Class: MobileObject #
#######################

class MobileObject(NamedObject):
    def __init__(self, name, place):
        super().__init__(name)
        self.place = place

    def get_place(self):
        return self.place

######################
# Class: LivingThing #
######################

class LivingThing(MobileObject):
    def __init__(self, name, health, threshold):
        super().__init__(name, None)
        self.health = health
        self.threshold = threshold

    def get_threshold(self):
        return self.threshold

    def get_health(self):
        ''' Returns the current health of this living thing. '''
        return self.health

    def add_health(self, health):
        self.health = min(100, self.health+health)

    def reduce_health(self, health):
        self.health = max(0, self.health-health)
        if self.health == 0:
            self.go_to_heaven()

    def go_to_heaven(self):
        self.place.del_object(self)
        heaven.add_object(self)
        print(self, "went to heaven!")
        return True

    def move_to(self, new_place):
        ''' Move to an adjacent place '''
        old_place = self.place
        if new_place in old_place.neighbor_dict.values():
            old_place.del_object(self)
            new_place.add_object(self)
            print("{0} moves from {1} to {2}".format(self.name, old_place, new_place))
        else:
            print("{0} cannot move from {1} to {2}".format(self.name, old_place, new_place))

    def act(self):
        if self.threshold >= 0 and randint(0, self.threshold) == 0:
            new_place = random_neighbor(self.place)
            if new_place:
                self.move_to(new_place)


## New class
class Duck(LivingThing):
    def __init__(self, name, health, threshold, duckType):
        super().__init__(name, health, threshold)
        self.duckType = duckType

    def getDuckType(self):
        return self.duckType

    def __eq__(self, other):
        if isinstance(other, Duck):
            if self.get_name() == other.get_name():
                if self.getDuckType() == other.getDuckType():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

## New class again

class FlyableDuck(Duck):
    def fly(self):
        print(self.name + " is flying!")

class SwimmableDuck(Duck):
    def swim(self):
        print(self.name + " is swimming!")

class FlySwimDuck(FlyableDuck, SwimmableDuck):
    pass
