#!python3
from itertools import permutations

# dict = {}						#Create empty dictionary
# file = open("/usr/share/dict/words", "r")		#Open file containing dictionary
# print("Building dictionary . . . ")
# for word in file:					#Iterate through every word in the dictionary
# 	word = word.strip().lower()			#Strip newlines and send to lowercase
# 	sorted_word = ''.join(sorted(word))		#Alphabetically sort the word
# 	if sorted_word in dict:				#Check if sorted_word is already a key
# 		if word not in dict[sorted_word]:	#Make sure word is not already in the list under the key sorted_word
# 			dict[sorted_word].append(word)	#Add to list under the key sorted_word
# 	else:						#If not in dictionary
# 		dict[sorted_word] = [word]		#Create new list with one entry
# while(True):						#Loop until quit is typed
# 	jumble = raw_input("Enter a jumble to decode or 'quit': ")	#Get input
# 	jumble = jumble.lower()				#Send jumble to lower
# 	if(jumble == "quit"):				#Quit if quit is typed
# 		break
# 	jumble = ''.join(sorted(jumble))		#Sort jumble alphabetical
# 	if jumble in dict:				#If sorted jumble exists in dictionary
# 		results = dict[jumble]			#Get list of words that match jumble
# 		for result in results:			#Loop through list printing results
# 			print(result)			#Trailing , designates that there should be a space between entries
# 		print("")				#Print newlines
# 	else:						#Jumble not found in diitctionary print message
# 		print("Results for jumble not found")


def wordJumble(string):
    file = open("/usr/share/dict/words", "r")
    words = file.read().replace('\n', '').lower()
    words_to_list = list(words)
    print(''.join(words_to_list))


    
    perm = permutations(string)
    for word in list(perm):
        # print(''.join(word))
        pass


print(wordJumble("often"))



