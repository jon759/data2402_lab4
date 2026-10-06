from classes1 import Team, Driver

def load_teams(filename: str)-> dict:
    """reads data, creates Team object and addes Driver objects to Team. Stores and returns Team objects in a collection"""
    # collection should contain 10 Team objects, each with 2 or more Driver object
    teams = {}
    with open(filename, 'r') as f:
        f.readline()
        for line in f:
            line = line.strip()
            driver_name, team_name, points = line.split(',')

            if team_name not in teams:
            # create team object
                teams[team_name] = Team(team_name)

            # create driver object
            driver = Driver(driver_name, int(points))

            # add driver to team
            teams[team_name].add_driver(driver)

    return teams

def main()-> None:
    teams = load_teams('f1_points.csv')
    # print(len(teams))
    sorted_teams = sorted(teams.values())
    # print(sorted_teams)
    for team in sorted_teams:
        print(team)

if __name__ == '__main__':
    main()
    
        
