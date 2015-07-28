class Airport(object):
    def __init__(self,id = 0):
		self.id = id 
		self.ICAO = ""
		self.FIR = ""
		self.Name = ""
		self.Country = ""
		self.Remarks = ""
		self.FreqATIS = 0
		self.FreqTower = 0
		self.FreqGround = 0
		self.FreqApproach = 0
		self.FreqClearance = 0
