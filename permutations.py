class Permutation():
    def __init__(self, n: int):
        self._size = n
        self.__items = [i for i in range(1, n+1)]    

    @property
    def original(self):
        return self.__items[:]
    
    def permuteby(self, perm: list[tuple], ourlist: list =None) -> list:
        '''
        Provides the resulting list from a given permutation given as a list of tuples.
        Uses (disjoint) cycle notation - please input correctly.
        Default list is [1, 2, ..., n] but can input your own permuted list.
        '''
        if ourlist is None:
            ourlist = self.__items[:]
        else:
            ourlist = ourlist[:]
        if sorted(ourlist) != self.__items:
            raise ValueError('list is wrong size/has duplicates')
        
        newlist = ourlist[:]
        for cycle in perm:
            if len(cycle) < 2:
                continue # trivial cycles are irrelevant
            
            for i, x in enumerate(cycle):
                position = ourlist.index(x)
                newlist[position] = cycle[(1 + i) % len(cycle)]
        return newlist
    
    def find_perm(self, result: list) -> tuple:
        '''
        finds the permutation (using cycle notation) provided the result list
        '''
        if sorted(result) != self.__items:
            raise ValueError('invalid input')
        
        cycle = []
        for i, val in enumerate(result):
            if val != self.__items[i]:
                cycle.append(self.__items[i])

        if not cycle:
            return tuple()
        # now, provided not the identity, cycle is a list of all the items that moved.
        
        start = cycle[0]
        current = start
        visited = []
        while True:
            id = current - 1 
            target = result[id] # finds item at the place of 'current's' original position
            visited.append(current)
            current = target
            if current == start:
                break
        
        return tuple(visited)
        
    def perm_mult(self, perm1: tuple, perm2: tuple) -> tuple:
        '''
        this returns the permutation after applying perm2 then perm1
        '''
        result1 = self.permuteby(perm2)
        result2 = self.permuteby(perm1, result1)
        product = self.find_perm(result2)
        return product

    @staticmethod
    def perm_inv(perm: tuple) -> tuple:
        '''
        this returns the inverse of our permutation
        '''
        # we note that inverse of a cycle is doing it backwards, so we reverse the cycle.
        return tuple(reversed(perm))
    

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
    # evidently, at the moment, we have trouble with disjoint cycles

    l = (1, 3, 5, 4)
    print(Permutation.perm_inv(l))


    # ... permutation
