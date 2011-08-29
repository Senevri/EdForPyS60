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
def help():
  print """usage: buf = []
edit(buf) - edits
save(buf) - prompts for filename
buf = load() - prompts for filename
lcode(buf) - prints lines with numbers
lcpages(buf, step) - prints lines with
  numbers, requires enter after step
  lines.p
lcblock(buf, start, end) - prints a
  certain block of lines from buf.
"""
def lcpages(lines, step):
  i=0
  j=step
  cmd = ""
  while (cmd != "q"):
    lcblock(lines, i, j)
    i=j+1
    j=j+step
    cmd=raw_input()
    if cmd == "b":
      j=j-2*step
      if j-step=>0:
        i=j-step
      else: 
        i=0
        j=step