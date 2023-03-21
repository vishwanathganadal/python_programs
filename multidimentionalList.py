multlist = [["Mon","Tue","Wed"], [2, 4, 9,], [1,1.5, 2]]
multlist.append(["Phy","Chem","Math"])
print(multlist)

multlist[0].extend(["Thu","Fri"])
print(multlist)