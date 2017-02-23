class StringUtils:

  def isPalindrome(self, word):
    reverse = ""
    for i in range(0,len(word)):
      reverse += str(word[len(word)-(i+1)])
      print "reverse : ", reverse

    return reverse.lower() == word.lower()

  def isPalindromeR(self, word):
    return len(word) <=1 or word[0].lower() == word[len(word)-1].lower() and self.isPalindromeR(word[1:-1])
