import gflConst
import gflObject

one = 1
two = 2
three = one + two

hello = "hello"
world = "world"
helloworld = hello + " " + world

print helloworld + "!" + " " + str(three)

print "Piston Engine: " + str(gflConst.EngineC.PISTON)
print "Admin Logon: " + str(gflConst.LogonC.ADMIN)

ac1 = gflObject.Aircraft()
print "ac1 ID: " + str(ac1.id)
