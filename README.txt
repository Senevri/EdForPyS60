Okay, this is a demonstration of usage. 
Basically, this script adds some REALLY basic 
editing capabilities for REPL, for file creation
and such. I needed this for my smartphone's
pys60 script shell, but it's pure python. 
usage: run script, create list, edit(list), 
after you're done, an empty line with '.'
you can do save(list) which prompts for filename
or you can do list=load(), which prompts for 
file to load.
help() for more. Have fun.
*update*
made a class-version.
from ced import ced
ed=ced()
ed.load() - prompts for filename
ed.save() - prompts for filename
ed.edit()
ed.block(start, end) - displays a block from code
ed.page(step) - displays the document in steps.