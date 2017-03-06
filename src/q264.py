#! /usr/bin python3
# -*- encoding: utf-8 -*-

import unittest


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)
        h_list = [0] * (l + 1)
        for cite in citations:
            if cite > l:
                h_list[-1] += 1
            else:
                h_list[cite] += 1

        h = 0
        for i in range(len(h_list) - 1, -1, -1):
            h += h_list[i]
            if h >= i:
                return i
        return 0


class Tester(unittest.TestCase):

    matcher = Solution()

    def test_hindex(self):
        self.assertEqual(self.matcher.hIndex([3, 0, 6, 1, 5]), 3)
        self.assertEqual(self.matcher.hIndex([6, 6, 6, 6, 6]), 5)
        self.assertEqual(self.matcher.hIndex([1, 1]), 1)


if __name__ == '__main__':
    unittest.main()
