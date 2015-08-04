import datetime

class Pilot(object):
    def __init__(self,id = 0):
		self.id = id
        self.FirstName = ""
        self.Surname = ""
        self.Callsign = ""
        self.HighestRank = 0 # gflConst.RankC
        self.DOB = datetime.datetime(1800,01,01)
        self.PasswordHash = ""
        self.PasswordSalt = ""
        self.Permissions = 0 # gflConst.LogonC
        self.DurationDay = datetime.timedelta()
        self.DurationNight = datetime.timedelta()
        self.TotalCompletedFlights = 0
        self.Remarks = ""