filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
oldDomain: "hhp"
newDomain: "h"
newfilenames = []
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

for ext in filenames:
    if ext.endswith(".hpp"):
        newfilenames.append(ext.replace(".hpp", ".h"))
    else:
        newfilenames.append(ext)


print(newfilenames)
newfilenames = [ext.replace(".hpp", ".h") for ext in filenames]
print(newfilenames)


print(newfilenames)
