# encoding: UTF-8
import random
from abc import Union
import nanoid
import debugging


#
# * Defining static values
#

# ! It's recommended to use Better Commenets

NANOID_LENGTH = 21


MAX_GRASS_GROWTH_LEVEL = 100
RANDOM_MAX = 200  # How small is the chance of something happening
GROWTH_RANDOMBOOST = random.randint(9114, 11412) / 10000
GROWTH_STEP = 1

ANIMAL_TYPES = {  # All default data about animals is provided here
    "not defined": {
        "maxhealth": 0
    },
    "cow": {
        "standart": {
            "maxhealth": "100"
        }
    }
}

global_tick = 0  # Global tick counter


class Grass():
    """Basic grass cell."""

    def __init__(self, posx: int, posy: int, logger):
        self.growthlevel = random.randint(0, MAX_GRASS_GROWTH_LEVEL)
        self.random_tick_trigger = random.randint(0, RANDOM_MAX)
        self._logger = logger

    def __grow(self):
        if self.growthlevel + GROWTH_RANDOMBOOST * GROWTH_STEP > MAX_GRASS_GROWTH_LEVEL:
            self.growthlevel = MAX_GRASS_GROWTH_LEVEL
        else:
            self.growthlevel += GROWTH_RANDOMBOOST * GROWTH_STEP

    def tick(self):
        if random.randint(0, RANDOM_MAX) == self.random_tick_trigger:
            self.__grow()


class Animal():
    """Base class for all animal types."""
    health = 0
    animal_type = None

    def __init__(self, posx: int, posy: int, logger, health=None):
        self.posx = posx
        self.posy = posy
        self.logger = logger
        self.__id = nanoid.generate(NANOID_LENGTH)

        self.maxhealth = ANIMAL_TYPES[self.animal_type if self.animal_type !=
                                      None else "not defined"]["maxhealth"]

        if health != None and health > self.maxhealth:
            raise ValueError("Health for %s is bigger that max health for this type of animal: maximum: %d, given: %d" % (
                self.type, self.maxhealth, health))

        self.health = health

    def tick(self):
        # TODO: Implement tick, hunger and food consumption for animals.
        raise NotImplementedError(
            "Tick system is not yet implemented for %s" % type(self))


class Cow(Animal):
    """Class for cows"""
    animal_type = 'cow'
    breed = None

    def __init__(self, posx: int, posy: int, breed='standart', health=None):
        self.posx = posx
        self.posy = posy
        self.__id = nanoid.generate(NANOID_LENGTH)

        if breed in ANIMAL_TYPES[self.animal_type]:
            self.breed = breed
        else:
            raise ValueError("Breed %s is not defined for %s" %
                             (breed, self.animal_type))

        self.maxhealth = ANIMAL_TYPES[self.animal_type if self.animal_type !=
                                      None else "not defined"][breed]["maxhealth"]

        if health != None and health > self.maxhealth:
            raise ValueError("Health for %s is bigger that max health for this type of animal: maximum: %d, given: %d" % (
                self.type, self.maxhealth, health))

        self.health = health


class Field():
    """Base class for field — the place where all things start"""

    def __init__(self, sizex: int, sizey: int, logger):
        self.sizex = sizex
        self.sizey = sizey
        self.logger = logger
        self.__cells = self.__generate(self.sizex, self.sizey)

        self.__animals = list()

    def add_animal(self, animal: Animal, posx=None, posy=None):
        """Adds an animal to the field. Takes position as an additional argument. Notice: if posx is not given, posy will not be taken into account and vice versa."""
        if animal.posx != None and animal.posy != None:
            if isinstance(posx, int) and isinstance(posy, int):
                animal.posx, animal.posy = posx, posy
            else:
                raise ValueError("posx and posy must be integers. posx type: %s, posy type: %s" % (
                    type(posx), type(posy)))
        self.__animals.append(animal)

    def delete_animal(self, animal=None, id=None):
        """Deletes an animal from the field. Takes either instance of an animal or its unique id."""
        if animal != None or id != None:
            if animal != None:
                if isinstance(animal, Animal):
                    self.__animals.remove(animal)
                    return None
                else:
                    raise ValueError(
                        "%s is not an animal, cannot delete it from the field" % str(type(animal)))
            if id != None:
                if isinstance(id, str):
                    for animal in range(len(self.__animals)):
                        if animal.getid == id:
                            self.__animals.remove(animal)
                            break
                    return None
                else:
                    raise ValueError(
                        "%s is not a valid type for an id of an animal, cannot delete it from the field" % str(type(id)))
        else:
            raise ValueError(
                "Neither animal or id are given appropriately. Nothing to delete.")
        raise

    def __generate(self, sizex, sizey):
        cells = list()
        for y in range(sizey):
            row = list()
            for x in range(sizex):
                row.append(Grass(x, y, self.logger))
            cells.append(row)
        return cells

    def tick(self):
        self.__tick
