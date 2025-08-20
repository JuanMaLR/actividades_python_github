OFFSET_TO_TZ = {
    "-1200": "Etc/GMT+12",
    "-1100": "Pacific/Niue",
    "-1000": "Pacific/Honolulu",
    "-0900": "America/Anchorage",
    "-0800": "America/Los_Angeles",
    "-0700": "America/Denver",
    "-0600": "America/Mexico_City",
    "-0500": "America/New_York",
    "-0400": "America/Santiago",
    "-0300": "America/Sao_Paulo",
    "-0200": "Atlantic/South_Georgia",
    "-0100": "Atlantic/Cape_Verde",
    "+0000": "Etc/UTC",
    "+0100": "Europe/Madrid",
    "+0200": "Europe/Berlin",
    "+0300": "Europe/Moscow",
    "+0330": "Asia/Tehran",
    "+0400": "Asia/Dubai",
    "+0430": "Asia/Kabul",
    "+0500": "Asia/Karachi",
    "+0530": "Asia/Kolkata",
    "+0545": "Asia/Kathmandu",
    "+0600": "Asia/Dhaka",
    "+0630": "Asia/Yangon",
    "+0700": "Asia/Bangkok",
    "+0800": "Asia/Shanghai",
    "+0830": "Asia/Pyongyang",
    "+0900": "Asia/Tokyo",
    "+0930": "Australia/Darwin",
    "+1000": "Australia/Sydney",
    "+1030": "Australia/Lord_Howe",
    "+1100": "Pacific/Guadalcanal",
    "+1200": "Pacific/Auckland",
    "+1245": "Pacific/Chatham"
}

"""Programa final: Que el programa lea los logs de nginx e identifique las IPs, el agent id, http code, http method y hora y fecha de la petición.
1. 167.235.143.113 - - [17/Aug/2025:06:34:07 -0600] "HEAD / HTTP/1.1" 200 0 "https://www.kolibers.com" "Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/)"

IP: 167.235.143.113
Date: 17/Aug/2025
Time: 06:34:07
Time zone: Mexico City
Method: HEAD
Resource:  /
HTTP Code: 200
User Agent: Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/

2. 46.136.223.20 - - [17/Aug/2025:06:37:39 -0600] "GET /images/blog/hydra-ssh.png HTTP/1.1" 200 297784 "https://www.google.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.7 Mobile/15E148 Safari/604.1"

IP: 46.136.223.20
Date: 17/Aug/2025
Time: 06:37:29
Time zone: Mexico City
Method: GET
Resource:  /images/blog/hydra-ssh.png
HTTP Code: 200
User Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.7 Mobile/15E148 Safari/604.1
"""

# Parsear una línea del archivo de logs
# Por posición 
def parse_log(line):
    segments = line.split(" ", 11)
    ip = segments[0]
    print(f"IP: {ip}")
    date_and_time = segments[3]
    # Forma larga con una lista
    """ date_and_time_list = date_and_time.split(':', 1)
    print(f"Date: {date_and_time_list[0].replace('[', '')}")
    print(f"Time: {date_and_time_list[1]}") """
    # Forma corta unpacking
    [date, time] = date_and_time.split(':', 1)
    print(f"Date: {date.replace('[', '')}")
    print(f"Time: {time}")
    timezone = segments[4].replace(']', '')
    print(f"Time zone: {OFFSET_TO_TZ[timezone].split('/')[1].replace('_', ' ')}")
    method = segments[5].replace('"', '')
    print(f"Method: {method}")
    resource = segments[6]
    print(f"Resource: {resource}")
    http_code = segments[8]
    print(f"HTTP Code: {http_code}")
    agent = segments[11].replace('"', '')
    print(f"User Agent: {agent}")

# Variable con ejemplo de una línea de un log file
line = '167.235.143.113 - - [17/Aug/2025:06:34:07 -0600] "HEAD / HTTP/1.1" 200 0 "https://www.kolibers.com" "Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/)"'
parse_log(line)





