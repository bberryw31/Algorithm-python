class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        number = num

        thousands = number//1000
        number = number%1000
        roman += "M" * thousands

        hundreds = number//100
        number = number%100
        if hundreds<4:
            roman += "C" * hundreds
        elif hundreds == 4:
            roman += "CD"
        elif hundreds == 5:
            roman += "D"
        elif hundreds<9:
            roman += "D" + "C" * (hundreds - 5)
        else:
            roman += "CM"

        tens = number//10
        number = number%10
        if tens<4:
            roman += "X" * tens
        elif tens == 4:
            roman += "XL"
        elif tens == 5:
            roman += "L"
        elif tens<9:
            roman += "L" + "X" * (tens - 5)
        else:
            roman += "XC"

        ones = number
        if ones<4:
            roman += "I" * ones
        elif ones == 4:
            roman += "IV"
        elif ones == 5:
            roman += "V"
        elif ones<9:
            roman += "V" + "I" * (ones-5)
        else:
            roman += "IX"

        return roman