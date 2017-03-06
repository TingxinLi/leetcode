#! /usr/bin python3
# -*- encoding: utf-8 -*-

import unittest


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return num % 9 if num % 9 != 0 else 9


class Tester(unittest.TestCase):

    matcher = Solution()

    def test_ugly(self):
        self.assertEqual(self.matcher.addDigits(38), 2)
        self.assertEqual(self.matcher.addDigits(112), 4)
        self.assertEqual(self.matcher.addDigits(123456789), 9)
        self.assertEqual(self.matcher.addDigits(0), 0)


if __name__ == '__main__':
    unittest.main()
