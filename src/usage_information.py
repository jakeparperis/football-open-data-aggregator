from statsbombpy import sb
import sb_ids as ids

def display_competitions(gender='m'):
    if gender == 'm' or gender == 'men' or gender == 'mens':
        print("Men's Competitions (name - id):\n--------------------------------------------------")

        for key, value in ids.mens_comp_ids.items():
            print(f"{key} - {value}")
        print()

    elif gender == 'w' or gender == 'women' or gender == 'womens':
        print("Women's Competitions (name - id):\n--------------------------------------------------")

        for key, value in ids.womens_comp_ids.items():
            print(f"{key} - {value}")
        print()

def display_seasons(comp_id):
    seasons_exist = False
    comps = sb.competitions()
    comps = comps.sort_values(by='season_id')

    print("Available Seasons (season - id):\n--------------------------------------------------")
    for _, comp in comps.iterrows():
        if comp['competition_id'] == comp_id:
            seasons_exist = True
            print(f'{comp['season_name']} - {comp["season_id"]}')

    if not seasons_exist:
        print("ERROR: No seasons available or no competition found with the specified id.")


display_competitions()
display_seasons(2)