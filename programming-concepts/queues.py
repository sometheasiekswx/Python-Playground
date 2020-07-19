import queue

q = queue.Queue()

# True
print(q.empty())

q.put('Somethea')
q.put('Sopheany')

# False
print(q.empty())

item1 = q.get()
# Somethea
print(item1)

item2 = q.get()
# Sopheany
print(item2)

# True
print(q.empty())

# # Blocks program execution
# item3 = q.get()

# Does not block program execution
try:
    item3 = q.get(False)
except queue.Empty:
    print('Queue is empty')

small_q = queue.Queue(2)
small_q.put('Tom')
small_q.put('Jerry')

# True
print(small_q.full())

# # Blocks program execution
# small_q.put('Somethea')

# Does not block program execution
try:
    small_q.put_nowait('Somethea')
except queue.Full:
    print('Queue is full')
