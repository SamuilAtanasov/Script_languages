import random

class Team:
    def __init__(self, name, country, place):
        self.name =  name
        self.country = country
        self.place = place

    def __str__(self):
        return f"{self.name} ({self.country}, {self.place})"
    
def can_play(team1, team2):
    if team1.place == team2.place:
        return False
    if team1.country == team2.country:
        return False
    if (team1.country == "Ukraine" and team2.country == "Russia") or \
        (team1.country == "Russia" and team2.country == "Ukraine"):
        return False
    return True
def draw_round_of_16(teams):
    first_place = [t for t in teams if t.place == 1]
    second_place = [t for t in teams if t.place == 2]

    random.shuffle(first_place)
    random.shuffle(second_place)

    matches = []
    second_copy = second_place[:]

    for first in first_place:
        possible_opponents = [s for s in second_copy if can_play(first, s)]

        if not possible_opponents:
            return None
        
        opponent = random.choice(possible_opponents)
        matches.append((first, opponent))
        second_copy.remove(opponent)
    return matches

def main():
    teams = [
        Team("PSG", "France", 2),
        Team("Liverpool", "England", 1),
        Team("Inter", "Italy", 1),
        Team("Manchester City", "England", 1),
        Team("Leipzig", "Germany", 2),
        Team("Eintracht Frankfrut", "Germany", 2),
        Team("Napoli", "Italy", 1),
        Team("Porto", "Portugal", 2),
        Team("Club Brugge", "Belgium", 2),
        Team("Benfica", "Portugal", 1),
        Team("Tottenham", "England", 2),
        Team("Milan", "Italy", 1),
        Team("Bayer", "Germany", 1),
        Team("Real Madrid", "Spain", 2),
        Team("Chelsea", "England", 2),
        Team("Dortmund", "Germany", 1)
    ]
    attempts = 0
    while True:
        attempts += 1
        matches = draw_round_of_16(teams)

        if matches is not None:
            print(f"The lot was successfully taken after {attempts} times.\n")
        for i, (team1, team2) in enumerate(matches, start = 1):
            print(f"Match {i}: {team1.name} vs {team2.name}")
        break
if __name__ == "__main__":
    main()