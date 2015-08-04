import datetime

class PilotAircraft(object):
    def __init__(self,id = 0):
		self.id = id
        self.Rank = 0 # gflConst.RankC
        self.CompletedFlights = 0
        self.DurationDay = datetime.timedelta()
        self.DurationNight = datetime.timedelta()
        self.WxRating = 0 # gflConst.WxC
        self.TotalCargoWeight = 0
        self.TotalPAXWeight = 0
        self.TotalPAXCount = 0