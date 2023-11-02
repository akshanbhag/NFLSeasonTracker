# NFLSeasonTracker
This application accesses a database about specific NFL seasons and how each team and player performed. This project uses Python, HTML, Django.
The main table that is used is the Games table, which has the following fields: game_id, home_team, away_team, winner, date_played, week_number. All of these fields are integer values, except the date_played is in a MM/DD/YYYY format.
When the project is run, there are two URLs to go to.
For the games_interface(add/edit/delete): http://127.0.0.1:8000/seasontracker/games_interface
For the report_interface: http://127.0.0.1:8000/seasontracker/report_interface
