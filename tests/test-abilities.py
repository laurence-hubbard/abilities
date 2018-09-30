from __future__ import absolute_import
import unittest
import sys
sys.path.append(".")
from abilities import abilities


class SuiteOfTests(unittest.TestCase):
    def test_one(self):
        result = abilities([1,2,3])
        expected = ['__delitem__', '__iadd__', '__imul__', '__reversed__', '__setitem__', 'append', 'clear', 'copy', 'extend', 'insert', 'pop', 'remove', 'reverse', 'sort']

        self.assertEqual(expected, result)

if __name__ == '__main__':
  unittest.main()

