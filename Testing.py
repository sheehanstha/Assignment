import unittest
from tkinter import Tk
import FinalAssignment

root2 = Tk()
a = FinalAssignment.Student_info(root2)


class TestNewAlgorithm(unittest.TestCase):
    def test_sort(self):
        a.sortcombo.set('fname')
        array_test = [('Sayhan', 'Shrestha', '9843516693', 'Hacking'),
                          ('Dipendra', 'Mainali', '9803635098', 'Security')]
        expected_result = [('Dipendra', 'Mainali', '9803635098', 'Security'),
                           ('Sayhan', 'Shrestha', '9843516693', 'Hacking')]

        a.sortcombo.set('fname')
        ac_result=a.bubbleSort(array_test)
        self.assertEqual(expected_result,ac_result)


    def test_search(self):
        array_test = [('Sayhan', 'Bhaisepati', '9843516693', 'Hacking'),
                      ('Dipendra', 'Kathmandu', '9803635098', 'Security')]
        expected_result = [('Sayhan', 'Bhaisepati', '9843516693', 'Hacking')]
        a.searchentry.delete(0, 'end')
        a.searchentry.insert(0, 'Sayhan')
        a.searchcombo.set('fname')
        ac_result = a.search(array_test)
        self.assertEqual(expected_result, ac_result)



if __name__ == '__main__':
    unittest.main()
