def generate_permutations(s):
    if len(s) == 1:
        return [s]  
    permutations = []
    for i in range(len(s)):
        char = s[i]
        rest = s[:i] + s[i+1:]
        for perm in generate_permutations(rest):
            permutations.append(char + perm)    
    return list(set(permutations))
print(generate_permutations("abc")) 
print(generate_permutations("aab"))  
