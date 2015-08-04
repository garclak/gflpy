class Runway(object):
    def __init__(self,id = 0):
		self.id = id
        self.Designation = ""
        self.Surface = 0 # gflConst.SurfaceC
        self.Length = 0
        self.LocFreq = 0
        self.LocHeading = 0
        self.LocAltFreq = 0
        self.LocAltHeading = 0
        self.Remarks = ""