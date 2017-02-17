def normalize(l):
	max_item = max(l)
	min_item = min(l)
	return [(x - min_item) * 1.0 / (max_item - min_item) for x in l]
