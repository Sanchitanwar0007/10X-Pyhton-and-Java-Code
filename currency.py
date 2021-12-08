def currency_val(string,i,res):
    if(i==len(string)):
        print(res)
        return
    currency_val(string,i+1,res+(int(string[i])))

string=input()
currency_val(string,0,0)

