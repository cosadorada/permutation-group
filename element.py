from permutations import Permutation


class PermutationElement():
    def __init__(self, perm: list[tuple], k: Permutation):
        self._group = k
        self._perm = Permutation.normalise(perm)
        self.inline = k.permuteby(perm)
    
    def __mul__(self, other):
        '''Permutation multiplication: self * other means apply other, then self.'''
        if self._group != other._group:
            raise ValueError('cannot multiply elements of different groups')
        
        new_perm = self._group.perm_mult(self._perm, other._perm)
        return PermutationElement(new_perm, self._group)

    def __repr__(self):
        return f'PermutationElement({self._perm})'
    