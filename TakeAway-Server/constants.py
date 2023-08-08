#
# python constants for ITC-SIM API
#

#################Define columns for fix routes ############
DF_FIX_COL = {
    'vehicle': 9,
    # 'nodetype': 3,
    'schtime': 176,
    'schdotime':177,
    'PUlat': 31,
    'PUlong': 30,
    'DOlat':33,
    'DOlong':32,
    'passcount': 105,
    'name': 17,
    'PUaddr': 1,
    'DOaddr': 4,
    # 'reqtime': 19,
    'trvtime': 22,
    'trvdist': 21,
    'confnum':73,
    'phonenum': 70,
    'status': 92
}
##############################Ends here####################





DF_COLS = {
    'vehicle': 9,
    # 'nodetype': 3,
    'schtime': 176,
    'schdotime':177,
    'PUlat': 31,
    'PUlong': 30,
    'DOlat':33,
    'DOlong':32,
    'passcount': 105,
    'name': 17,
    'PUaddr': 1,
    'DOaddr': 4,
    # 'reqtime': 19,
    'trvtime': 22,
    'trvdist': 21,
    'confnum':73,
    'phonenum': 70,
    'status': 92
}

DF_FUTURE_COLS = {
    'vehicle': 0,
    'nodetype': 3,
    'schtime': 4,
    'lat': 12,
    'long': 13,
    'passcount': 14,
    'name': 16,
    'addr': 17,
    'reqtime': 19,
    'trvtime': 21,
    'trvdist': 22,
    'idletime':20,
    'confnum':15
}



LOC_COLS = {
    'vehicle': 99,
    'latitude': 105,
    'longitude': 106,
    'state': 101,
    'direction': 109,
    'stop-lat': 119,
    'stop-long': 118,
    'avlzone': 104,
    'veh-color': 6,
    'affiliateID': 34,
    'capacity':15,
    'load':127

}

ZONE_COLS = { 
    'name':1,
    'lat':46,
    'long':47,
    'ID':0,
    'color':20

}

ALERT_COLS = {
    'message':1,
    'details':9,
    'datetime': 10,
    'affiliateID':15
}



DB_CONNECT_CRED = 'Driver={Sql Server};Server=192.168.13.92;Database=DispatchManagerDB;UID=sa;PWD=Regency1;'





########################################### SAME sp calls ################################################

DB_SMART_DEVICE = """ Exec usp_LiveRouteDashboardAPIQueries @iQuery = 1, @selectedAffiliate = '{{ selectedAffiliate }}'""" # for RM Dashboard

DB_FRSMART_DEVICE = """ Exec usp_LiveRouteDashboardAPIQueries @iQuery = 1, @iTransType = 1 , @selectedAffiliate = '{{ selectedAffiliate }}' """ # for FR Dashboard

DB_ALERTS = """ Exec usp_LiveRouteDashboardAPIQueries @iQuery = 2, @dDate = '{{ date }}' """ # for RM Dashboard

DB_ZONES = """ Exec usp_LiveRouteDashboardAPIQueries @iQuery = 3 """# for RM Dashboard

DB_QUERY_TRIPS = """ Exec usp_LiveRouteDashboardAPIQueries @iQuery = 4, @dDate = '{{ date }}', @selectedAffiliate = '{{ selectedAffiliate }}' """# for RM Dashboard

# Without SET NOCOUNT ON in the query the whole query will break!!!!
FUTURE_DB_QUERY_TRIPS = """ Exec usp_LiveRouteDashboardAPIQueries @iQuery = 5, @dDate = '{{ date }}' """# for RM Dashboard

FR_GET_Statistics = """ Exec usp_LiveRouteDashboardAPIQueries @iQuery = 6, @selectedAffiliate = '{{ selectedAffiliate }}' """# for FR Dashboard

RM_GET_Statistics = """ Exec usp_LiveRouteDashboardAPIQueries @iQuery = 7, @selectedAffiliate = '{{ selectedAffiliate }}' """# for RM Dashboard

PASSENGER_LOAD_FIXED_BUS="""Exec usp_LiveRouteDashboardAPIQueries @iQuery = 8"""# for FR Dashboard

RM_INITIAL="""Exec usp_LiveRouteDashboardAPIQueries @iQuery = 9, @iuserid = '{{ userid }}' , @bpoweruser = '{{ bpoweruser }}'"""# for RM Dashboard

FR_INITIAL="""Exec usp_LiveRouteDashboardAPIQueries @iQuery = 10, @iuserid = '{{ userid }}'"""# for FR Dashboard


DB_PUBLIC_FRSMART_DEVICE = """ Exec usp_LiveRouteDashboardAPIQueries @iQuery = 11, @selectedAffiliate = '{{ selectedAffiliate }}' """

########################################### SAME sp calls ################################################








########################################### Different sp calls ################################################

ZONE_LOCATIONS = """ --SET NOCOUNT ON; usp_Zone_GetVertices WITH (NOLOCK) """

DB_STATUS = 'usp_SD_GetTripLoadStatus'

DB_FIX_ROUTE = """ Exec usp_MVGetVisualStopsForRouteMaker @dtSelectedDate = '{{ date }}', @bSetManifestNumber = 1, @bIncludePerformedTrips = 1 """# for FR Dashboard

DB_RouteStationsPolylines = """ Exec usp_InsertUpdatePolylineCoordinates @iMode = 0 """

DB_RouteStationsPolylinesPerRSTs = """ Exec usp_InsertUpdatePolylineCoordinates @iMode = 3 """

DB_FRPublicTrips = """ Exec usp_MVGetFixedRouteStopsView @dtSelectedDate = '{{ date }}', @vLoggedUserAffiliateList='{{ iAffiliateId }}', @iMode='{{ mode }}' """


DB_FRMissingTripsPLCoords = """ Exec usp_InsertUpdatePolylineCoordinates @iMode = 1 """ #for FR Public Dashboard Missing PL coords

DB_UpdateFRPublicDashboard = """ Exec usp_InsertUpdatePolylineCoordinates @iMode = 2 @vSSlat = '{{vSSlat}}', @vSSlng = '{{vSSlng}}', @vESlat = '{{vESlat}}', @vESlng = '{{vESlng}}', @vPLCoords = '{{vPLCoords}}' """ #for FR Public Dashboard Missing PL coords

DB_GetAffiliates=""" EXEC usp_GetTripsPerformanceStatistics @iMode = 1, @vAffiliateIds = '{{ @vAffiliateIds }}' """
DB_GetFundingSource=""" EXEC usp_SRPC_GetAllFundingSources @iMode=3, @iATSPID= {{ @iAffiliateId }} """

DB_GetPerformanceStatistics=""" Exec usp_GetTripsPerformanceStatistics @iMode = 0, @iAffiliateId = {{ @iAffiliateId }} , @FSIds = '{{ FSIds }}'"""
DB_GetPerformanceStatisticsTrips=""" Exec usp_GetTripsPerformanceStatistics @iMode = 0, @iAffiliateId = {{ @iAffiliateId }} , @FSIds = '{{ FSIds }}' , @vType = '{{ vType }}'"""

DB_GetODStationForReservation=""" Exec usp_GetODStationForReservation @iMode = '{{ iMode }}', @dtDate = '{{ dtDate }}', @vPickupLatitude = '{{ vPickupLatitude }}' , @vPickupLongitude = '{{ vPickupLongitude }}', @SchPUTime = '{{ SchPUTime }}', @NearByStationRadius = '{{ NearByStationRadius }}', @NearByStationMinTimeInMin = '{{ NearByStationMinTimeInMin }}', @NearByStationMaxTimeInMin = '{{ NearByStationMaxTimeInMin }}', @vPhoneNo = '{{ vPhoneNo }}', @vPersonName = '{{ vPersonName }}', @vStationAddress = '{{ vStationAddress }}' """

########################################### Different sp calls ################################################

