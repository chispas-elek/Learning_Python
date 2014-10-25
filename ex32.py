# Realizaremos for haciendo un uso de listas

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first list kind of for-loop goes through a list
for number in the_count:
    print "This is count: %d" % number

# Sames as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# Also we can through mixed list too
# notice we have to use %r since we don't know wat's is in
for i in change:
    print "I got %r" % i

# We can also build list, first start with an empty one
elements = []

# Then use the range function to do 0 to 5 counts
# La funcion range me va a permitir establecer un rango de vueltas tanto como quiera
# En este caso voy a poder decirle que cuente desde 0 hasta 6, o sea, 5 vueltas en total desde el valor 0 hasta el 5.

for i in range(0, 6):
    print "Adding %d to the list" % i
    # append is a function that lists understand
    elements.append(i)

# now we cant print then out too
for i in elements:
    print "Element was: %d" % i
