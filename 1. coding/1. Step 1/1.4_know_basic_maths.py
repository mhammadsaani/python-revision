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
    
    
    
know_basic_math = KnowBasicMath()
result = know_basic_math.reverse_bits(1)
print(result)

# 1000000000000000000000000000000
# 10000000000000000000000000000000