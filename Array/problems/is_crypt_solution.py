def isCryptSolution(crypt, solution):
    sol_dict = {item[0]: item[1] for item in solution}
    crypt_word = []
    
    for word in crypt:
        number = "".join([sol_dict[num] for num in word])
        if number[0] == "0" and len(number) > 1:
            return False
        crypt_word.append(int(number))
    if crypt_word[0] + crypt_word[1] == crypt_word[2]:
        return True
    return False