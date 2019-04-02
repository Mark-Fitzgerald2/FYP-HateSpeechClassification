#results = [74.75, 74.63, 88.41, 86.44, 86.25, 75.81, 87.02, 86.9, 87.76, 76.08, 74.57]
#results = [94.9, 94.96, 95.08, 95.11, 94.96, 96.02, 95.42, 94.74, 95.17, 94.4, 94.77, 94.96]
#results = [95.57, 95.66, 95.23, 95.69, 95.76, 95.86, 95.6, 95.88, 95.91, 94.65, 95.36]
#results = [96.03, 96.31, 96.31, 96.23]
results = [91.67, 92.19, 92.23]
mean = 0
var = 0
for result in results:
	mean += result
mean = mean/len(results)
print(mean)
for result in results:
	var += (result-mean)**2

var = var/len(results)
print(var)
