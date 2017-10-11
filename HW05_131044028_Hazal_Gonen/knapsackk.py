# items: [(id, weight, value)]
def knapsack(items, max_weight):
	knapsack = []
	knapsack_weight = 0
	knapsack_value = 0
	items_sorted = sorted(items, key=lambda x: x[2])
	while len(items_sorted) > 0:
		item = items_sorted.pop()
		if item[1] + knapsack_weight <= max_weight:
			knapsack.append(item)
			knapsack_weight += knapsack[-1][1]
			knapsack_value += knapsack[-1][2]
		else:
			break
	return knapsack, knapsack_weight, knapsack_value

def main():
        knapsack_items = [(0,2,3), (1,5,3), (2,7,4), (3,3,5)]
        W = 10
        print("butun itemler:(id,agirlik,deger)",knapsack_items , "  knapsack kapasitesi:", W)
        knapsack_, wt, val = knapsack(knapsack_items, W)
        print("secilen itemler",knapsack_)
        print("agırlık:",wt)
        print("deger ",val)
