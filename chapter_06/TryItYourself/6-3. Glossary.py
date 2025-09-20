# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.

# • Think of five programming words you’ve learned about in the previous
# 	chapters. Use these words as the keys in your glossary, and store their
# 	meanings as values.

# •	Print each word and its meaning as neatly formatted output. You might
# 	print the word followed by a colon and then its meaning, or print the word
# 	on one line and then print its meaning indented on a second line. Use the
# 	newline character (\n) to insert a blank line between each word-meaning
# 	pair in your output.

# can't think of any new words I've learned

glossary = {
	'list':'an ordered, mutable collection of items that can hold elements of any type.',
	'tupple':'an ordered, immutable collection of values, usually used to group related data together.',
	'dictionary':'a collection of data stored as key-value pairs, where each key maps to a specific value.',
	'dictionary':'a BIS collection of data stored as key-value pairs, where each key maps to a specific value.',
	'if-elif-else':'a way to run different code depending on whether certain conditions are true.',
	'loop':'a control structure that repeatedly runs a block of code as long as a condition is met or for each item in a sequence.',
	'variable':'a name that stores a value, allowing you to reuse and manipulate that value throughout your code.'
}

for key in glossary:
	if key != 'if-elif-else':
		print(f"\n{key.title()}:")
	else:
		print(f"\n{key.upper()}:")
	print(f"  - It is {glossary[key]}")