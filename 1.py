import pprint

ms = [[0 for _ in range(10)] for _ in range(10)]
pprint.pprint(ms)

ms[1][1] = 15
pprint.pprint(ms)