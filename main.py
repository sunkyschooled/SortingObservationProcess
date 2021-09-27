import random
from time import thread_time
random.seed(20)
f = open('sort.csv', 'w')
for N in range(10000):
  data_to_sort=(list(range(N)))
  random.shuffle(data_to_sort)
  runtime = thread_time()
  data_to_sort.sort()
  f.write('{},{}\n'.format(N, thread_time()-runtime))
f.close()