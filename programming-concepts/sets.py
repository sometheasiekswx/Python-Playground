fun = set(['life', 'food', 'death', 'games', 'songs', 'programming', 'learning', 'travelling'])
hard = set(['life', 'death', 'programming', 'learning', 'social events', 'hell', 'tom jerry', 'somethea siek'])
easy = set(['death', 'games', 'songs', 'resting', 'tom jerry', 'somethea siek'])

print(f'fun: {fun}')
print(f'union: {fun.union(hard, easy)}')
print(f'intersection: {fun.intersection(hard, easy)}')
print(f'difference: {easy.difference(hard)}')
print(f'difference: {hard.difference(easy)}')
print(f'symmetric_difference: {hard.symmetric_difference(easy)}')

fun.add('partying')
# No error
fun.add('partying')
print('partying' in fun)
fun.remove('partying')
# # Error
# fun.remove('partying')
print('partying' in fun)
# Remove random items
fun.pop()
