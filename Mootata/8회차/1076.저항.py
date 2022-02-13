resisters = {'black' : 0, 'brown' : 1, 'red' : 2, 'orange' : 3, 'yellow' : 4, 'green' : 5, 'blue' : 6, 'violet' : 7, 'grey' : 8, 'white' : 9}
inputs = [input() for _ in range (3)]

print((resisters[inputs[0]] * 10 + resisters[inputs[1]]) * (10 ** resisters[inputs[2]]))