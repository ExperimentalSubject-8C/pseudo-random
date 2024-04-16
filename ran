class PRNG:

  def __init__(self, seed):
    self.seed = seed
    self.a = 166452541928740173948
    self.c = 637245824524567913119612398192847752
    self.m = (2**64)-1

  def set_seed(self, seed):
    self.seed = seed

  def rand(self):
    self.seed = (self.a * self.seed + self.c) % self.m
    return self.seed

  def rand_range(self, start, end):
    return start + (self.rand() % (end - start + 1))

  def save_seed(self):
    with open('seed.txt', 'w') as f:
      f.write(str(self.seed))

  def load_seed(self):
    with open('seed.txt', 'r') as f:
      return int(f.read())


try:
  Random =PRNG(0)
  saved_seed = Random.load_seed()
  prng = saved_seed
  Random.set_seed(saved_seed)
except ValueError:
  Random = PRNG(0)
  saved_seed = 1234
