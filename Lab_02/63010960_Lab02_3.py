class TorKham:

	def __init__(self):
		self.words = []

	def restart(self):
		self.words = []
		return "game restarted"

	def play(self, word):
		if self.words == [] :
			self.words.append(word)
			return self.words
		elif str(self.words[len(self.words) - 1][len(self.words[len(self.words) - 1]) - 2:]).lower() == str(word[0:2]).lower():
    		
			self.words.append(word)
			return self.words
		else:
			return "game over"



torkham = TorKham()

print("*** TorKham HanSaa ***")


S = input("Enter Input : ").split(',')

for i in range(len(S)):
	if S[i][0] == "P":
		print("\'",S[i][2:],"\' -> ",torkham.play(S[i][2:]),sep="")
	elif S[i][0] == "R":
		print(torkham.restart())
	elif S[i][0] == "X":
		break
	else:
		print("\'",S[i][:],"\' is Invalid Input !!!",sep="")
		break