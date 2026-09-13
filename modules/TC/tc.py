"""Celuis -> F..."""
def c2f(c):
    f=c*1.8+32
    return f
""" F -> C"""
def f2c(f):
    c=(f-32)/1.8
    return c
print(f"__name__ is {__name__}")

"""Test"""
if __name__=="__main__":
    print(f"Test, 0 C={c2f(0):.2f} F")
    print(f"Test, 0 F={f2c(0):.2f} C")
