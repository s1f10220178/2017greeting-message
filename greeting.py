from datetime import datetime

def greet():
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
        message = 'Hello'
    else:
        message = 'Good evening, ' + name + '-san!'
>>>>>>> timely-message
    print(message)


greet('Inoue')
