from typing import Dict, List, Tuple

class Hashing:
    
    def array_count_using_array_hash(self, number: int, _list: List[int]) -> int:
        max_value = _list[0]
        for current_value in _list:
            if current_value > max_value:
                max_value = current_value
        hash_arr = []
        for value in range(max_value+1):
            hash_arr.append(0)
        for value in _list:
            hash_arr[value] += 1
        return hash_arr[number] if number < len(hash_arr) else "Not Found"
    
    def characters_count_in_string_array_hash(self, char: str, text: str) -> int:
        if type(char) == int:
            return "Not found" 
        max_value = ord(text[0])
        for _char in text:
            if ord(_char) > max_value:
                max_value = ord(_char)
        hash_arr = []
        for value in range(max_value+1):
            hash_arr.append(0)
        for _char in text:
            hash_arr[ord(_char)] += 1
        return hash_arr[ord(char)] 
        
    def array_count_using_dict(self, number: int or str, _list: List[int or str]) -> int:
        dic = {}
        # for value in _list:
        #     dic[value] = 0        
        # for value in _list:
        #     dic[value] += 1
        for value in _list:
            dic[value] = dic.get(value, 0) + 1  # get value from dic if not found set value to 0 and add 1 to it
        return dic[number] if number in dic else 0
    
    def frequencey_of_limited_range_array(self,_list, n):
        dic = {}
        for num in _list:
            dic[num] = dic.get(num, 0) + 1
        result_list = []
        for i in range(1, n+1):
            result_list.append(dic.get(i, 0))
        return result_list
    
    
hashing = Hashing()
# print(hashing.array_count_using_array_hash(0, [5, 2, 3, 6, 10, 13, 11, 13]))
# print(hashing.characters_count_in_string_array_hash("a", "a quick brown fox jumps over the lazy dog"))
# print(hashing.array_count_using_dict("e", "a quick brown fox jumps over the lazy dog"))
print(hashing.frequencey_of_limited_range_array([2, 3, 2, 3, 5], 5))