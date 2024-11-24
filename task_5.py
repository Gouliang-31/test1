class RandomGenerator:
    def __init__(self, seed=1):
        self.a = 1664525
        self.c = 1013904223
        self.m = 2 ** 32
        self.state = seed

    def next(self):

        self.state = (self.a * self.state + self.c) % self.m

        return self.state % 101



gen = RandomGenerator(seed=42)

for _ in range(10):
    print(gen.next())