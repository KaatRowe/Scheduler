import requests


circuits = {
        'Australia' : {
            'region': 'Oceania', 
            'circuits': 1,
            'location': 'Melbourne'
        },
        'Mexico' : {
            'region': 'North America',
            'circuits': 1,
            'location': 'Mexico City'
        }, # type: ignore
        'Italy' : {
            'region': 'Europe',
            'circuits': 2,
            'location': {
                1: 'Imola',
                2: 'Monza'
            }
        },
        'Brazil' : {
            'region': 'South America',
            'circuits': 1,
            'location': 'Sao Paulo'
        },
        'Bahrain' : {
            'region': 'Middle East',
            'circuits': 1,
            'location': 'Sakhir'
        },
        'Azerbaijan' : {
            'region': 'Middle East',
            'circuits': 1,
            'location': 'Baku'
        },
        'Spain' : {
            'region': 'Europe',
            'circuits': 1,
            'location': 'Montmelo'
        },
        'Monaco' : {
            'region': 'Europe',
            'circuits': 1,
            'location': 'Monte Carlo'
        },
        'Belgium' : {
            'region': 'Europe',
            'circuits': 1,
            'location': 'Stavelot'
        },
        'Canada' : {
            'region': 'North America',
            'circuits': 1,
            'location': 'Montreal'
        },
        'United States' : {
            'region': 'North America',
            'circuits': 3,
            'location': {
                1: 'Austin',
                2: 'Miami',
                3: 'Las Vegas'
            }
        },
        'Netherlands' : {
            'region': 'Europe',
            'circuits': 1,
            'location': 'Zandvoort'
        },
        'Hungary' : {
            'region': 'Europe',
            'circuits': 1,
            'location': 'Mogyorod'
        },
        'Saudi Arabia' : {
            'region': 'Middle East',
            'circuits': 1,
            'location': 'Jeddah'
        },
        'Qatar' : {
            'region': 'Middle East',
            'circuits': 1,
            'location': 'Lusail'
        },
        'Singapore' : {
            'region': 'Asia',
            'circuits': 1,
            'location': 'Marina Bay'
        },
        'Austria' : {
            'region': 'Europe',
            'circuits': 1,
            'location': 'Spielburg'
        },
        'China' : {
            'region': 'Asia',
            'circuits': 1,
            'location': 'Shanghai'
        },
        'United Kingdom' : {
            'region': 'Europe',
            'circuits': 1,
            'location': 'Silverstone'
        },
        'Japan' : {
            'region': 'Asia',
            'circuits': 1,
            'location': 'Suzuka'
        },
        'UAE' : {
            'region': 'Middle East',
            'circuits': 1,
            'location': 'Abu Dhabi'
        }
    }

def circuits_iteration(dict, region):
    e_count = 0
    na_count = 0
    sa_count = 0
    me_count = 0
    a_count = 0
    o_count = 0
    for i in dict:
        for k in dict[i].values():
            if k == 'Europe':
                e_count += dict[i].get('circuits')
            elif k == 'North America':
                na_count += dict[i].get('circuits')
            elif k == 'South America':
                sa_count +=dict[i].get('circuits')
            elif k == 'Middle East':
                me_count +=dict[i].get('circuits')
            elif k == 'Asia':
                a_count +=dict[i].get('circuits')
            elif k == 'Oceania':
                o_count +=dict[i].get('circuits')
    
    switch={
        "eu": e_count,
        "na": na_count,
        "sa": sa_count,
        "me": me_count,
        "aus": a_count,
        "oce": o_count
    }

    return switch.get(region)
    

def islamic_to_gregorian(date):
    r = requests.get('http://api.aladhan.com/v1/hToG', params=date)
    json = json.loads(r.text)
    print("Status:", json.get('code'), json.get('status'))
    data = json.get('data')
    gregorian_date = data.get('gregorian').get('date')

    return gregorian_date



#18 bye weeks including summer break, 6 sprint races

def distance_matrix(location, mode):
    original_loc = location[0]
    destination_loc = location[1]
    origin = 'origins='+ original_loc + '&destinations=' + destination_loc + 'mode=' + mode + '&key=tq2PgWqeI3erx0r3M3TVWwSl1ArIrvy2D7dw6MWgvdms6BZvRpg2GhcPZhw42ibU'
    r = requests.get('https://api.distancematrix.ai/maps/api/distancematrix/json?', params=origin)

    json = r.json()
    print("Status:", json.get('code'), json.get('status'))