#################################Extracting Sub-Strings###################################
# Extracting Sub-Strings Practice #1
# Extract the first word of the following sentence using slicing, and display it on the screen:
# "Controlling complexity is the essence of programming"
text='Controlling complexity is the essence of programming'
result=text
print(result.find('Controlling'))
print(result[0:11])
# Hint: "Controlling" is 11 characters long.

# Extracting Sub-Strings Practice #2
# Take every third character starting from the ninth to the end of the sentence, and print the result.
# "Never trust a computer you can't throw out a window"
text1= "Never trust a computer you can't throw out a window"
result2=text1
print(result2[9::3])
# Extracting Sub-Strings Practice #3
# Reverses the position of all the characters in the following sentence and displays the result on the screen.
# "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"
text3= "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"
result3=text3
print(result3[::-1])