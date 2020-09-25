values = [0, 25, 50, 41, 30]
valuex = [0, 0, 25, 50, 41, 30]
order = ["first", "second", "third", "fourth", "fifth"]
sum = 0
summes = [0]
length = 0
for value in values:
    sum += value
    length += 1
    if sum == None:
        sum = 0
    else:
        sum = sum
    index = int(length)
    summes.append(sum)
    average = sum / length
    print(
        f"In the {order[index-1]} try the sum of {summes[index-1]} and {values[index-1]} was {sum} and the average of this {length} items was {average} \n"
    )

