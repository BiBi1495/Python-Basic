# Co formating string 18

print("thứ tự là {} {} {} {}".format("thứ 1", "thứ 2", "thứ 3", "thứ 4"))

print("thứ tự là {1} {0} {3} {2}".format("thứ 1", "thứ 2", "thứ 3", "thứ 4"))

print("thứ tự là {2} {2} {2} {1}".format("thứ 1", "thứ 2", "thứ 3", "thứ 4"))

print("thứ tự là {st} {th} {nd} {rd}".format(st= "thứ 1",nd = "thứ 2",rd ="thứ 3",th="thứ 4"))

# float format

value = 1023.12345678
print("số đó là {r:1.8f}".format(r = value))
print("số đó là {r:20.8f}".format(r = value))
print("số đó là {r:1.3f}".format(r = value))
