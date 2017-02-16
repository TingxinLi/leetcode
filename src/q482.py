#! /usr/bin python3
# -*- encoding: utf-8 -*-

import unittest


class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        string = S.replace('-', '')
        first = len(string) % K
        license_list = []
        if first != 0:
            license_list.append(string[:first].upper())
        while (first < len(string)):
            license_list.append(string[first: first+K].upper())
            first += K
        return '-'.join(license_list)


class Tester(unittest.TestCase):

    matcher = Solution()

    def test_match(self):
        self.assertEqual(self.matcher.licenseKeyFormatting("2-4A0r7-4k", 4),
                         '24A0-R74K')
        self.assertEqual(self.matcher.licenseKeyFormatting("2-4A0r7-4k", 3),
                         '24-A0R-74K')


if __name__ == '__main__':
    unittest.main()
