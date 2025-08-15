import sb_ids as ids


def display_competitions(gender='m'):
    if gender == 'm' or gender == 'men' or gender == 'mens':
        print("Men's Competitions:\n--------------------------------------------------")

        for key, value in ids.mens_comp_ids.items():
            print(f"{key}: {value}")
        print()

    elif gender == 'w' or gender == 'women' or gender == 'womens':
        print("Women's Competitions:\n--------------------------------------------------")

        for key, value in ids.womens_comp_ids.items():
            print(f"{key}: {value}")
        print()

def display_seasons(comp_id, gender='m'):
    comp_name = None

    if gender == 'm' or gender == 'men' or gender == 'mens':
        for key, value in ids.mens_comp_ids.items():
            if value == comp_id:
                comp_name = key
                break

    if comp_name is not None:
        dict_to_display_name = "season_ids_" + comp_name
        try:
            dict_to_display = getattr(ids, dict_to_display_name)
        except AttributeError:
            print("ERROR: No seasons found for this competition.")
            return
    else:
        print("ERROR: Competition not found.")
        return

    print(f"{comp_name}\n--------------------------------------------------")
    for key, value in dict_to_display.items():
        print(f"{key}: {value}")

display_competitions()
display_seasons(7)