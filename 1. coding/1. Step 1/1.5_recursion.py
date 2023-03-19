class Recursion:
    
    def print_name_n_times(self, name, n):
        
        if n == 0:
            return
        print(name)
        # n -= 1
        self.print_name_n_times(name, n -1)
    
    def print_1_to_n(self, n, count=1):
        
        if n + 1== count:
            return
        print(count)
        count += 1
        self.print_1_to_n(n, count=count)
    
    def print_1_to_n_backtracking(self, n):
        if n == 0:
            return 
        self.print_1_to_n_backtracking(n - 1)
        print(n)
        
        
    def print_n_to_1(self, n):
        
        if n == 0:
            return
        print(n)
        self.print_n_to_1(n - 1)
        
    def sumOfSeries(self,N):
        #code here
        if N == 0:
            return 0
        
        sum = N**3 + self.sumOfSeries(N-1)
        return sum
        
    def sum_of_n_numbers(self, n):
        
        if n == 1:
            return 1
        
        return n + self.sum_of_n_numbers(n - 1)
    
    def factorial(self, n):
        
        if n == 0:
            return 1
        
        return n * self.factorial(n - 1)
    
    
    def reverse_an_array(self, _list):
        for i in range(len(_list)// 2):
            temp = _list[len(_list) - 1 - i]
            _list[len(_list) - 1 - i] = _list[i]
            _list[i] = temp
        return _list     
    
    def is_palindrome(self, text: str) -> bool:
        for i in range((_len_str:= len(text)) // 2):
            if text[i] == text[_len_str - 1 - i]:
                continue
            else:
                return False
        return True   
    
    def print_fibonacci_series(self, n):
        if n == 0:
            print(0)
        elif n == 1:
            print("0 1")
        else:
            previous_a = 0
            previous_b = 1
            print(previous_a, previous_b, end=" ")
            for i in range(2, n):
                temp = previous_a + previous_b
                print(temp, end=" ")
                previous_a = previous_b
                previous_b = temp
            
                
recursion = Recursion()
res = recursion.print_fibonacci_series(10)
print(res)