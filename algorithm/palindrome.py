import re


class Palindrome:
    # palindrome initializer method
    def __init__(self, candidate):
        # input values
        self._candidate = candidate  # input string
        self._length = len(candidate)  # input length
        # analysis values
        self._is_a_palindrome = False  # initialize status
        self._az09 = re.sub(r'[^a-zA-Z0-9]', '', self._candidate)  # alpha numeric characters
        self._analysis = []  # array of tests
        self._tests = 0  # counter of tests performed
        # evaluate for palindrome
        self.is_palindrome()

    # palindrome tester method
    def is_palindrome(self):
        c = self._az09
        # Run loop from 0 to len/2 of string (middle is exit point)
        tests = int(len(c) / 2)
        for i in range(0, tests):
            front = c[i];
            back = c[len(c) - i - 1]
            if front.lower() == back.lower():
                self.logger(front, back, True)
                self._tests += 1
            else:
                self.logger(front, back, False)
                return
        self._is_a_palindrome = True
        return

    # palindrome logging
    def logger(self, front, back, result):
        self._analysis.append({"test": self._tests, "front": front, "back": back, "result": result})

    # getters follow
    @property
    def candidate(self):
        return self._candidate

    @property
    def tests(self):
        return self._tests

    @property
    def isPalindrome(self):
        return self._is_a_palindrome

    @property
    def analysis(self):
        return self._analysis
# Tester Code
if __name__ == "__main__":
    '''Value for testing'''
    '''Constructor of Class object'''
    palindrome = Palindrome(n)

    '''Using getters to obtain data from object'''
    print(f"Palindrome number for {n} = {palindrome.number}")
    print(f"Palindrome series for {n} = {palindrome.list}")

    '''Using method to get data from object'''
    for i in range(n):
        print(f"Fibonacci sequence {i + 1} = {palindrome.get_sequence(i)}")
