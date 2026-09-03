def is_paired(input_string):
    stack = []
    for item in input_string:
        if item in "([{":
            stack.append(item)
        if item in ")]}":
            if stack != []:
                if (item == ")" and stack[-1] == "(") or (item == "]" and stack[-1] == "[") or (item == "}" and stack[-1] == "{"):
                    stack.pop()
                else:
                    return False
            else :
                return False
    return stack == []
                    
            
            
        
        
