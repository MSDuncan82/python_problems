
from filelock import sys


class BadRomanNumeralError:
    """Raised when there is a problem with an input roman numeral"""

class RomanToInt:
    roman_numeral_lookup = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    def romanToInt(self, roman_string: str) -> int:
        """Convert roman numeral to integer"""
        num_list = self._roman_to_num_list(roman_string)
        signed_nums = self._add_signs(num_list)
        total = sum(signed_nums)
        
        return total

    def _single_roman_numeral_to_num(self, roman_numeral: str) -> int:
        """Convert a single roman numeral to an integer"""
        num = self.roman_numeral_lookup.get(roman_numeral)

        if num is None:
            raise BadRomanNumeralError(f"""
            The roman numeral '{roman_numeral}' was not found. Please use one of: {list(self.roman_numeral_lookup.keys())}
            """)

        return num

    def _roman_to_num_list(self, roman_string: str) -> list[int]:
        """Convert a roman numeral string to a list of integers"""
        num_list = [self._single_roman_numeral_to_num(rn) for rn in roman_string]

        return num_list

    def _add_signs(self, num_list: list[int]) -> list[int]:
        """
        Multiply the all numbers in a list before the max by -1
        
        [1, 1, 5, 5, 1, 1] -> [-1, -1, 5, 5, 1, 1]
        """
        # Find index of max
        max_num = max(num_list)
        max_idx = num_list.index(max_num)

        # Multiply all numbers before max by -1
        signed_list = [n * -1 if i < max_idx else n for i, n in enumerate(num_list)]
        return signed_list

if __name__ == '__main__':
    print(__file__)    
    print(sys.path)