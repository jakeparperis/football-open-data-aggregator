from statsbombpy import sb


def display_competitions():
    comps = sb.competitions()
    comps = comps.sort_values(by='competition_id')
    comps_displayed = []

    print("Available Competitions (Competition - id):\n--------------------------------------------------")
    for _, comp in comps.iterrows():
        if comp['competition_id'] not in comps_displayed:
            comps_displayed.append(comp['competition_id'])
            print(f"{comp['competition_name']} - {comp['competition_id']}")

    print()

def display_seasons(comp_id):
    seasons_exist = False
    comps = sb.competitions()
    comps = comps.sort_values(by='season_id')

    print("Available Seasons (season - id):\n--------------------------------------------------")
    for _, comp in comps.iterrows():
        if comp['competition_id'] == comp_id:
            seasons_exist = True
            print(f"{comp['season_name']} - {comp['season_id']}")

    if not seasons_exist:
        print("ERROR: No seasons available or no competition found with the specified id.")

    print()

display_competitions()
display_seasons(2)