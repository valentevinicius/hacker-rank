import os

def timeConversion(s):
    hour = int(s[0:2])
    t_format = s[-2:]  # AM/PM
    if t_format == "AM":
        if hour == 12:
            hour = 00
    elif t_format == "PM":
        if hour == 12:
            hour = 12
        elif hour >= 0 and hour <= 12:
            hour += 12

    s = s.replace(t_format, "")
    hours = "{:02d}".format(abs(hour))
    converted_time = str(hours) + s[2:]
    return converted_time
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()