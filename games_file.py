import array
import json


class game_file:

    games_list = []

    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def latest_game_array(file_path) -> array:
        # open file
        file_path = open('games.json', 'r')
        # read file
        games_list = json.loads(file_path.read())
        # close file
        file_path.close()

        return games_list

    # adds game to array json file: returns true if added, returns false if not
    def add_game(self, title: str, array):
        # convert string to lowercase
        title.lower()

        # check it does not exisit
        if title not in array:
            # add to array
            array.append(title)

            with open('games.json', 'w') as outfile:
                new_games_json = json.dumps(array)
                outfile.seek(0)
                outfile.write(new_games_json)
                outfile.truncate()

            return True
        else:
            return False
