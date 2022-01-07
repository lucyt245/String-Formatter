
def phrase_formatter(phrase):
    q_words = ('Who', 'What', 'Why', 'Where', 'How', 'Is')
    phrase = phrase.capitalize()

    if phrase.startswith(q_words):
        return '{}? '.format(phrase)
    else:
        return '{}. '.format(phrase)


def outputter(phrase_bank):
    full_speech = ''

    for phrase in phrase_bank:
        full_speech = full_speech + phrase
    
    print(full_speech)


def input_loop():
    phrase_bank = []

    while True:
        phrase = input('Enter a phrase: ')
        
        if phrase == '\end':
            break
        else:
            phrase_bank.append(phrase_formatter(phrase))
    
    outputter(phrase_bank)


input_loop()
