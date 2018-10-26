def reformateDate(dates):
    days2num = {"1st": "01", "2nd": "02", "3rd": "03", "4th": "04", "5th": "05", "6th": "06",
                "7th": "07", "8th": "08", "9th": "09", "10th": "10", "11th": "11", "12th": "12",
                "13th": "13", "14th": "14", "15th": "15", "16th": "16", "17th": "17", "18th": "18",
                "19th": "19", "20th": "20", "21st": "21", "22nd": "22", "23rd": "23", "24th": "24",
                "25th": "25", "26th": "26", "27th": "27", "28th": "28", "29th": "29", "30th": "30", "31st": "31"}

    month2num = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
                 "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

    results = []
    for date in dates:
        day, month, year = date.split()
        res = year+"-"+month2num[month]+"-"+days2num[day]
        results.append(res)
    return results


date_list = ["1st Mar 1984", "2nd Feb 2013", "4th Apr 1990"]
correct_format = reformateDate(date_list)
print(correct_format)
