def get_hours_minutes_seconds(seconds):
    returnString = ""
    days = seconds//86400
    if days != 0:
        returnString=returnString+str(days)+"d "
        seconds=seconds-(days * 86400)
    hours = seconds//3600
    if hours != 0:
        returnString=returnString+str(hours)+"h "
        seconds=seconds-(hours * 3600)
    minutes = seconds//60
    if minutes != 0:
        returnString=returnString+str(minutes)+"m "
        seconds=seconds-(minutes * 60)
    if seconds != 0:
        returnString=returnString+str(seconds)+"s"
    return returnString
    
print(get_hours_minutes_seconds(90042))