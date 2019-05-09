def canConstruct (ransomNote, Magazine):
    for c in ransomNote:
        if c not in Magazine:
            return False
        else:
            Magazine = Magazine.replace(c, "",1)
    return True

if __name__ == '__main__':
    ransomNote = "aasz2f"
    Magazine = "a2ajkszhdf"
    result = canConstruct(ransomNote,Magazine)
    print result