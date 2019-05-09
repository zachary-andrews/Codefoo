def mapping(obj):
    return map({}.setdefault, obj,range(len(obj)))
    
pattern = "abba"
str = "cat dog dog cat"
print mapping(pattern) == mapping(str.split())

