"""Symmetry analyzer for ternary sequences."""
def find_mirror_pairs(v): return [(i,len(v)-1-i) for i in range(len(v)//2) if v[i]==v[len(v)-1-i]]
def find_conservation_pairs(v): return [(i,v[i],len(v)-1-i,v[len(v)-1-i]) for i in range(len(v)//2) if v[i]+v[len(v)-1-i]==0]
def classify(v): return {"mirror":find_mirror_pairs(v),"conservation":find_conservation_pairs(v)}
if __name__=="__main__": print(classify([1,0,-1,1,0,-1,1,1]))
