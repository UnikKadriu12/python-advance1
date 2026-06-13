from unioni import rezultati

set1 = {1,2,3}
set2 = {3,4,5}

print(set1^set2)

rezultati = set1.symmetric_difference(set2)

print(rezultati)