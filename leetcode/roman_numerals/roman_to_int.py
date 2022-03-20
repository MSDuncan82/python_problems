
class BadRomanNumeralError:
    """Raised when there is a problem with an input roman numeral"""

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
    
    def roman_to_int(self, roman_string: str) -> int:
        """Convert roman numeral to integer"""
        num_list = self.roman_to_num_list(roman_string)
        signed_nums = self.add_signs(num_list)
        total = sum(signed_nums)
        
        return total

    def single_roman_numeral_to_num(self, roman_numeral: str) -> int:
        """Convert a single roman numeral to an integer"""
        num = self.roman_numeral_lookup.get(roman_numeral)

        if num is None:
            raise BadRomanNumeralError(f"""
            The roman numeral '{roman_numeral}' was not found. Please use one of: {list(self.roman_numeral_lookup.keys())}
            """)

        return num

    def roman_to_num_list(self, roman_string: str) -> list[int]:
        """Convert a roman numeral string to a list of integers"""
        num_list = [self.single_roman_numeral_to_num(rn) for rn in roman_string]

        return num_list

    def add_signs(num_list: list[int]) -> list[int]:
        """
        Multiply the all numbers in a list before the max by -1
        
        [1, 1, 5, 5, 1, 1] -> [-1, -1, 5, 5, 1, 1]
        """
        max_num = max(num_list)
        max_idx = num_list.index(max_num)

        signed_list = [n * -1 if i < max_idx else n for i, n in enumerate(num_list)]
        return signed_list
