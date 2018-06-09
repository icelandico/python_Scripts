def dms2dd(value):
    """
    Transforms DMS given coordintes to DD.
    Type in Degrees Minutes Seconds format (Like: N53 12 12.12)
    """

    value0 = value[0]
    value1 = value.replace(" ", "")

    value11 = float(value1[1:3])
    value12 = float(value1[3:5])
    value13 = float(value1[5:])

    lat0 = value11
    lat1 = (value12/60)
    lat2 = (value13/3600)

    value21 = float(value1[1:4])
    value22 = float(value1[4:6])
    value23 = float(value1[6:])

    lon1 = value21
    lon2 = (value22 / 60)
    lon3 = (value23 / 3600)

    direction = 1

    if value0 == 'N' or value0 == 'S' or value0 == 'n' or value0 == 's':
        if value0 == 'N' or value0 =='n':
            direction *= 1
        elif value0 == 'S' or value0 =='s':
            direction *= -1
        else:
            direction = 0
        result = direction * (lat0 + lat1 + lat2)
        return result
    elif value0 == 'W' or value0 == 'E' or value0 =='w' or value0 == 'e':
        if value0 == 'e' or value0 == 'E':
            direction *= 1
        elif value0 == 'w' or value0 =='W':
            direction *= -1
        else:
            direction = 0
        result = direction*(lon1 + lon2 + lon3)
    return result
