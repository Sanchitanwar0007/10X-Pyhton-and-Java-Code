def generate_bracket(string,bracket,opening_bracket,closing_bracket):
    if(opening_bracket==0 and closing_bracket==0):
        bracket.append(string)

    if(opening_bracket>0):
        generate_bracket(string+'(',bracket,opening_bracket-1,closing_bracket)

    if(closing_bracket>opening_bracket):
        generate_bracket(string+')',bracket,opening_bracket,closing_bracket-1)
        
def getAllBalancedParan(n):
    # Implement this function
    bracket=[]
    generate_bracket("",bracket,n,n)
    return bracket
# Do not edit anything below
n = int(input())
allBalancedParan = getAllBalancedParan(n)
allBalancedParan.sort()
for expr in allBalancedParan:
    print(expr)