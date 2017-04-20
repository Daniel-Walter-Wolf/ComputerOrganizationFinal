Daniel W. Wolf

My assembler has a dictionary of all acceptable inputs for its assembly code. 
It then parses a text file and takes each line and converts that into binary.
It then concatanates them with line breaks and writes them into a file.

You use the assembler by opening it up in idle and calling the assemble 
function.  This function takes a filename as its parameter.  In our case you
would input the 20-line-Assembly.txt file.  It then produces the newHexFile.
hex file, which can be loaded into logisim.

