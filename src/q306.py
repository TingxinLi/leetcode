#! /usr/bin python3
# -*- encoding: utf-8 -*-

import unittest


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        l = len(num)
        # this is for python 2 and 3 compatability
        compatable_round = l // 2 + (l % 2 > 0)
        for i in range(1, compatable_round):
            for j in range(i+1, l-i+1):
                first = num[:i]
                second = num[i: j]
                if len(first) > 1 and first[0] == '0' or\
                        len(second) > 1 and second[0] == '0':
                    continue

                if self._is_additive(first, second, num[j:]):
                    return True

        return False

    def _is_additive(self, first, second, rest):
        if rest[0] == '0' and len(rest) > 1 or len(rest) == 0:
            return False

        if int(first) + int(second) == int(rest):
            return True

        for i in range(1, len(rest)):
            if int(first) + int(second) == int(rest[:i]):
                return self._is_additive(second, rest[:i], rest[i:])

        return False


class Tester(unittest.TestCase):

    matcher = Solution()

    def test_match(self):
        self.assertTrue(self.matcher.isAdditiveNumber('123'))
        self.assertTrue(self.matcher.isAdditiveNumber('101'))
        self.assertTrue(self.matcher.isAdditiveNumber('1235813'))
        self.assertTrue(self.matcher.isAdditiveNumber('199100199'))
        self.assertTrue(self.matcher.isAdditiveNumber('211738'))

    def test_not_match(self):
        self.assertFalse(self.matcher.isAdditiveNumber('1203'))


if __name__ == '__main__':
    unittest.main()
