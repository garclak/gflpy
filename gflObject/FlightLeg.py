import datetime

class FlightLeg(object):
    def __init__(self,id = 0):
		self.id = id
		CalcMinutes = datetime.timedelta()
		ActMinutes = datetime.timedelta()
		ArrDateUTC = datetime.datetime(1800,01,01)
		PlanAltitude = 0 
		PlanAirspeed = 0 
		PlanFuelWeight = 0 
		MinFuelWeight = 0 
		ActFuelWeight = 0 
		PlanWindMagBearing = 0 
		PlanWindSpeed = 0 
