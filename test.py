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

ac1 = gflObject.Aircraft(500)
ac1.id += 1
ap1 = gflObject.Airport(66)

print "ac1 ID: " + str(ac1.id)
print "ap1 ID: " + str(ap1.id)

dl1 = gflObject.DisplayItem(500,['one', 'two', 'three'])

print "dl1:-"
print dl1.getList()

