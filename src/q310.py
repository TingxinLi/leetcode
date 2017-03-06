#! /usr/bin python3
# -*- encoding: utf-8 -*-

import unittest


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        nodes = [set() for i in range(n)]
        for edge in edges:
            nodes[edge[0]].add(edge[1])
            nodes[edge[1]].add(edge[0])

        leaves = [i for i in range(n) if len(nodes[i]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                link_to = nodes[leaf].pop()
                nodes[link_to].remove(leaf)
                if len(nodes[link_to]) == 1:
                    new_leaves.append(link_to)
            leaves = new_leaves

        return leaves


class Tester(unittest.TestCase):

    matcher = Solution()

    def test_match(self):
        self.assertEqual(self.matcher.findMinHeightTrees(4,
                         [[1, 0], [1, 2], [1, 3]]),
                         [1])
        self.assertEqual(self.matcher.findMinHeightTrees(6,
                         [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]),
                         [3, 4])
        self.assertEqual(self.matcher.findMinHeightTrees(1,
                         []),
                         [0])


if __name__ == '__main__':
    unittest.main()
