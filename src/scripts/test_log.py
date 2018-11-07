 #!/usr/bin/env python

f = open("/home/waltzrobotics/demofile.txt", "a")


var1 = 10
var2 = 20
var3 = 30
outputString = "{}, {}, {}\n".format(var1, var2, var3)

f.write(outputString)