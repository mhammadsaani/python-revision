import math

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

    def armstrong_number (self, n):
        """
        An Armstrong number of three digits is an integer such
        that the sum of the cubes of its digits is equal to the
        number itself.
        """
        temp = str(n)
        result = 0
        for i in temp:
            result += int(i) ** 3
            
        return "Yes" if n == result else "No"
    
    def all_divisor(self, n):
        print(1, end=" ")
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                print(i, end=" ")
                if (n // i != i):
                    print(n // i, end=" ")
    
    def is_prime(self, n):
        if n == 1:
            return False
        for x in range(1, y:=int(math.sqrt(n))):
            print(y)
            if n % x == 0:
               return False
        
        return True
                
    
know_basic_math = KnowBasicMath()
result = know_basic_math.all_divisor(36)
print(result)
