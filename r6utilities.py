import requests
import base64
import os.path

rainbow_uuid = '39baebad-39e5-4552-8c25-2c9b919064e2'
stats_names = 'operatorpvp_smoke_poisongaskill,operatorpvp_timeplayed,operatorpvp_roundwon,operatorpvp_roundlost,operatorpvp_kills,operatorpvp_death,operatorpvp_mute_gadgetjammed,operatorpvp_thatcher_gadgetdestroywithemp,operatorpvp_castle_kevlarbarricadedeployed,operatorpvp_ash_bonfirewallbreached,operatorpvp_pulse_heartbeatspot,operatorpvp_doc_teammaterevive,operatorpvp_rook_armortakenteammate,operatorpvp_twitch_gadgetdestroybyshockdrone,operatorpvp_montagne_shieldblockdamage,operatorpvp_glaz_sniperkill,operatorpvp_fuze_clusterchargekill,operatorpvp_kapkan_boobytrapkill,operatorpvp_tachanka_turretkill,operatorpvp_iq_gadgetspotbyef,operatorpvp_jager_gadgetdestroybycatcher,operatorpvp_bandit_batterykill,operatorpvp_buck_kill,operatorpvp_frost_dbno,operatorpvp_blackbeard_gunshieldblockdamage,operatorpvp_valkyrie_camdeployed,operatorpvp_capitao_lethaldartkills,operatorpvp_echo_enemy_sonicburst_affected,operatorpvp_cazador_assist_kill,operatorpvp_black_mirror_gadget_deployed,operatorpvp_dazzler_gadget_detonate,operatorpvp_caltrop_enemy_affected,operatorpvp_concussionmine_detonate,operatorpvp_concussiongrenade_detonate,operatorpvp_phoneshacked,operatorpvp_attackerdrone_diminishedrealitymode,operatorpvp_tagger_tagdevice_spot,operatorpvp_rush_adrenalinerush,operatorpvp_barrage_killswithturret,operatorpvp_deceiver_revealedattackers,operatorpvp_maverick_wallbreached,operatorpvp_clash_sloweddown,operatorpvp_nomad_airjabdetonate,operatorpvp_kaid_electroclawelectrify,operatorpvp_gridlock_traxdeployed,operatorpvp_nokk_observationtooldeceived,operatorpvp_warden_killswithglasses,operatorpvp_goyo_volcandetonate,operatorpvp_amaru_distancereeled,operatorpvp_kali_gadgetdestroywithexplosivelance,operatorpvp_wamai_gadgetdestroybymagnet,weapontypepvp_kills,weapontypepvp_headshot,weapontypepvp_bulletfired,weapontypepvp_bullethit,generalpvp_timeplayed,generalpvp_matchplayed,generalpvp_killassists,generalpvp_revive,generalpvp_headshot,generalpvp_penetrationkills,generalpvp_meleekills,generalpvp_matchwon,generalpvp_matchlost,generalpvp_kills,generalpvp_death,generalpvp_bullethit,generalpvp_bulletfired,casualpvp_timeplayed,casualpvp_matchwon,casualpvp_matchlost,casualpvp_matchplayed,casualpvp_kills,casualpvp_death,rankedpvp_matchwon,rankedpvp_matchlost,rankedpvp_timeplayed,rankedpvp_matchplayed,rankedpvp_kills,rankedpvp_death,secureareapvp_matchwon,secureareapvp_matchlost,secureareapvp_matchplayed,secureareapvp_bestscore,rescuehostagepvp_matchwon,rescuehostagepvp_matchlost,rescuehostagepvp_matchplayed,rescuehostagepvp_bestscore,plantbombpvp_matchwon,plantbombpvp_matchlost,plantbombpvp_matchplayed,plantbombpvp_bestscore,generalpvp_timeplayed,generalpvp_matchplayed,generalpvp_killassists,generalpvp_revive,generalpvp_headshot,generalpvp_penetrationkills,generalpvp_meleekills,generalpvp_matchwon,generalpvp_matchlost,generalpvp_kills,generalpvp_death,generalpvp_bullethit,generalpvp_bulletfired,weapontypepvp_kills,weapontypepvp_headshot,weapontypepvp_bulletfired,weapontypepvp_bullethit,operatorpvp_smoke_poisongaskill,operatorpvp_timeplayed,operatorpvp_roundwon,operatorpvp_roundlost,operatorpvp_kills,operatorpvp_death,operatorpvp_mute_gadgetjammed,operatorpvp_thatcher_gadgetdestroywithemp,operatorpvp_castle_kevlarbarricadedeployed,operatorpvp_ash_bonfirewallbreached,operatorpvp_pulse_heartbeatspot,operatorpvp_doc_teammaterevive,operatorpvp_rook_armortakenteammate,operatorpvp_twitch_gadgetdestroybyshockdrone,operatorpvp_montagne_shieldblockdamage,operatorpvp_glaz_sniperkill,operatorpvp_fuze_clusterchargekill,operatorpvp_kapkan_boobytrapkill,operatorpvp_tachanka_turretkill,operatorpvp_iq_gadgetspotbyef,operatorpvp_jager_gadgetdestroybycatcher,operatorpvp_bandit_batterykill,operatorpvp_buck_kill,operatorpvp_frost_dbno,operatorpvp_blackbeard_gunshieldblockdamage,operatorpvp_valkyrie_camdeployed,operatorpvp_capitao_lethaldartkills,operatorpvp_echo_enemy_sonicburst_affected,operatorpvp_cazador_assist_kill,operatorpvp_black_mirror_gadget_deployed,operatorpvp_dazzler_gadget_detonate,operatorpvp_caltrop_enemy_affected,operatorpvp_concussionmine_detonate,operatorpvp_concussiongrenade_detonate,operatorpvp_phoneshacked,operatorpvp_attackerdrone_diminishedrealitymode,operatorpvp_tagger_tagdevice_spot,operatorpvp_rush_adrenalinerush,operatorpvp_barrage_killswithturret,operatorpvp_deceiver_revealedattackers,operatorpvp_maverick_wallbreached,operatorpvp_clash_sloweddown,operatorpvp_nomad_airjabdetonate,operatorpvp_kaid_electroclawelectrify,operatorpvp_gridlock_traxdeployed,operatorpvp_nokk_observationtooldeceived,operatorpvp_warden_killswithglasses,operatorpvp_goyo_volcandetonate,operatorpvp_amaru_distancereeled,operatorpvp_kali_gadgetdestroywithexplosivelance,operatorpvp_wamai_gadgetdestroybymagnet,casualpvp_timeplayed,casualpvp_matchwon,casualpvp_matchlost,casualpvp_matchplayed,casualpvp_kills,casualpvp_death,rankedpvp_matchwon,rankedpvp_matchlost,rankedpvp_timeplayed,rankedpvp_matchplayed,rankedpvp_kills,rankedpvp_death,secureareapvp_matchwon,secureareapvp_matchlost,secureareapvp_matchplayed,secureareapvp_bestscore,rescuehostagepvp_matchwon,rescuehostagepvp_matchlost,rescuehostagepvp_matchplayed,rescuehostagepvp_bestscore,plantbombpvp_matchwon,plantbombpvp_matchlost,plantbombpvp_matchplayed,plantbombpvp_bestscore'

def get_ticket(email, password):
    # create a session so we can acquire a token from Ubisoft
    response = requests.post(
        'https://public-ubiservices.ubi.com/v3/profiles/sessions',
        headers={
            'Content-Type': 'application/json',
            'Ubi-AppId': rainbow_uuid,
            'Authorization': 'Basic ' + base64.b64encode(f'{email}:{password}'.encode('ascii')).decode('ascii')
        }
    )
    return response.json()['ticket']


def get_profile_stats(ticket, uuids):
    url = 'https://public-ubiservices.ubi.com/v1/spaces/5172a557-50b5-4665-b7db-e3f2e8c5041d/sandboxes/OSBOR_PC_LNCH_A/r6playerprofile/playerprofile/progressions'
    response = requests.get(
        url=url,
        params={'profile_ids': ','.join(uuids)},
        headers={
            'Content-Type': 'application/json',
            'Ubi-AppId': rainbow_uuid,
            'Authorization': f'Ubi_v1 t={ticket}'
        }
    )
    return response.json()


def get_ranked_stats(ticket, uuids):
    url = 'https://public-ubiservices.ubi.com/v1/spaces/5172a557-50b5-4665-b7db-e3f2e8c5041d/sandboxes/OSBOR_PC_LNCH_A/r6karma/players'
    response = requests.get(
        url=url,
        params={
            'profile_ids': ','.join(uuids),
            'board_id': 'pvp_ranked',
            'region_id': 'emea',
            'season_id': '-1'
        },
        headers={
            'Content-Type': 'application/json',
            'Ubi-AppId': rainbow_uuid,
            'Authorization': f'Ubi_v1 t={ticket}'
        }
    )
    return response.json()


def get_all_stats(ticket, uuids):
    url = 'https://public-ubiservices.ubi.com/v1/spaces/5172a557-50b5-4665-b7db-e3f2e8c5041d/sandboxes/OSBOR_PC_LNCH_A/playerstats2/statistics'
    response = requests.get(
        url=url,
        params={
            'populations': ','.join(uuids),
            'statistics': stats_names
        },
        headers={
            'Content-Type': 'application/json',
            'Ubi-AppId': rainbow_uuid,
            'Authorization': f'Ubi_v1 t={ticket}'
        }
    )
    return response.json()

def get_profile_uuid(list, uuid):
    for player in list['player_profiles']:
        if player['profile_id'] == uuid:
            return player

# -------------- RANKED -----------------

def manipulate_won(status):
    if status == '0':
        # season reset?
        return 2
    elif status == '1':
        # win
        return 1
    elif status == '2':
        # loss
        return '0'
    else:
        # not recognised, return received
        return status

# find all columns in the header line
def find_columns(header, columns):
    results = {}
    for i in range(0, len(header)):
        for column in columns:
            if header[i] == column:
                results[column] = i
                break
    return results

# find the index position of a column in the header (NOT RECOMMENDED)
def find_column(header, column):
    for i in range(0, len(header)):
        if header[i] == column:
            return i
    return -1

# get how many lines there are in a file
def get_line_count(filepath):
    count = 0
    try:
        with open(filepath, 'rt') as f:
            line = f.readline()
            while line:
                count = count + 1
                line = f.readline()
    except IOError as e:
        print(f'An error occured when trying to read {filepath}.')
        raise e
    return count

# create the file if it does not exist in history folder
def create_if_not_exist(uuid, headers):
    # check if ranks history file exists
    uhrpath = f'history\\{uuid}-history-ranked.csv'
    if not os.path.isfile(uhrpath):
        print(f'{uhrpath} does not exist, creating new CSV...')
        try:
            with open(uhrpath, 'w') as f:
                # write file headers here
                # TO-DO: make this dynamic later
                f.write(','.join(headers) + '\n')
        except IOError as e:
            print(f"Could not create or save new CSV file for {uuid}")
            raise e
    return uhrpath

# write ranked match history for a specified uuid
def write_ranked_matches(uuids):
    for uuid in uuids:
        phpath = os.path.join('players', f'{uuid}.csv')
        totalcounts = get_line_count(phpath)
        if totalcounts < 2:
            raise FileNotFoundError('The file snapshot must have at least two snapshots to perform calculations and differences.')
        # we have verified that there is at least 3 lines (1 header + 2 snapshots)

        try:
            # open player history from/ path
            with open(phpath, 'rt') as f:
                # get header and split the columns
                snapshot_headers = f.readline().rstrip().split(',')
                # keep column count for later snapshot check
                columncount = len(snapshot_headers)

                # get column indices for specific column
                columns = find_columns(snapshot_headers, ['time','rkills','rdeaths','rlastwon','rlastmatchmmrchange','rmmr','grankedmatchtimeplayed'])

                # read in and split for commas
                previous = f.readline().rstrip().split(',')
                current = f.readline().rstrip().split(',')
                
                # get the path of ranked history (create if not exists)
                # uhrpath = create_if_not_exist(uuid, ['time','kills','deaths','result','mmrchange','mmr','seconds'])
                uhrpath = os.path.join('history', f'{uuid}-history-ranked.csv')

                try:
                    with open(uhrpath, 'w') as n:
                        # overwrite existing history file since the entire thing is calculated from earliest to latest
                        n.write(','.join(['time','kills','deaths','result','mmrchange','mmr','seconds']) + '\n')

                        while current and len(current) == columncount:
                            previousmmr = previous[columns['rmmr']]
                            currentmmr = current[columns['rmmr']]
                            if currentmmr != previousmmr:
                                # collect kills and deaths (and check if rank reset for new season)
                                kills = int(current[columns['rkills']]) - int(previous[columns['rkills']])
                                deaths = int(current[columns['rdeaths']]) - int(previous[columns['rdeaths']])
                                if kills >= 0 and deaths >= 0:
                                    time = current[columns['time']]
                                    won = manipulate_won(current[columns['rlastwon']])
                                    mmrchange = current[columns['rlastmatchmmrchange']]
                                    mmr = current[columns['rmmr']]
                                    timeplayed = int(current[columns['grankedmatchtimeplayed']]) - int(previous[columns['grankedmatchtimeplayed']])
                                    newline = f'{time},{str(kills)},{str(deaths)},{won},{mmrchange},{mmr},{str(timeplayed)}\n'
                                    n.writelines(newline)

                            # move forward in processing match history
                            previous = current
                            current = f.readline().rstrip().split(',')
                except IOError as e:
                    print(f'Some error occured when opening {uhrpath}.')
                    raise e
        except IOError as e:
            print(f'Some error occured when opening {phpath}.')
            raise e