from Stack_module import Stack

#Сбалансированно
#s = '(((([{}]))))'
s = '[([])((([[[]]])))]{()}'
#s = '{{[()]}}'

#Несбалансированно
#s = '}{}'
#s = '{{[(])]}}'
#s = '[[{())}]'


lst_bracket = list(s)
index_del_bracket = []
sc = Stack()


def search_brackets(lst_b):
    for i in range(len(lst_b) - 1):
        if lst_b[i] == '[' and lst_b[i + 1] == ']':
            sc.push(i)
            sc.push(i+1)
        elif lst_b[i] == '(' and lst_b[i + 1] == ')':
            sc.push(i)
            sc.push(i + 1)
        elif lst_b[i] == '{' and lst_b[i + 1] == '}':
            sc.push(i)
            sc.push(i + 1)
    return sc


def delete_brackets(s_c):
    for i in range(s_c.size()):
        del lst_bracket[s_c.pop()]
    return lst_bracket


if __name__ == '__main__':
    i = len(lst_bracket)
    while i > 0:
        if len(lst_bracket) == 0:
            break
        delete_brackets(search_brackets(lst_bracket))
        index_del_bracket = []
        i -= 1
    if len(lst_bracket) == 0:
        print('Сбалансированно')
    else:
        print('Несбалансированно')

