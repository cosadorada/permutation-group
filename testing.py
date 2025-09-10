import unittest
from permutations import Permutation

class TestPermutationMethods(unittest.TestCase):
    def setUp(self):
        self.p = Permutation(5)

    def test_permuteby_default(self):
        result = self.p.permuteby([(1, 3, 5), (2, 4)])
        self.assertEqual(result, [3, 4, 5, 2, 1])

    def test_permuteby_custom(self):
        result = self.p.permuteby([(3, 5, 1)], [5, 2, 1, 4, 3])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_identity(self):
        result = self.p.permuteby([])
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_single_cycle(self):
        result = self.p.permuteby([(1, 2, 3, 4, 5)])
        self.assertEqual(result, [2, 3, 4, 5, 1])

    def test_find_perm(self):
        result = self.p.find_perm([1, 4, 5, 2, 3])
        result = Permutation.normalise(result)
        self.assertEqual(result, Permutation.normalise([(4, 2), (3, 5)]))

    def test_perm_mult(self):
        perm1 = [(1, 3, 5)]
        perm2 = [(2, 4)]
        product = self.p.perm_mult(perm1, perm2)
        expected = [(3, 5, 1), (2, 4)]
        expected = Permutation.normalise(expected)
        product = Permutation.normalise(product)
        self.assertEqual(product, expected)

    def test_perm_inv(self):
        perm = [(1, 3, 5), (2, 4)]
        inv = Permutation.perm_inv(perm)
        expected = [(3, 1, 5), (4, 2)]
        expected = Permutation.normalise(expected)
        inv = Permutation.normalise(inv)
        self.assertEqual(inv, expected)

    def check_cycle_equivalence(self):
        perm = [(3, 4, 1), (5, 2)]
        expected = Permutation.normalise(perm)
        test_perm = [(1, 3, 4), (2, 5)]
        self.assertEqual(test_perm, expected)

'''
must create a normalising method, before the other tests will work - cycles are up to reordering.
- DONE
 '''

if __name__ == '__main__':
    unittest.main()