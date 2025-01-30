morse_chart = {
    'A': '._',
    'B': '_...',
    'C': '_._.',
    'D': '_..',
    'E': '.',
    'F': '.._.',
    'G': '__.',
    'H': '....',
    'I': '..',
    'J': '.___',
    'K': '_._',
    'L': '._..',
    'M': '__',
    'N': '_.',
    'O': '___',
    'P': '.__.',
    'Q': '__._',
    'R': '._.',
    'S': '...',
    'T': '_',
    'U': '.._',
    'V': '..._',
    'W': '.__',
    'X': '_.._',
    'Y': '_.__',
    'Z': '__..',
    ' ': '/',  # This is for separating words
    '.': '._._._',
    ',': '__..__',
    '0': '_____',
    '1': '.____',
    '2': '..___',
    '3': '...__',
    '4': '...._',
    '5': '.....',
    '6': '_....',
    '7': '__...',
    '8': '___..',
    '9': '____.'
}


def morse_code_translator(message):
    morse_code = ''
    for i in message.upper():
        morse_code += morse_chart.get(i, '') + ' '

    return morse_code


#  text should be either alphanumeric or only , and . for this simple morse code generator
plain_text = input("Enter the message: ")
morse_coded_message = morse_code_translator(plain_text)
print(f"The morse code for {plain_text} is \n{morse_coded_message}")