import datetime

class Aircraft(object):
    def __init__(self,id = 0):
        self.id = id
        self.Manufacturer = ""
        self.Model = ""
        self.Variant = ""
        self.Type = 0 # gflConst.AircraftC
        self.VMinOperating = 0
        self.VRotation = 0
        self.VClimb = 0
        self.VFlapsLimit = 0
        self.VLanding = 0
        self.MinRunwayLength = 0
        self.WeightTakeOffMax = 0
        self.WeightEmpty = 0
        self.WeightFuelMax = 0
        self.MaxPAXCount = 0
        self.AltitudeMax = 0
        self.MaxRangeNm = 0
        self.DurationMaxEndurance = datetime.timedelta()
        self.EngineType = 0 # gflConst.EngineC
        self.EngineCount = 0
        self.FuelCruisePPH = 0
        self.FuelMaxPPH = 0
        self.DurationTotalFlight = datetime.timedelta()
        self.MfgDate = 0
        self.Remarks = ""		
