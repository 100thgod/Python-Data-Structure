from StackADT import Stack

def par_checker(symbol_string):
    p=Stack()
    balanced = True
    index = 0
    while index<len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '({[':
            p.push(symbol)    
        else:
            if p.is_empty() or "({["[")}]".index(symbol)] != p.peek():
                balanced=False
            else:
                p.pop()
            
        index+=1
    if balanced and p.is_empty():
        return True
    else:
        return False

print(par_checker('((()))'))
print(par_checker('(()'))
print(par_checker('({{}})'))
