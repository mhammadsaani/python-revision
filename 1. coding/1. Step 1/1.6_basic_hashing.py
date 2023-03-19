from typing import Dict, List, Tuple

class Hashing:
    
    def array_count_using_hashing(self, number: int, _list: List[int]) -> int:
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
    
    def characters_count_in_string(self, char: str, text: str) -> int:
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
        
    
hashing = Hashing()
# print(hashing.array_count_using_hashing(0, [5, 2, 3, 6, 10, 13, 11, 13]))
print(hashing.characters_count_in_string("a", "a quick brown fox jumps over the lazy dog"))