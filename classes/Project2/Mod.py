

class Mod:
    def __init__(self, value, modulus):
        if not isinstance(modulus, int):
            raise TypeError('Unsupported')

        if modulus <= 0 :
            raise TypeError('Unsupported')

        self._modulus = modulus
        self._value = value % self._modulus

    @property
    def value(self):
        return self._value

    @property
    def modulus(self):
        return self._modulus

    def __int__(self):
        return self.value

    def __repr__(self):
        return f'Mod({self.value},{self.modulus})'


    def __eq__(self, other):
        if isinstance(other, Mod):
            if self.modulus != other.modulus:
                return NotImplemented
            else:
                return self.value == other.value
        elif isinstance(other, int):
            return other % self.modulus == self.value
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.value, self.modulus))

    def __neg__(self):
        return Mod(-self.value, self.modulus)


    def __add__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(other.value+ self.value, self.modulus)
        elif isinstance(other, int):
            return Mod(other + self.value, self.modulus)
        else:
            return NotImplemented


    def __sub__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(other.value - self.value, self.modulus)
        elif isinstance(other, int):
            return Mod(self.value - other, self.modulus)
        else:
            return NotImplemented


    def __mull__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(other.value * self.value, self.modulus)
        elif isinstance(other, int):
            return Mod(self.value * other, self.modulus)
        else:
            return NotImplemented



    def __pow__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value ** other.value , self.modulus)
        elif isinstance(other, int):
            return Mod(self.value * (other % self.modulus), self.modulus)
        else:
            return NotImplemented


    def __iadd__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self._value = (other.value+ self.value) % self.modulus
        elif isinstance(other, int):
            self._value = (other + self.value) % self.modulus
        else:
            return NotImplemented


    def __isub__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self._value = (other.value - self.value) % self.modulus
        elif isinstance(other, int):
            self._value = (other - self.value) % self.modulus
        else:
            return NotImplemented

    def __imul__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self._value = (other.value * self.value) % self.modulus
        elif isinstance(other, int):
            self._value = (other * self.value) % self.modulus
        else:
            return NotImplemented

    def __ipow__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self._value = (other.value ** self.value) % self.modulus
        elif isinstance(other, int):
            self._value = (other ** self.value) % self.modulus
        else:
            return NotImplemented


    def __lt__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return  self.value < other.value
        elif isinstance(other, int):
            return  self.value < (other % self.modulus)
        else:
            return NotImplemented



print(Mod(3,12) == Mod(15,12))
print(Mod(3,12) + 12)
print(Mod(3,12) + 25)