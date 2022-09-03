### composite: Composition is a concept that models a has a relationship.
# It enables creating complex types by combining objects of other types.
# This means that a class Composite can contain an object of another class Component.
class Gun:
    """Simple class for making a gun"""
    def __init__(self, gun_name, gun_type, gun_weight, gun_magazine):
        self._gun_name = gun_name
        self._type = gun_type
        self.weight = gun_weight
        self._magazine = gun_magazine
    
    def __str__(self):
        return f"""Gun info:
        Name: {self.name}
        Type: {self.type}
        Weight: {self.weight} kg
        Magazine: {self.magazine} bullets
        """

    def __dir__(self):
        return ['name', 'type', 'weight', 'magazine']

    def _get_name(self): return self._gun_name
    name = property(fget=_get_name, doc='R-able property')

    def _get_type(self): return self._type
    type = property(fget=_get_type, doc='R-able property')

    def _set_mag(self, value):
        if isinstance(value, int): self._magazine = value
        else: raise ValueError('magazine must be int!')
    def _get_mag(self): return self._magazine
    magazine = property(fget=_get_mag, fset=_set_mag, doc='R&W-able property')

class Soldier:
    """Simple class for making a soldier"""
    def __init__(self, soldier_name, soldier_rank='Sergeant', gun=None):
        self._name = soldier_name
        self._rank = soldier_rank
        if gun is None: self._guns = []
        else: self._guns = [gun]
    
    def __str__(self):
        return f"""Soldier info:
        Name: {self._name}
        Rank: {self._rank}
        Other Guns: {self.guns}
        """
    
    def add_gun(self, new_gun):
        self._guns.append(new_gun)
    
    @property # read-only
    def soldier_name(self):
        return self._name
    
    @property # read-only
    def guns(self):
        guns = ''
        for gun in self._guns:
            guns += f"{gun.name}, "
        return guns

    @property # read
    def rank(self):
        return self._rank
    @rank.setter # write
    def rank(self, new_rank):
        if new_rank in ['Sergeant', 'Capitan', 'General']: self._rank = new_rank
        else: raise ValueError("rank most be in ['Sergeant', 'Capitan', 'General']")

### inheritance: Inheritance models what is called an is a relationship.
# This means that when you have a Derived class that inherits from a Base class,
# you created a relationship where Derived is a specialized version of Base.

## single inheritance:
# what is super()? super() alone returns a temporary object of the superclass that then allows you to call that superclass’s methods.
class M4(Gun):
    """Simple class for making real gun, inherit from Gun"""
    # def __init__(self, fire_rate, price, gun_name, gun_type, gun_weight, gun_magazine):
    #     self._fire_rate = fire_rate
    #     self._price = price
    #     super().__init__(gun_name, gun_type, gun_weight, gun_magazine)

    def __init__(self, fire_rate, price, *args):
        """*args = (
            gun_name: str
            gun_type: str
            gun_weight: int
            gun_magazine: int
        ) for superclass of M4 {}
        """.format(super().__class__)
        self._fire_rate = fire_rate
        self._price = price
        super().__init__(*args) # recommended and sufficient
        # super(M4).__init__(*args)
        # super(M4, self).__init__(*args)
    
    # def __str__(self):
    #     return f"""M4 info:
    #     Name: {super().name}
    #     Type: {super().type}
    #     Weight: {super().weight} kg
    #     Magazine: {super().magazine} bullets
    #     Fire Rate: {self._fire_rate} bullet/s
    #     Price: {self._price} $
    #     """

    def __str__(self):
        return f"""
{super().__str__()}
        Fire Rate: {self._fire_rate} bullet/s
        Price: {self._price} $
        """

## multiple inheritance:
class General(Soldier, Gun):
    """Simple class for making General, inherit from (Soldier, Gun)"""
    def __init__(self, soldier_name, gun_name, gun_type, gun_weight, gun_magazine):
        Gun.__init__(self, gun_name, gun_type, gun_weight, gun_magazine)
        Soldier.__init__(self, soldier_name, soldier_rank='General')
    
    def __str__(self):
        return f"""
        {Soldier.__str__(self)}
        Main Gun:
            {Gun.__str__(self)}
        """

    def add_gun(self, new_gun): # overload method
        self._guns.append(new_gun)
        print(f"{new_gun}Added to guns of {self.soldier_name}")
    
    def remove_gun(self, old_gun):
        self._guns.remove(old_gun)
        print(f"{old_gun}Removed from guns of {self.soldier_name}")
    
    @property
    def main_gun(self):
        return f"""{Gun.__str__(self)}"""

def main():
    smg = Gun('Uzi', 'SMG', 1, 40); print(smg)
    rifle = Gun('Ak-47', 'Rifle', 3, 32); print(rifle)
    colt = Gun('Magnum 44', 'Colt', 1, 6); print(colt)

    soldier = Soldier('Bob. Smith', soldier_rank='Capitan', gun=smg)
    soldier.add_gun(rifle)
    print(soldier)
    print(soldier.guns)
    try: soldier.guns = [colt]
    except AttributeError as AE: print(AE, '\n')
    soldier.add_gun(colt)
    print(soldier.guns)

    M4_A4 = M4(30, 4000, 'M4-A4', 'Rifle', 2, 30)
    print(M4_A4)

    general = General('Frank. Cooper', colt.name, colt.type, colt.weight, colt.magazine)
    general.add_gun(M4_A4)
    print(general)

if __name__ == '__main__':
    main()