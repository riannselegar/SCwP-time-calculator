def add_time(start, duration, day=None):
    weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    splitedStart = start.split(":")
    startHour = int(splitedStart[0])
    startMinute = int(splitedStart[1].split()[0])
    startAMPM = splitedStart[1].split()[1]

    splitedDuration = duration.split(":")
    durationHour = int(splitedDuration[0])
    durationMinute = int(splitedDuration[1])

    remainingHours, finalMinute = divmod((startMinute + durationMinute), 60)
    remainingAMPM, finalHour = divmod((startHour + durationHour + remainingHours), 12)

    remainingDays, remainingTime = divmod(remainingAMPM, 2)

    if startAMPM == "PM" and remainingTime == 1:
        finalAMPM = "AM"
        remainingDays += 1
    elif startAMPM == "AM" and remainingTime == 1:
        finalAMPM = "PM"
    else:
        finalAMPM = startAMPM

    if finalHour == 0:
        finalHour = 12

    finalTime = str(finalHour) + ":" + str(finalMinute).zfill(2) + " " + finalAMPM

    if day is not None:
        finalDay = weekDays[(weekDays.index(day.capitalize())+remainingDays) % 7]
        finalTime += f", {finalDay}"

    if remainingDays == 1:
        finalTime += " (next day)"
    elif remainingDays > 1:
        finalTime += f" ({remainingDays} days later)"

    return finalTime