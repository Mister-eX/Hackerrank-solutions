def timeInWords(h, m):
    num= ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']

    if m==0:
        return str(num[h-1])+ " o' clock"
    elif m==1:
        return "one minute past "+str(num[h-1])
    elif m==59:
        return "one minute to "+str(num[h-1])
    elif m==15:
        return "quarter past "+str(num[h-1])
    elif m==45:
        return "quarter to "+str(num[h])
    elif m==30:
        return "half past "+str(num[h-1])
    elif m>30:
        return str(num[60-m-1])+ " minutes to "+str(num[h])
    else:
        return (str(num[m-1])+" minutes past "+str(num[h-1]))
