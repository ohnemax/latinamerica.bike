import os
import gpxpy

# in m/s - everything above that is counted as moving
MOVING_SPEED = 1 / 3.6 

class trip:
    def __init__(self, filename):
        self.parsed = False
        self.calculated = False

        if not os.path.isfile(filename):
            print("cyclegpx - Problem: The filename does not exist. Please initialize the class with an existing filename")
        self.filename = filename

        self.maxS = 0.
        self.averagetotalS = 0.
        self.averagemovingS = 0.
        self.climbingD = 0.
        self.descendingD = 0.
        self.totalD = 0.
        self.movingD = 0.
        self.totalT = 0.
        self.movingT = 0.
        self.name = ""
        self.description = ""
        self.points = 0
        
    def loadandparse(self):
        f = open(self.filename, 'r')
        gp = gpxpy.parse(f)
        f.close()

        # only first track in file is used!
        
        # store descriptive information
        self.name = gp.tracks[0].name
        self.description = gp.tracks[0].description
        # takes only points from first segment 
        self.points = gp.tracks[0].segments[0].points

        self.parsed = True

    def calculate(self):
        self.totalD = gpxpy.geo.length_3d(self.points)

        
        # This parts is heavily inspired by the function get_moving_data of gpx.py in the gpxpy module
        sd = 0.
        st = 0.
        speeds = []
        prev = self.points[0]
        for i in range(1, len(self.points)):
            point = self.points[i]
            t = (point.time - prev.time).total_seconds()
            d = point.distance_3d(prev)
            if t > 0:
                s = d / t
            else:
                s = 0.
            if s > MOVING_SPEED:
                self.movingD += d
                self.movingT += t
            else:
                sd += d
                st += t
            speeds.append(s)
            prev = point

        self.totalD = self.movingD + sd
        self.totalT = self.movingT + st

        self.maxS = max(speeds)
        self.averagetotalS = self.totalD / self.totalT
        self.averagemovingS = self.movingD / self.movingT

        # From get_uphill_downhill in gpx.py
        elevations = list(map(lambda point: point.elevation, self.points))
        self.climbingD, self.descendingD = gpxpy.geo.calculate_uphill_downhill(elevations)
        
        self.calculated = True

    # check status and load necessary parts
    def checkandload(self):
        if not self.parsed:
            self.loadandparse()
        if not self.calculated:
            self.calculate()
        
    # Get information.
    # Distances are in km, speeds are in km/h and times are strings like hh:mm:ss
    def maxspeed(self):
        self.checkandload()
        return self.maxS * 3.6
    
    def averagetotalspeed(self):
        self.checkandload()
        return self.averagetotalS * 3.6

    def averagemovingspeed(self):
        self.checkandload()
        return self.averagemovingS * 3.6

    def climbingdistance(self):
        self.checkandload()
        return self.climbingD / 1000.0

    def descendingdistance(self):
        self.checkandload()
        return self.descendingD / 1000.0

    def totaldistance(self):
        self.checkandload()
        return self.totalD / 1000.0

    def totaltime(self):
        self.checkandload()
        minutes = int(self.totalT / 60)
        hours = int(minutes / 60)
        minutes -= hours * 60
        seconds = int(self.totalT) - hours * 3600 - minutes * 60
        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

    def movingtime(self):
        self.checkandload()
        minutes = int(self.movingT / 60)
        hours = int(minutes / 60)
        minutes -= hours * 60
        seconds = int(self.movingT) - hours * 3600 - minutes * 60
        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

    def trackname(self):
        self.checkandload()
        return self.name

    def trackdescription(self):
        self.checkandload()
        return self.description
