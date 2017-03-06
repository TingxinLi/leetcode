#! /usr/bin python3
# -*- encoding: utf-8 -*-

import unittest


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        while num != 1:
            if num % 2 == 0:
                num /= 2
                continue
            if num % 3 == 0:
                num /= 3
                continue
            if num % 5 == 0:
                num /= 5
                continue
            return False
        return True


class Tester(unittest.TestCase):

    matcher = Solution()

    def test_ugly(self):
        self.assertTrue(self.matcher.isUgly(6))
        self.assertTrue(self.matcher.isUgly(8))
        self.assertTrue(self.matcher.isUgly(1))

    def test_not_ugly(self):
        self.assertFalse(self.matcher.isUgly(14))
        self.assertFalse(self.matcher.isUgly(0))


if __name__ == '__main__':
    unittest.main()
