"""
As this is binary character set, the strings match to their numeric counterparts.
"""
class BinaryCharacterSetMapper():

	def getConfig(self, side, char):
        if len(char) < 2:
            print "Error: Incorrect character detected. Setting character to 00"
            char = "00"
		if side == 0:
            return self.getLeftConfig(char)
		else:
            return self.getRightConfig(char)

	def getLeftConfig(self, char):
		print("CharSet: Getting info for left")
		c = char.lower()
		return int(char[0])

	def getRightConfig(self, char):
		print("CharSet: Getting info for right")
		return int(char[1])