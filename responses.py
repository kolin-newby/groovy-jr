import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Howdy!'
    
    if p_message == 'roll':
        return 'Your roll is: ' + str(random.randint(1, 6))

    if p_message == '!help':
        return "no help for you"
    
    return 'Your command was not recognized, please try again.'