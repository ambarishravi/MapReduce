# reducer.py code

def reducer():	
	salesTotal = 0
	oldItem = None
	for line in sys.stdin:
		data = line.strip().split("/t")
		if len(data) != 2:
			continue
		thisItem, thisSales = data
		if oldItem and oldItem != thisItem:
			print "{0}\t{1}".format(oldItem, salesTotal)
			salesTotal = 0
		oldItem = thisItem
		salesTotal += float(thisSales)
	if oldItem != None:
		print "{0}\t{1}".format(oldItem, salesTotal)


  
