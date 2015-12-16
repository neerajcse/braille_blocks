class CharacterSetMapper():
    def __init__(self):
        self.mappings = {
            "a": 40, "b": 60, "c": 44, "d": 46,
            "e": 42, "f": 64, "g": 66, "h": 62,
            "i": 24, "j": 26, "k": 50, "l": 70,
            "m": 54, "n": 56, "o": 52, "p": 74,
            "q": 76, "r": 72, "s": 34, "t": 36,
            "u": 51, "v": 71, "w": 27, "x": 55,
            "y": 57, "z": 53,
        }


    def getConfig(self, side, char):
        if side == 0:
            return self.getLeftConfig(char)
        else:
            return self.getRightConfig(char)

    def getLeftConfig(self, char):
        print("CharSet: Getting info for left")
        c = char.lower()
        num = self.mappings[c]
        num = int(num/10)
        return num

    def getRightConfig(self, char):
        print("CharSet: Getting info for right")
        c = char.lower()
        num = self.mappings[c]
        num = num%10
        return num

class EnglishCharacterSet(CharacterSetMapper):
    def __init__(self):
        self.mappings = {
            "a": 40, "b": 60, "c": 44, "d": 46,
            "e": 42, "f": 64, "g": 66, "h": 62,
            "i": 24, "j": 26, "k": 50, "l": 70,
            "m": 54, "n": 56, "o": 52, "p": 74,
            "q": 76, "r": 72, "s": 34, "t": 36,
            "u": 51, "v": 71, "w": 27, "x": 55,
            "y": 57, "z": 53,
        }
