def alphabet():
    alp="abcdefghijklmnopqrstuvwxyz" * 10
    lettreu=""
    lettrea=""
    lettre="a"
    n=1
    while lettreu < alp and len(lettre) > len(lettrea):
        print(lettre)
        lettrea = lettre
        lettreu += lettre
        n += 1
        lettre = alp[len(lettreu):len(lettreu)+n]

alphabet()

