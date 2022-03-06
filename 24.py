from itertools import permutations

string = '0123456789'

def lexiographic_permutations(string :str) -> str:
    string_list = sorted(list(string))

    perms = list(permutations(string_list))

    answer = ''.join(perms[999999])
    print(answer)

lexiographic_permutations(string)