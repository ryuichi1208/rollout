import timeit
code = '''
import redis
r = redis.StrictRedis()
r.flushdb()
for i in range(10000):
    r.set(i, i)
'''
print(timeit.timeit(code,number=1))
