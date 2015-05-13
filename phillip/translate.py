translation_dict = {
    "a": "4",
    "b": "8",
    "e": "3",
    "l": "1",
    "o": "0",
    "s": "5",
    "t": "7"
}

original_text = raw_input("Enter some text: ")
new_string = ""

for char in original_text:
    if char in translation_dict.keys():

        new_string += char
