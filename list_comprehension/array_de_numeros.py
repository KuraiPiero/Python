"[ (expression-involving-loop-variable (x)) for ((loop-variable in sequence (in range(10)) ]"

# This will step over every element in a sequence, successively setting the loop-variable equal to
# every element one at a time. It will then build up a list by evaluating the
# expression-involving-loop-variable for each one. This eliminates the need to use lambda forms and generally
# produces a much more readable code than using map() and a more compact code than using a for loop.

ListOfNumbers = [x for x in range(10)]

