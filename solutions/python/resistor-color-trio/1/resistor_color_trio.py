code = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

""" list of colors """

def label(colors):
    answer = (code.index(colors[0])*10 + code.index(colors[1])) * 10**(code.index(colors[2]))
    if answer >= 1000000000: 
        answer = answer // 1000000000 
        return f'{answer}' + ' gigaohms'
    if answer >= 1000000: 
        answer = answer // 1000000 
        return f'{answer}' + ' megaohms'
    if answer >= 1000: 
        answer = answer // 1000 
        return f'{answer}' + ' kiloohms'
    
    return f'{answer}' + ' ohms'
