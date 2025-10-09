def send_messages(messages, sent_messages):
	"""Show the messages passed into the list."""
	while messages:
		msg = messages.pop()
		print(msg)
		sent_messages.append(msg)

messages = ['Hola, ¿Cómo te llamas?', 'Hola, ¿Cómo estás?', 'Hi, How are you?', 'Hi, What is your name?']
sent_messages = []

send_messages(messages, sent_messages)

print(f"\nOriginal Messages:")
for msg in messages:
	print(f"  - {msg}")

print(f"\nMessages Sent:")
for msg in sent_messages:
	print(f"  - {msg}")
