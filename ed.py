lines=[]
def edit(lines):
  rin=raw_input()
  while(rin!='.'):
    lines.append(rin+'\n')
    rin=raw_input()    
def load():
  rin=raw_input()
  f=open(rin,"r")
  lines=f.readlines()
  f.close()
  return lines
def save(lines):
  f=open(raw_input(), "w")
  if lines[0].endswith("\n"):
    f.writelines(lines)
  else :
    f.write('\n'.append(lines))
  f.close()
def lcode(lines):
  i=0
  for l in lines:
    print i, '\t', l.strip('\n')
    i=i+1
def lcblock(lines, start, end):
  i=0
  for l in lines:
    if start<=i<=end:
      print i, '\t', l.strip('\n')
    i=i+1
def lcpages(lines, step):
  i=0
  j=step
  while j<len(lines):
    lcblock(lines, i, j)
    i=j+1
    j=j+step
    foo=raw_input()
def help():
  print "edit(list) - insert lines to list until \nline only contains '.'"
  print "list = load() prompts for filename \nand loads lines to list"
  print "save() saves a list named 'lines'"
  print "lcode(list) prints line numbers and \nthe lines in a list"
  print "lcblock(list, start, end) prints a \ncertain subsection of a list"
  print "lcpages(list, step) prints the entire"
  print "list, but pauses after step lines"

