import json
from datetime import datetime


def get_streaming_history_list(filename: str) -> list:
    data_list = []
    with open(filename) as json_file:
        json_data = json.load(json_file)
        # print(data)
        new_dict = {}
        print(json_data)

        for p in json_data:
            if p['msPlayed'] > 3000:
                date_obj = datetime.strptime(p['endTime'], '%Y-%m-%d %H:%M')

                data_entry = [date_obj, p['artistName'], p['trackName'], p['msPlayed']]
                print(data_entry)
                data_list.append(data_entry)

    print(data_list)
    return data_list


data_list = get_streaming_history_list("StreamingHistory0.json")

weekdayList = [0] * 7
monthList = [0] * 13

print(weekdayList)
for entry in data_list:
    print(entry)
    weekdayList[entry[0].weekday()] += 1
    monthList[entry[0].month] += 1

print(weekdayList)
print(monthList)

