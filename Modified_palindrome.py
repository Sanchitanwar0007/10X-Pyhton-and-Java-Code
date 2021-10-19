def palin(s):
    if s==s[::-1]:
        return True
    else:
        e=len(s)-1
        for i in range(len(s)):
            if s[i]!=s[e-i]:
                a=s[:i]+s[i+1:]
                b=s[:e-i]+s[e-i+1:]
                if a==a[::-1] or b==b[::-1]:
                    return True
                else:
                    return False
for _ in range(int(input())):
    s=input()
    print(palin(s))