"[ (expression-involving-loop-variables ([x,y])) for outer-loop-variable in outer-sequence for inner-loop-variable in inner-sequence ]"

# results = []
# for outer_loop_variable in outer_sequence:
#    for inner_loop_variable in inner_sequence:
#        results.append( expression_involving_loop_variables )  <---- version larga

# simplificada

nestedArray = [[x, y] for x in [1, 2, 3] for y in [4, 5, 6]]
print(nestedArray)
