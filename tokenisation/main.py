import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')
text = "This is a simple text"


tokens = encoder.encode(text=text)

print(tokens)
