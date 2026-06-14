
import sys
def fun(*args):
    print(*args,file=sys.stderr)
fun("hello class")

'''note: the output of this code wille be "hello class" but it appears
under "Run time errors" because sys.stderr sends the message to the error stream, not the regular output'''