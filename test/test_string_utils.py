import unittest

from src.string_utils import StringUtils

class StringUtilsTest(unittest.TestCase):

  def setUp(self):
    print 'Setup method'


  def tearDown(self):
    print 'Teardown method'


  def test_word_is_not_palindrome(self):
    string_utils = StringUtils()
    self.assertEqual(string_utils.isPalindromeR("Hello"), False)

  def test_word_is_palindrome(self):
    string_utils = StringUtils()
    self.assertEqual(string_utils.isPalindromeR("ellE"), True)

  def test_empty_word_is_palindrome(self):
    string_utils = StringUtils()
    self.assertEqual(string_utils.isPalindromeR(""), True)

if __name__ == '__main__':
  unittest.main()
