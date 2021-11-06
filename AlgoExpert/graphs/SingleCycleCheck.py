testcases = [
  {
    "input": ([2, 3, 1, -4, -4, 2]),
    "output": True,
  },
]


def get_next_idx(idx, array):
	next_idx = (idx + array[idx]) % len(array)
	return next_idx if next_idx >=0 else len(array) + next_idx


def hasSingleCycle(array):
	count = 0
	idx = 0
	while count < len(array):
		if count > 0 and idx == 0:
			return False
		count += 1
		idx = get_next_idx(idx, array)
	return idx == 0
