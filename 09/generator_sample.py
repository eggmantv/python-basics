from inspect import isgenerator, isgeneratorfunction

def gen_num(ids):
    cached_ids = set()

    for x in ids:
        if x in cached_ids:
            print('cached')
            continue

        yield x
        cached_ids.add(x)

# print(isgeneratorfunction(gen_num))
# print(isgenerator(gen_num("hello")))

for x in gen_num("hello"):
    print(x)
