n, m = map(int, input().split()) # 수록된 포켓몬의 수, 맞춰야 하는 문제의 수
pokemon_dict = {}

for i in range(1, n + 1):
    pokemon_dict[input()] = i

reversed_dict = dict(map(reversed, pokemon_dict.items()))

for j in range(m):
    inputs = input()
    if inputs.isdigit():
        print(reversed_dict[int(inputs)])
    else:
        print(pokemon_dict[inputs])