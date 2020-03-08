import time
import os.path
import json
from r6utilities import get_ticket, get_profile_uuid, get_profile_stats, get_ranked_stats, get_all_stats

class r6proc():
    def __init__(self):
        # get email and password from config.json
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)
            self.ticket = get_ticket(config['email'], config['password'])
        except IOError as e:
            print("Make sure config.json.example has been renamed to config.json with correct values.")
            raise e

    def process_uuids(self, uuids):
        profile_stats = get_profile_stats(self.ticket, uuids)
        ranked_stats = get_ranked_stats(self.ticket, uuids)
        all_stats = get_all_stats(self.ticket, uuids)
        for player_uuid in uuids:
            print(f'Processing {player_uuid}')
            base_path = 'players'
            if not os.path.exists(base_path):
                os.makedirs(base_path)

            file_path = f'{player_uuid}.csv'
            full_path = os.path.join(base_path, file_path)

            profile = get_profile_uuid(profile_stats, player_uuid)
            ranked = ranked_stats['players'][player_uuid]
            general = all_stats['results'][player_uuid]

            kv_pairs = {
                # profile stats
                'time':                         str(int(time.time())),
                'level':                        str(profile['level']),
                'xp':                           str(profile['xp']),

                # current ranked season stats
                'rkills':                       str(ranked['kills']),
                'rdeaths':                      str(ranked['deaths']),
                'rwins':                        str(ranked['wins']),
                'rlosses':                      str(ranked['losses']),
                'rlastwon':                     str(ranked['last_match_result']),
                'rabandons':                    str(ranked['abandons']),
                'rlastmatchmmrchange':          str(ranked['last_match_mmr_change']),
                'rmmr':                         str(ranked['mmr']),
                'rmaxmmr':                      str(ranked['max_mmr']),
                'rskillmean':                   str(ranked['skill_mean']),
                'rskillstdev':                  str(ranked['skill_stdev']),
                'rlastmatchskillmeanchange':    str(ranked['last_match_skill_mean_change']),
                'rlastmatchskillstdevchange':   str(ranked['last_match_skill_stdev_change']),

                # overall casual stats
                'gcasualmatchwon':              str(general['casualpvp_matchwon:infinite']),
                'gcasualmatchlost':             str(general['casualpvp_matchlost:infinite']),
                'gcasualmatchtimeplayed':       str(general['casualpvp_timeplayed:infinite']),
                'gcasualmatchesplayed':         str(general['casualpvp_matchplayed:infinite']),
                'gcasualkills':                 str(general['casualpvp_kills:infinite']),
                'gcasualdeaths':                str(general['casualpvp_death:infinite']),

                # overall ranked stats
                'grankedmatchwon':              str(general['rankedpvp_matchwon:infinite']),
                'grankedmatchlost':             str(general['rankedpvp_matchlost:infinite']),
                'grankedmatchtimeplayed':       str(general['rankedpvp_timeplayed:infinite']),
                'grankedmatchesplayed':         str(general['rankedpvp_matchplayed:infinite']),
                'grankedkills':                 str(general['rankedpvp_kills:infinite']),
                'grankeddeaths':                str(general['rankedpvp_death:infinite']),

                # overall stats
                'gbulletshit':                  str(general['generalpvp_bullethit:infinite']),
                'gbulletsfired':                str(general.get('generalpvp_bulletfired:infinite', "0")),
                'gheadshots':                   str(general['generalpvp_headshot:infinite']),
                'gkills':                       str(general['generalpvp_kills:infinite']),
                'gdeaths':                      str(general['generalpvp_death:infinite']),
                'gassists':                     str(general['generalpvp_killassists:infinite']),
                'gmatchesplayed':               str(general['generalpvp_matchplayed:infinite']),
                'gtimeplayed':                  str(general['generalpvp_timeplayed:infinite']),
                'gmatcheswon':                  str(general['generalpvp_matchwon:infinite']),
                'gmatcheslost':                 str(general['generalpvp_matchlost:infinite'])
            }

            # if file csv does not exist
            if not os.path.isfile(full_path):
                try:
                    with open(full_path, 'a+') as f:
                        # write file headers here
                        f.write(','.join(list(kv_pairs.keys())) + '\n')
                except IOError as e:
                    print(e)

            # begin writing one-line stats
            try:
                with open(full_path, 'rt+') as f:
                    # reach to the latest line and get latest line
                    latest = f.readline()
                    current = f.readline()
                    while len(current) > 0:
                        latest = current
                        current = f.readline()

                    # split latest line from file csv to array
                    data = latest.replace('\n', '').split(',')

                    # check if latest line is any different from current data
                    different = False
                    values = list(kv_pairs.values())
                    for i in range(1, len(data)):
                        # skip unix time by starting from 1
                        if data[i] != values[i]:
                            # is different, prepare for writing
                            different = True
                            break
                
                    if different:
                        print(f'{player_uuid} is changed, updating...')
                        # write time-based one-line data here
                        f.write(','.join(values) + '\n')
                    else:
                        print(f'{player_uuid} is not updated, continuing...')
            except IOError as e:
                print(e)