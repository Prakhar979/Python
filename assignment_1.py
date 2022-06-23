def Q1(string,char):
    ans=''
    for i in string:
        if i!=char:
            ans+=i
    return ans


def Q2(string,char):
    return string.count(char)


def Q3(string1,string2):
    string1.sort()
    string2.sort()
    return string1==string2


def Q4(string):
    return string==reversed(string)


def Q5(char):
    a=['a','e','i','o','u']
    if char in a:
        return 'Vowel'
    else:
        return 'Consonant'

def Q6(ex):
    return ex.isdigit()

def Q8(string,char):
    ans=''
    for i in string:
        if i==' ':
            ans+=char
        else:
            ans+=i
    return ans


def Q9(string,char):
    return string.replace(' ',char)


def Q1011(string):
    return string.upper()

def Q12(arr):
    for i in len(arr):
        if arr[i]==i+1:
            pass
        else:
            return i+1

def Q13(arr):
    focc=[]
    res=[]
    for i in arr:
        if i in focc:
            res.append(i)
        else:
            focc.append(i)
    return res

def Q14(arr,sum):
    res=[]
    for i in arr:
        j=sum-i
        if j in arr:
            res.append([i,j])
        else:
            pass
    return res


def Q15(arr1,arr2):
    return len(arr1)==len(arr2)


def Q16(arr):
    arr.sort()
    return arr[0],arr[-1]

def Q17(arr):
    arr.sort(arr)
    return arr[-2]

def Q18(arr):
    arr.sort()
    return arr[-1],arr[-2]


def Q19(arr):
    return set(arr)

def Q21(arr):
    return reversed(arr)
    # Q22 return arr[::-1]

def Q23(arr):
    return len(arr)

def Q24(arr,element):
    arr.append(element)










