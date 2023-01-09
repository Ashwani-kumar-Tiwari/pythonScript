def text_to_hex():
  text = input('Enter the string: ')
  # Encode the text into a bytes object
  b = text.encode('utf-8')

  # Convert the bytes object into a list of integers
  int_list = list(b)

  # Convert the list of integers into a list of hexadecimal strings
  hex_list = [hex(i) for i in int_list]

  # Concatenate the hexadecimal strings into a single string
  hex_string = ''.join(hex_list)

  print(hex_string)


if __name__ == "__main__":
    text_to_hex()
