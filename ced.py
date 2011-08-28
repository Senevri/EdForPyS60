class ced:
  buffer = []
  def edit(self):
    rin = raw_input()
    while (rin!='.'):
      self.buffer.append(rin+'\n')
      rin=raw_input()
  def load(self):
    f=open(raw_input(), "r")
    self.buffer = f.readlines()
    f.close()
  def save(self):
    f=open(raw_input(), "w")
    f.writelines(self.buffer)
    f.close()
  def block(self, start, end):
    i=0
    for l in self.buffer:
      if start<=i<=end:
        print i, '\t', l.strip('\n')
      i=i+1
  def page(self, step):
    i=0
    j=step
    cmd = ""
    while (j+step<len(self.buffer) and cmd != "q"):
      self.block(i, j)
      i=j+1
      j=j+step
      cmd=raw_input()

