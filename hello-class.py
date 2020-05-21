#! usr/bin/env python3


class Duck:
    _sound = 'Quaaack!'
    _walking = 'Walking like a duck.'

    # functions that are associated with a class are called methods.
    # self makes the method an object method. is a reference to the object
    # we can rename it but is common practice to use "self"
    def quack(self):
        print(self._sound)
        return self._sound

    def walk(self):
        print(self._walking)
        return self._walking

    def __str__(self):  # special method for providing the string representation of the object
        return f'The duck says "{self.quack()}" and moves "{self.walk()}"'


class Animal:
    def __init__(self, animal_type, name, sound):  # constructor is used to initialise the object
        # python does not have private vars, so _ is a common practice for indicating this var should not be used
        # outside the setter and getter methods
        self._animal_type = animal_type
        self._name = name
        self._sound = sound

    def animal_type(self):  # getter or accessor of animal type
        return self._animal_type

    def name(self):  # getter or accessor of name
        return self._name

    def sound(self):  # getter or accessor of _sound
        return self._sound


class Animal2:
    def __init__(self, **kwargs):
        # all this vars are using encapsulation, meaning they belong to the object and not to the class.
        # we shouldn't access them outside the class methods. that's why the use the _ convention
        self._animal_type = kwargs['animal_type'] if 'animal_type' in kwargs else 'fish'
        self._name = kwargs['name'] if 'name' in kwargs else 'bob'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'blup'

    def animal_type(self):  # getter or accessor of animal type
        return self._animal_type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


class Animal3:
    def __init__(self, **kwargs):
        # all this vars are using encapsulation, meaning they belong to the object and not to the class.
        # we shouldn't access them outside the class methods. that's why the use the _ convention
        if 'animal_type' in kwargs:
            self._animal_type = kwargs['animal_type']
        if 'name' in kwargs:
            self._name = kwargs['name']
        if 'sound' in kwargs:
            self._sound = kwargs['sound']

    def animal_type(self):  # getter or accessor of animal type
        return self._animal_type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


class Kitten(Animal3):
    def __init__(self, **kwargs):
        self._animal_type = 'kitten'
        if 'animal_type' in kwargs:
            del kwargs['animal_type']
        super().__init__(**kwargs)

    def kill(self, targets):
        print(f'{self.name()} will now kill all {targets}')


def print_animal(o):
    if isinstance(o, Animal) or isinstance(o, Animal2) or isinstance(o, Animal3):
        print('The {} is named "{}" and says "{}".'.format(o.animal_type(), o.name(), o.sound()))


def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    print(donald)
    print()
    a0 = Animal('kitten', 'fluffy', 'rwar')
    a1 = Animal('duck', 'donald', 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal('velociraptor', 'john', 'hello'))
    print()
    print_animal(Animal2(animal_type='dog', name='pepe', sound='woof'))
    print_animal(Animal2())
    print_animal(Animal2(sound='blupblup'))
    print()
    a2 = Kitten(name='snowball', sound='miau')
    print_animal(a2)
    a2.kill('humans')


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT:
# Quaaack!
# Walking like a duck.
# Quaaack!
# Walking like a duck.
# The duck says "Quaaack!" and moves "Walking like a duck."
#
# The kitten is named "fluffy" and says "rwar".
# The duck is named "donald" and says "quack".
# The velociraptor is named "john" and says "hello".
#
# The dog is named "pepe" and says "woof".
# The fish is named "bob" and says "blup".
# The fish is named "bob" and says "blupblup".
#
# The kitten is named "snowball" and says "miau".
# snowball will now kill all humans

