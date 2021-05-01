import array
Python = "Python"
B = array.array('i')
B.fromstring("Python")
B.append("Pycharm")
type(B)

for karakter in B:
    print("%c " % karakter, end='')