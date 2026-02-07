def search(s, a):
    b = s.find(a)
    if b != -1:
        s = s.replace(s[b:b + len(a) + 1], "")
        return s
    else:
        return str(b)

def search_name(s, a):
    b = s.find(a)
    if b != -1:
        s = s.replace(s[b:len(s)], "")
        return s
    else:
        return str(b)
