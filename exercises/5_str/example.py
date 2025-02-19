#things are one of the most though out features in python
#these are all the methods that can be used on strings

#first lets define our string
harlee = "quantum computing is fun..."

#string modifiers there are alot more but 
#these are the ones that matter the most

harlee.lower()                         # sets all characters to lower 
harlee.upper()                         # sets all characters to upper
harlee.find("quantum")                 # gives the index to the first instance of the given word
harlee.replace("Python", "Java")       # replaces the first string with the second in your code
harlee.strip()                         # removes all whitespace
harlee.split()                         # breaks up the string into a list, can use custom seperators like .split(":")


luke = "luke is really handsome"

# in luke[0:5] the brackets specify that we are getting the 
# characters between 0 and 5 in the list of characters

newstr = luke[0:5] + harlee[18:27] 

print(newstr)


