def show_messages(messages):
	"""Show the messages passed into the list."""
	while messages:
		msg = messages.pop()
		print(msg)

messages = ['Hola, ¿Cómo te llamas?', 'Hola, ¿Cómo estás?', 'Hi, How are you?', 'Hi, What is your name?']
show_messages(messages)