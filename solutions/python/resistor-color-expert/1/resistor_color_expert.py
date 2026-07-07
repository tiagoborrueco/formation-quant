code = ['black', 
        'brown', 
        'red', 
        'orange', 
        'yellow', 
        'green', 
        'blue', 
        'violet', 
        'grey', 
        'white']

tolerance = {'grey': 0.05,
             'violet': 0.1,
             'blue': 0.25,
             'green': 0.5,
             'brown': 1,
             'red': 2,
             'gold': 5,
             'silver': 10}

def resistor_label(colors):
    if len(colors) == 1:
        return f'{code.index(colors[0])}' + ' ohms'
    
    if len(colors) == 4:
        answer = (code.index(colors[0])*10 + code.index(colors[1])) * 10**(code.index(colors[2]))
        if answer >= 1000000000: 
            answer = answer / 1000000000 
            return f'{answer:g}' + ' gigaohms' + ' ±' +f'{tolerance[colors[3]]}' + '%'
        if answer >= 1000000: 
            answer = answer / 1000000 
            return f'{answer:g}' + ' megaohms' + ' ±' +f'{tolerance[colors[3]]}' + '%'
        if answer >= 1000: 
            answer = (answer / 1000)
            return f'{answer:g}' + ' kiloohms' + ' ±' +f'{tolerance[colors[3]]}' + '%'
        return f'{answer:g}' + ' ohms' + ' ±' +f'{tolerance[colors[3]]}' + '%'
        
    if len(colors) == 5:
        answer = (code.index(colors[0])*100 + code.index(colors[1])*10 + code.index(colors[2])) * 10**(code.index(colors[3]))
        if answer >= 1000000000: 
            answer = answer / 1000000000 
            return f'{answer:g}' + ' gigaohms' + ' ±' +f'{tolerance[colors[4]]}' + '%'
        if answer >= 1000000: 
            answer = answer / 1000000 
            return f'{answer:g}' + ' megaohms' + ' ±' +f'{tolerance[colors[4]]}' + '%'
        if answer >= 1000: 
            answer = (answer / 1000)
            return f'{answer:g}' + ' kiloohms' + ' ±' +f'{tolerance[colors[4]]}' + '%'
        return f'{answer:g}' + ' ohms' + ' ±' +f'{tolerance[colors[4]]}' + '%'