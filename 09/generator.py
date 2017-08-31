def gen_123():
    yield 1
    yield 2
    yield 3

# a = gen_123()
# print(a)
# print(next(a))
# print(next(a))
# print(next(a))

for x in gen_123():
    print(x)
