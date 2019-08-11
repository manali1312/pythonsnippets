sampleSet={0,1,2,3}
anotherSet={3,4,5}
print(sampleSet)
sampleSet.add(1)
print(sampleSet)
sampleSet.add(4)
print(sampleSet)

print(sampleSet.union(anotherSet))
print(sampleSet.intersection(anotherSet))

print(sampleSet.remove(3))
for i in sampleSet:
    print(i)
print(list(sampleSet))