class Solution:
    def removeDigit(self, number: str, digit: str) -> str:

        max_value = 0

        for i in range(len(number)):
            if number[i] == digit:
                new_number = number[:i] + number[i+1:]
                max_value = max(max_value, int(new_number))


        return str(max_value)

        