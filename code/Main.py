import json
import pprint
from datetime import datetime
from collections import defaultdict
from collections import Counter


def get_streaming_history_list(filename: str) -> list:
    data_list = []
    with open(filename) as json_file:
        json_data = json.load(json_file)
        for p in json_data:
            if p['msPlayed'] > 3000:
                date_obj = datetime.strptime(p['endTime'], '%Y-%m-%d %H:%M')

                data_entry = [date_obj, p['artistName'], p['trackName'], p['msPlayed']]
                # print(data_entry)
                data_list.append(data_entry)

    # print(data_list)
    return data_list


def mostCommon(lst):
    return [Counter(col).most_common(1)[0][0] for col in zip(*lst)]


data_list = get_streaming_history_list("StreamingHistory0.json")

weekdayList = [0] * 7
monthList = [0] * 13

for entry in data_list:
    # print(entry)
    weekdayList[entry[0].weekday()] += 1
    monthList[entry[0].month] += 1

print("Dataset goes from", data_list[0][0], "to", data_list[-1][0])
print(weekdayList)
print(monthList)

print(mostCommon(data_list))


def get_most_popular_artists(data_list: list) -> dict:
    return count_most_popular_entries(data_list, 1)


def get_most_popular_songs(data_list: list) -> dict:
    return count_most_popular_entries(data_list, 2)


def count_most_popular_entries(data_list: list, entry_to_count: int) -> dict:
    counting_dict = defaultdict(int)
    for data_entry in data_list:
        counting_dict[data_entry[entry_to_count]] += 1
    return counting_dict


artist_dict = get_most_popular_artists(data_list)
print(artist_dict)

pprint.pprint(artist_dict)
pprint.pprint(get_most_popular_songs(data_list))
