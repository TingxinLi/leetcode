#! /usr/bin python3
# -*- encoding: utf-8 -*-

import unittest


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        string_list = str.split()

        if len(pattern) != len(string_list):
            return False

        pat_to_word = {}
        for pat, word in list(zip(pattern, string_list)):
            s_in_pat = pat_to_word.get(pat, None)
            if s_in_pat is not None:
                if s_in_pat != word:
                    return False
            else:
                pat_to_word[pat] = word

        return len(pat_to_word.values()) == len(set(pat_to_word.values()))


class Solution1(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pass


class Tester(unittest.TestCase):

    matcher = Solution()

    def test_match(self):
        self.assertTrue(self.matcher.wordPattern('aaba',
                                                 'apple apple dog apple'))

    def test_not_equal_len(self):
        self.assertFalse(self.matcher.wordPattern('ab', 'apple'))

    def test_not_match(self):
        self.assertFalse(self.matcher.wordPattern('abba',
                                                  'dog cat cat fish'))
        self.assertFalse(self.matcher.wordPattern('abba',
                                                  'dog dog dog dog'))


if __name__ == '__main__':
    unittest.main()
