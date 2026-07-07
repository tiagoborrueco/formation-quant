def commands(binary_str):
    action = []
    if binary_str.endswith('1'):
        action.append('wink')
    if binary_str[-2] == '1' :
        action.append('double blink')
    if binary_str[-3] == '1' :
        action.append('close your eyes')
    if binary_str[-4] == '1' :
        action.append('jump')

    if binary_str.startswith('1'):
        action = action[::-1]

    return action
