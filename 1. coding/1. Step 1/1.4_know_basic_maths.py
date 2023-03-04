class KnowBasicMath:
    
    
    def evenly_divides(self, n: int) -> int:
        """
        Given a number N. Count the number of
        digits in N which evenly divides N.
        Time Complexity log 10 (n) -> meaning what should be the power of 10 that we get n
        """
        N = n
        count = 0
        while(N != 0):
            remainder = N % 10
            if remainder == 0:
                N = N // 10
                continue
            if (int(n % remainder) == 0):
                count += 1
            N = N // 10
        return count

    def reverse_bits(self, n: int) -> int:
        """
           Given a 32 bit number X, reverse its binary
           form and print the answer in decimal.
        """
        temp = '{:033b}'.format(n)
        print(len(temp))
        temp_2 = temp[32:0:-1]
        return int(temp_2, 2)
    
    def reverse_num(self, n: int) -> int:
        reversed_num = 0
        while(n != 0):
            temp = n % 10
            reversed_num = reversed_num * 10 + temp
            n = n // 10
        return reversed_num
    
    def count_digits(self, n: int) -> int:
        count = 0
        while n != 0:
            n = n // 10
            count += 1            
        return count
    
    def count_digits_2(self, n: int) -> int:
        return len(str(n))

    def is_palindrome(self, n: int) -> int:
        reversed_num = self.reverse_num(n)
        return reversed_num == n
    
    def is_palindrome_2(self, n: int) -> int:
        reversed_num = str(n)
        temp = len(reversed_num) 
        reversed_num = reversed_num[temp::-1]
        print(reversed_num)
        return int(reversed_num) == n
    
know_basic_math = KnowBasicMath()
result = know_basic_math.is_palindrome_2(212)
print(result)

# 1000000000000000000000000000000
# 10000000000000000000000000000000