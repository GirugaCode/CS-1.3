from set import Set
import unittest

if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class SetTest(unittest.TestCase):

    def test_init(self):
        test_set = Set(['A','B','C','D'])
        assert test_set.length() == 4
    
    def test_contains(self):
        test_set = Set(['A','B','C','D'])
        assert test_set.length() == 4
        assert test_set.contains('A') == True
        assert test_set.contains('B') == True
        assert test_set.contains('C') == True
        assert test_set.contains('D') == True
        assert test_set.contains('E') == False
        assert test_set.contains('Z') == False

    def test_add(self):
        test_set = Set()
        assert test_set.length() == 0
        test_set.add('A')
        assert test_set.contains('A') == True
        test_set.add('B')
        assert test_set.contains('B') == True
        test_set.add('C')
        assert test_set.contains('C') == True

    def test_remove(self):
        test_set = Set(['A','B','C','D'])
        assert test_set.length() == 4
        test_set.remove('D')
        assert test_set.length() == 3
        assert test_set.contains('D') == False
        test_set.remove('C')
        assert test_set.length() == 2
        assert test_set.contains('C') == False
        test_set.remove('B')
        assert test_set.length() == 1
        assert test_set.contains('B') == False
        test_set.remove('A')
        assert test_set.length() == 0
        assert test_set.contains('A') == False
    
    def test_union(self):
        test_set_one = Set(['A','B','C','D'])
        test_set_two = Set(['E','F','G','H'])
        union = test_set_one.union(test_set_two)
        union_items = union.get_items()
        self.assertCountEqual(union_items, ['A','B','C','D','E','F','G','H'])
    
    def test_intersection(self):
        test_set_one = Set(['A','B','C','D'])
        test_set_two = Set(['A','F','C','H'])
        intersection = test_set_one.difference(test_set_two)
        intersection_items = intersection.get_items()
        self.assertCountEqual(union_items, ['A','C'])
    
    def test_difference(self):
        test_set_one = Set(['A','B','C','D'])
        test_set_two = Set(['A','F','C','H'])
        difference = test_set_one.difference(test_set_two)
        difference_items = difference.get_items()
        self.assertCountEqual(difference_items, ['B', 'D'])
    
    def test_is_subset(self):
        test_set = Set(['A','B','C','D'])
        subset = Set(['A', 'B'])
        assert test_set.is_subset(subset) == True
        subset = Set(['E','F','G'])
        assert test_set.is_subset() == False

if __name__ == '__main__':
    unittest.main()







    
