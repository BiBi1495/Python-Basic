# begin with set

#create set
A = {1,3}
print(A)

#add elements
A.add(2)
print(A)

#update elements
A.update('python', A, ['a', 'b'])
print(A)

#delete elements
A.discard('t')
A.remove('a')
print(A)

#union and intersection
print('\n union and intersection:')
A = {1,2,3,4}
B = {1,3,5,7}
C = A | B
print(C)
print(A.union(B))
print(B.union(A))

D = A & B
print(D)
print(A.intersection(B))
print(B.intersection(A))

#defferece and symmetric defference
print('\n defference and symmetric defference:')
E = A - B
print(E)
#print(A.defference(B)) the set have not attribute defference

F = A ^ B
print(F)
#print(A.symmetric_defference(B)) the set have not attribute defference
