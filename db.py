db=[]
def select(table):
  for t in db:
    if t[0]==table:
      return t[1:]
def columns(table, columns):
  indices = []
  for c in columns:
    i=0
    for c2 in table[0]:
      if c2==c: 
        indices.append(i)
        i=0
      i=i+1 #my c was showing
  out = []
  for c in table:
    out.append([])
    for i in indices:
      out[len(out)-1].append(c[i])
  return out
def create_table(tname, desc_list):
  db.append(tname, desc_list)
