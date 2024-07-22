# Football Team Manager

## Overview

The Football Team Manager is a Python application built with Streamlit and SQLite to help manage a football team. This application provides functionality for managing players, fixtures, team selection, captains, and player roles.

## Features

### Player Management
- **Add Player**: Add a new player with details such as name, position, number, and age.
- **View Players**: View all players currently in the database.
- **Update Player**: Update details of an existing player by selecting their ID.
- **Delete Player**: Remove a player from the database by selecting their ID.

### Fixture Management
- **Add Fixture**: Schedule a new fixture for the next month with details like date and opponent.
- **View Fixtures**: View all fixtures scheduled for the next month.

### Team Selection
- **Select Team for Next Match**: Choose players for the upcoming match.

### Captain Management
- **Add Captain**: Designate a player as a captain with priority levels 1, 2, and 3.
- **View Captains**: View all captains and their priority levels.

### Player Roles
- **Assign Role**: Assign specific roles to players, including:
  - Left Corner Taker
  - Right Corner Taker
  - Penalty Taker
  - Free Kick Taker
  - Long Free Kick Taker
- **View Roles**: View assigned roles for all players.

### Player Status
- **Status Options**: Set and view player status, including:
  - Available
  - Absent
  - Injured
  - Partially Injured

### Additional Features
- **Unique Player Numbers**: Ensure that each player number is unique across the team.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/football_team_manager.git
