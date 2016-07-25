# Dynamic labeling within ArcMap
# created by Eddie Anderson 5/2016
# This code (minus the comments) is meant to be run in the Label Expression window in ArcMap.
# Make sure the Advanced checkbox is clicked and Python is selected as the parser.

# "def" defines a function called "FindLabel." It has to be called "FindLabel" to work in the
# label expression field in ArcMap. In the parentheses() the fields that the function will be
# using are declared. 

def FindLabel ( [DNRTRNXNUM] , [T_PNAMES] , [T_EXPDATE], [SL_EMate_2]  ):

# There could be multiple materials listed for each lease on school trust lands (the "SL_EMate_2"
# column/field). Since, we want to show only primary materials, we need to include the following lines.

# "a" variable is declared and given the values of the SL_EMate_2 field
  a = [SL_EMate_2]
  
# "b" variable is declared. The "split" method will take the "a" variable(i.e. the SL_EMate_2 field)
# and separate it wherever there is a semicolon. This means that the "b" variable becomes a list data
# type (more on that later).
  b = a.split(";")

# This "for loop" essentially says "for every item in the "b" variable, i.e. every
# material listed within a cell on the "SL_EMate_2" column, do the following.  
  for x in b:
	  
# We're only concerned with primary materials, so when a material is identified as primary,
# it goes to the next line. If a material is not primary, then it is skipped.	  
    if "Primary" in x:
	    
# The following takes a text string, such as "Gravel, High Value (Primary)" and chops off the
# "(Primary)" part, i.e. the last 9 characters, leaving us with "Gravel, High Value". It assigns
# this output to a new variable, called "c". This is the variable we will use on the return line
# to represent SL_EMate_2.
      c = x[:-9]

# a variable is declared, called "leaseename". This statement deals with the T_PNAMES column/field.
# Some names (for example, the "&" character, which could confuse ArcMap into thinking it is code
# and not text. So, this "replace" method replaces "&" with "&amp", which ArcMap recognizes as the
# text character "&" and not code. It's somewhat counterintuitive: we need code to tell ArcMap that
# "&" really is "&" and not code.    
  leaseename = [T_PNAMES].replace("&","&amp;")

# The return command prints the following expression for each feature
  return "<BOL><UND>" + "Lease # " + [DNRTRNXNUM]  [5:]+ "</UND></BOL>" + "\r\n"+ "Leasee: "+leaseename + "\r\n" + "Primary Material: " +  str(c)+"\r\n" + "Expires: " + [T_EXPDATE]

# Additional notes:
# <BOL> and <UND>  are tags to bold and underline everything following them. They are turned off by
# the </BOL></UND> tags. Also, they must be within quotes, i.e. "<BOL><UND>"
#
# Python is big on proper indentation. Note how all lines after the first one are indented at least
# 2 spaces. The "if" statement is indented 4 spaces, (it is part of the "for" statement) and the
# following line (it is part of the "if" statement) is indented another 2 spaces (or 6 spaces total).
#
# "\n" is typically a newline break within Python, but in this case it needs to be preceded by "\r"
#
# the return line is made up of a bunch of strings (the text within quotes) stitched together with
# plus signs. Note the str(c) part: str converts the c variable(which is a list [because it was
# created using the split method]) into a string type so it matches the others. 
