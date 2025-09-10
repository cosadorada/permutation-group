class Permutation():
    def __init__(self, n: int):
        self._size = n
        self.__items = [i for i in range(1, n+1)]    

    @property
    def original(self):
        return self.__items[:]
    
    def permuteby(self, perm: list[tuple], start: list =None) -> list:
        '''
        Provides the resulting list from a given permutation given as a list of tuples.
        Uses (disjoint) cycle notation - please input correctly.
        Default list is [1, 2, ..., n] but can input your own permuted list.
        '''
        if isinstance(perm, tuple):
            perm = [perm]  # allow single cycle input as tuple

        if start is None:
            start = self.__items[:]
        else:
            start = start[:]
        if set(start) != set(self.__items):
            raise ValueError('list is wrong size/has duplicates')
        
        newlist = start[:]
        index_map = {v: i for i, v in enumerate(start)}

        for cycle in perm:
            if len(cycle) < 2:
                continue # trivial cycles are irrelevant
            
            for i, x in enumerate(cycle):
                idx = index_map[x]
                newlist[idx] = cycle[(1 + i) % len(cycle)]
        return newlist
    
    def find_perm(self, result: list) -> list[tuple]:
        '''
        Finds the permutation (in cycle notation, from [1, ..., n]) provided the result list.
        '''
        if set(result) != set(self.__items):
            raise ValueError('invalid input')

        # first find where each item goes
        mapping = {}
        for i, val in enumerate(self.__items):
            new_val = result[i]
            if val != new_val:
                mapping[val] = new_val

        seen = set()
        perm = []

        for beginning in mapping:
            if beginning in seen:
                continue
            tracking = beginning
            cycle = []
            while tracking not in cycle:
                seen.add(tracking)
                cycle.append(tracking)
                tracking = mapping[tracking]
            if len(cycle) > 1:
                perm.append(tuple(cycle))

        return perm
        
    def perm_mult(self, perm1: list[tuple], perm2: list[tuple]) -> list[tuple]:
        '''
        Returns the permutation given by multiplying perm1 * perm2 (that is, applying perm2 then perm1).
        '''
        result1 = self.permuteby(perm2)
        result2 = self.permuteby(perm1, result1)
        product = self.find_perm(result2)
        return product
    
    @staticmethod
    def perm_inv(perm: list[tuple]) -> list[tuple]:
        '''
        Returns the inverse of our permutation.
        '''
        # we note that inverse of a cycle is doing it backwards, so we reverse each cycle.
        return [tuple(reversed(cycle)) for cycle in perm]
    
    @staticmethod
    def normalise(perm: list[tuple]) -> list[tuple]:
        '''
        Orders a permutation, having each cycle start with its smallest element, and cycles by first element.
        '''
        normed = []
        if isinstance(perm, tuple):
            perm = [perm]

        for cycle in perm:
            if len(cycle) == 0:
                continue
            min_index = cycle.index(min(cycle))
            spun = cycle[min_index:] + cycle[:min_index]
            normed.append(tuple(spun))
        
        return sorted(normed)

if __name__ == '__main__':
    b = Permutation(5)
    print(b.original)
    c1 = b.permuteby([(3, 5, 1)])
    print(c1)
    c2 = b.permuteby([(3, 5, 1)], [5, 2, 1, 4, 3]) 
    print(c2)
    print(b.find_perm(c1))
    
    c3 = b.permuteby([(1, 3, 5), (2, 4)])
    print(c3)

    print(b.perm_inv.__doc__)
    d = [1, 4, 5, 2, 3]    
    e = b.find_perm(d)
    print(d, e)

    l = [(1, 3, 5, 4)]
    print(Permutation.perm_inv(l))


    # ... permutation
