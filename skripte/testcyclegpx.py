import cyclegpx

cg = cyclegpx.trip("../tracks/2016-09-05_d2.gpx")

cg.loadandparse()
cg.calculate()

print("Name: {:s}".format(cg.trackname()))
print("Description: {:s}".format(cg.trackdescription()))

print("Max Speed: {:f}".format(cg.maxspeed()))
print("Average Moving Speed: {:f}".format(cg.averagemovingspeed()))
print("Average Total Speed: {:f}".format(cg.averagetotalspeed()))
print("Total Distance: {:f}".format(cg.totaldistance()))
print("Total Time: {:s}".format(cg.totaltime()))
print("Total Time in seconds: {:f}".format(cg.totaltimeseconds()))
print("Moving Time: {:s}".format(cg.movingtime()))
print("Moving Time in seconds: {:f}".format(cg.movingtimeseconds()))
print("Uphill distance: {:f}".format(cg.climbingdistance()))
print("Downhill distance: {:f}".format(cg.descendingdistance()))
