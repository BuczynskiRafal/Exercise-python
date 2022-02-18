V = {
    'RS': {'M': 1.5, 'U': 9, 'T': 1},
    'M': {'U': 1.5},
    'T': {'S': 1},
    'S': {'U': 1},
}
# cost = V['RS']['T'] + V['T']['S'] + V['S']['U']
# print(cost)
# # 3 students
# tramwaj = cost * 3
# taksówka = 9
# print(f'Tramwajem: {tramwaj}, taksóką: {taksówka}')

my_route = ['RS', 'T', 'S', 'U']
sum = 0
start = my_route[0]
for destination in my_route[1:]:
    sum += V[start][destination]
    start = destination
print('The cost for 1 student is:', sum)
print('The cost for 3 students is:', 3*sum)
print('The cost for 3 students in taxi is:', V['RS']['U'])