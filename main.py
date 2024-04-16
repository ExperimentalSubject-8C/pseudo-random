from Ran import PRNG

try:
  Random =PRNG(0)
  saved_seed = Random.load_seed()
  prng = saved_seed
  Random.set_seed(saved_seed)
except ValueError:
  Random = PRNG(0)
  saved_seed = 1234

print("Seed: ", Random.seed)

print("Please input the following:")
while True:
  try:
    range1 = input("input blank1 of random integer from (blank1) to (blank2): ")
    range1 = int(range1)
    range2 = input(f"input blank2 of random integer from {range1} to (blank2):")
    range2 = int(range2)
    break
  except ValueError:
    print("Please provide an integer")

print(Random.rand_range(range1, range2))
Random.save_seed()
