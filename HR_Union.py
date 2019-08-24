frenchNewsPaper = {10,1,2,3,11,21,55,6,8}
englishNewsPaper = {1,2,3,4,5,6,7,8,9}

atLeastOne = frenchNewsPaper.union(englishNewsPaper)
print(atLeastOne)

bothNewsPaper = frenchNewsPaper.intersection(englishNewsPaper)
print(bothNewsPaper)

onlyEnglish = englishNewsPaper.difference(frenchNewsPaper)
print(onlyEnglish)

eitherEngOrFrench = englishNewsPaper.symmetric_difference(frenchNewsPaper)
print(eitherEngOrFrench)