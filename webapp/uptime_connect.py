# encoding: iso-8859-1
import os

# All configuration for connection with UptimeRobot

# Variable URL always have this radical
URL = "https://api.uptimerobot.com/v2/"

'''
Possible Values for the METHOD_NAME variable:
    - getAccountDetails
    - getMonitors
    - newMonitor
    - editMonitor
    - deleteMonitor
    - resetMonitor
    - getAlertContacts
    - newAlertContact
    - editAlertContact
    - deleteAlertContact
    - getMWindows
    - newMWindow
    - editMWindow
    - deleteMWindow
    - getPSPs
    - newPSP
    - editPSP
    - deletePSP

'''
METHOD_NAME = "getMonitors"

# This is the variable used to connect with the UptimeRobot
URL_CONNECT = URL+METHOD_NAME

'''
VARIABLE FORMAT sets the return type for UptimeRobot
Possible values:
    - json
    - xml
'''
FORMAT = "json"

# PARAMETERS LIST FOR THE PAYLOAD VARIABLE
'''
    - api_key - required
    - monitors - optional (if not used, will return all monitors in an account.
                 Else, it is possible to define any number of monitors with
                 their IDs like: monitors=15830-32696-83920)
    - types - optional (if not used, will return all monitors types (HTTP,
    keyword, ping..) in an account.
                 Else, it is possible to define any number of monitor types
                 like: types=1-3-4)
    - statuses - optional (if not used, will return all monitors statuses (up,
        down, paused) in an account.
                 Else, it is possible to define any number of monitor statuses
                 like: statuses=2-9)
    - custom_uptime_ratios - optional (defines the number of days to calculate
        the uptime ratio(s) for.
                 Ex: custom_uptime_ratios=7-30-45 to get the uptime ratios for
                  those periods)
    - custom_uptime_ranges - optional (defines the ranges to calculate the
        uptime ratio(s) for.
                 Ex: custom_uptime_ranges=1465440758_1466304758 to get the
                    uptime ratios for those periods.
                 It is possible to send multiple ranges like
                 1465440758_1466304758-1434682358_1434855158)
    - all_time_uptime_ratio - optional (returns the "all time uptime ratio".
                 It will slow down the response a bit and, if not really
                 necessary, suggest not using it. Default is 0)
    - all_time_uptime_durations - optional (returns the "all time durations
            of up-down-paused events".
                 It will slow down the response a bit and, if not really
                 necessary, suggest not using it. Default is 0)
    - logs - optional (defines if the logs of each monitor will be returned.
                 Should be set to 1 for getting the logs. Default is 0)
    - logs_start_date - optional and works only for the Pro Plan as 24 hour+
            logs are kept only in the Pro Plan
                 (starting date of the response times, formatted as Unix time
                 and must be used with response_times_end_date) (can only be
                 used if monitors parameter is used with a single id and
                 response_times_end_date - response_times_start_date can't be
                 more than 7 days)
    - logs_end_date - optional and works only for the Pro Plan as 24 hour+
    logs are kept only in the Pro Plan
                 (ending date of the response times, formatted as Unix time
                 and must be used with response_times_start_date) (can only
                 be used if monitors parameter is used with a single id and
                 response_times_end_date - response_times_start_date can't be
                 more than 7 days)
    - logs_limit - optional (the number of logs to be returned (descending
            order). If empty, all logs are returned.
    - response_times - optional (defines if the response time data of each
            monitor will be returned.
                 Should be set to 1 for getting them.
                 Default is 0)
    - response_times_limit - optional (the number of response time logs to be
            returned (descending order). If empty, last 24 hours of logs are
            returned (if response_times_start_date and response_times_end_date
                  are not used).
    - response_times_average - optional (by default, response time value of
        each check is returned.
                 The API can return average values in given minutes.
                 Default is 0. For ex: the Uptime Robot
                 dashboard displays the data averaged/grouped in 30 minutes)
    - response_times_start_date - optional (starting date of the logs,
        formatted as Unix time and must be used with logs_end_date)
        (can only be used if monitors parameter is used with a single id)
    - response_times_end_date - optional (ending date of the logs, formatted
        as Unix time and must be used with logs_start_date)
        (can only be used if monitors parameter is used with a single id)
    - alert_contacts - optional (defines if the alert contacts set for the
        monitor to be returned. Default is 0)
    - mwindows - optional (the maintenance windows for the monitor which can
        be mentioned with their
                 IDs like 345-2986-71)
    - custom_http_headers - optional (defines if the custom HTTP headers of
        each monitor will be returned.
                 Should be set to 1 for getting them. Default is 0)
    - timezone - optional (defines if the user's timezone should be returned.
                 Should be set to 1 for getting it. Default is 0)
    - offset - optional (used for pagination. Defines the record to start
        paginating. Default is 0)
    - limit - optional (used for pagination. Defines the max number of records
        to return for the response.
                 Default and max. is 50)
    - search - optional (a keyword of your choice to search within url and
        friendly_name and get filtered results)
'''
PAYLOAD = "api_key="+os.environ['UPTIMEROBOT_TOKEN']+"&"
PAYLOAD += "format="+FORMAT+"&"
PAYLOAD += "logs=1&"
# PAYLOAD += "logs_limit="+LOGS_LIMIT+"&"
PAYLOAD += "timezone=1"

# VARIABLE HEADERS have this value always
HEADERS = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
}
