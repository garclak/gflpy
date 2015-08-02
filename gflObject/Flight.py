import datetime

class Flight(object):
    def __init__(self,id = 0):
		self.id = id
		self.Status = 0 # gflConst.StatusC
		self.FlightNotes = ""
		self.WxRating = 0 # gflConst.WxC
		self.OnDateUTC = datetime.datetime(1800,01,01)
		self.OffDateUTC = datetime.datetime(1800,01,01)
		self.DurationDay = datetime.timedelta()
		self.DurationNight = datetime.timedelta()
		self.DepCloudCeiling = 0
		self.DepVisDistance = 0
		self.DepOAT = 0
		self.DepWindMagBearing = 0
		self.DepWindSpeed = 0
		self.DepBarometer = 0
		self.ArrCloudCeiling = 0
		self.ArrVisDistance = 0 
		self.ArrOAT = 0
		self.ArrWindMagBearing = 0
		self.ArrWindSpeed = 0
		self.ArrBarometer = 0
		self.AltCloudCeiling = 0
		self.AltVisDistance = 0
		self.AltOAT = 0
		self.AltWindMagBearing = 0
		self.AltWindSpeed = 0
		self.AltBarometer = 0
		self.PassengerWeight = 0
		self.CargoWeight = 0
		self.PassengerCount = 0
		self.ZeroFuelWeight = 0
		self.ManifestNotes = ""
		self.MinutesTaxi = 0
		self.MinutesBurn = 0
		self.MinutesCont = 0
		self.MinutesRes = 0
		self.MinutesAlt = 0
		self.MinutesWx = 0
		self.FuelWeightTaxi = 0
		self.FuelWeightBurn = 0
		self.FuelWeightCont = 0
		self.FuelWeightRes = 0
		self.FuelWeightAlt = 0
		self.FuelWeightWx = 0
		self.DebriefReport = ""
		self.IncidentRecorded = 0
		self.IncidentReport = ""	
