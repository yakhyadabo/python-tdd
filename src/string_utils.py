class StringUtils:

  def isPalindrome(self, word):
    reverse = ""
    for i in range(0,len(word)):
      reverse += str(word[len(word)-(i+1)])
      print "reverse : ", reverse

    return reverse.lower() == word.lower()