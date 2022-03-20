class Solution:
    roman_numeral_lookup = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    def romanToInt(self, s: str) -> int:
        num_list = self.s_to_list(s)
        signed_nums = self.add_signs(num_list)
        total = sum(signed_nums)
        
        return total
        