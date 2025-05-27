
def encrypt_text(text):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	new_word = ""
	index_increment = 0
	no_of_alphabets = 26
	alphabets_for_letters_greater_than = 25

	for each_letter in text:
		initial = text.index(each_letter)
		count = 0
		for letter in alphabet:
			count += 1
			if letter == each_letter:
				break

		initial_plus = count + 13

		if initial_plus < alphabets_for_letters_greater_than and each_letter != " ":
			index_increment = count + 13
			new_letter = alphabet_index(index_increment)
			new_word = new_word + new_letter

		elif initial_plus > alphabets_for_letters_greater_than and each_letter != " ":

			index_increment = count + 13
			new_index = index_increment - no_of_alphabets
			new_letter = alphabet_index(new_index)
			new_word = new_word + new_letter

		elif each_letter == " ":
			new_word = new_word + each_letter

	return new_word

def alphabet_index(final_key):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	count = 0

	for letter in alphabet:
		letter = letter
		count = count + 1
		if count == final_key:
			break

	return letter
 
				
				
text = "hello world"
print(encrypt_text(text))	
		