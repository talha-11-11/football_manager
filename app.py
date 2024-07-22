import streamlit as st
import pandas as pd
from database import (
    create_table, add_player, get_all_players, update_player, delete_player,
    add_fixture, get_all_fixtures, add_team_selection, get_team_selection,
    add_captain, get_captains, add_role, get_roles
)

# Initialize the database
create_table()

def main():
    st.image("rename.png", width=150)
    st.title("Football Team Manager")

    menu = [
        "Add Player", "View Players", "Update Player", "Delete Player",
        "Manage Fixtures", "Team Selection", "Manage Captains", "Manage Roles"
    ]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Player":
        st.subheader("Add a New Player")
        name = st.text_input("Name")
        position = st.text_input("Position")
        number = st.number_input("Number", min_value=1, step=1)
        age = st.number_input("Age", min_value=1, step=1)
        status = st.selectbox("Status", ["Available", "Absent", "Injured", "Partially Injured"])

        if st.button("Add Player"):
            add_player(name, position, number, age, status)
            st.success(f"Added {name} to the team")

    elif choice == "View Players":
        st.subheader("View All Players")
        players = get_all_players()
        if players:
            df = pd.DataFrame(players, columns=['ID', 'Name', 'Position', 'Number', 'Age', 'Status'])
            st.dataframe(df)
        else:
            st.write("No players found.")

    elif choice == "Update Player":
        st.subheader("Update a Player")
        players = get_all_players()
        df = pd.DataFrame(players, columns=['ID', 'Name', 'Position', 'Number', 'Age', 'Status'])
        st.dataframe(df)
        
        player_id = st.number_input("Select Player ID to Update", min_value=1, step=1)
        name = st.text_input("New Name")
        position = st.text_input("New Position")
        number = st.number_input("New Number", min_value=1, step=1)
        age = st.number_input("New Age", min_value=1, step=1)
        status = st.selectbox("New Status", ["Available", "Absent", "Injured", "Partially Injured"])

        if st.button("Update Player"):
            update_player(player_id, name, position, number, age, status)
            st.success(f"Updated player with ID {player_id}")

    elif choice == "Delete Player":
        st.subheader("Delete a Player")
        players = get_all_players()
        df = pd.DataFrame(players, columns=['ID', 'Name', 'Position', 'Number', 'Age', 'Status'])
        st.dataframe(df)

        player_id = st.number_input("Select Player ID to Delete", min_value=1, step=1)

        if st.button("Delete Player"):
            delete_player(player_id)
            st.success(f"Deleted player with ID {player_id}")

    elif choice == "Manage Fixtures":
        st.subheader("Manage Fixtures")
        action = st.selectbox("Select Action", ["Add Fixture", "View All Fixtures"])

        if action == "Add Fixture":
            date = st.date_input("Date")
            opponent = st.text_input("Opponent")
            venue = st.text_input("Venue")
            if st.button("Add Fixture"):
                add_fixture(date.strftime("%Y-%m-%d"), opponent, venue)
                st.success("Fixture added successfully!")

        elif action == "View All Fixtures":
            fixtures = get_all_fixtures()
            df = pd.DataFrame(fixtures, columns=['ID', 'Date', 'Opponent', 'Venue'])
            st.dataframe(df)

    elif choice == "Team Selection":
        st.subheader("Team Selection")
        fixtures = get_all_fixtures()
        fixture_ids = [f[0] for f in fixtures]
        selected_fixture = st.selectbox("Select Fixture", fixture_ids, format_func=lambda x: next(f[2] for f in fixtures if f[0] == x))
        if selected_fixture:
            players = get_all_players()
            player_ids = [p[0] for p in players]
            selected_players = st.multiselect("Select Players for the Fixture", player_ids, format_func=lambda x: next(p[1] for p in players if p[0] == x))
            is_substitute = st.checkbox("Mark as Substitute")
            if st.button("Save Team Selection"):
                for player_id in selected_players:
                    add_team_selection(selected_fixture, player_id, is_substitute)
                st.success("Team selection saved successfully!")

            st.subheader("Current Team Selection")
            team_selection = get_team_selection(selected_fixture)
            if team_selection:
                team_data = [(next(p[1] for p in players if p[0] == ts[1]), ts[2]) for ts in team_selection]
                df = pd.DataFrame(team_data, columns=['Player Name', 'Substitute'])
                st.dataframe(df)

    elif choice == "Manage Captains":
        st.subheader("Manage Captains")
        action = st.selectbox("Select Action", ["Add Captain", "View Captains"])
        
        if action == "Add Captain":
            players = get_all_players()
            player_ids = [p[0] for p in players]
            player_names = [p[1] for p in players]
            player_name = st.selectbox("Select Player", player_names)
            priority = st.number_input("Priority", min_value=1, step=1)
            if st.button("Add Captain"):
                player_id = player_ids[player_names.index(player_name)]
                add_captain(priority, player_id)
                st.success("Captain added successfully!")
        
        elif action == "View Captains":
            captains = get_captains()
            if captains:
                df = pd.DataFrame(captains, columns=['Priority', 'Player ID'])
                st.dataframe(df)
            else:
                st.write("No captains found.")

    elif choice == "Manage Roles":
        st.subheader("Manage Roles")
        action = st.selectbox("Select Action", ["Assign Role", "View Roles"])

        if action == "Assign Role":
            players = get_all_players()
            player_ids = [p[0] for p in players]
            player_names = [p[1] for p in players]
            player_name = st.selectbox("Select Player", player_names)
            role = st.selectbox("Select Role", ["Left Corner Taker", "Right Corner Taker", "Penalty Taker", "Free Kick Taker", "Long Free Kick Taker"])
            if st.button("Assign Role"):
                player_id = player_ids[player_names.index(player_name)]
                add_role(role, player_id)
                st.success("Role assigned successfully!")

        elif action == "View Roles":
            roles = get_roles()
            if roles:
                df = pd.DataFrame(roles, columns=['Role', 'Player ID'])
                st.dataframe(df)
            else:
                st.write("No roles found.")

if __name__ == '__main__':
    main()
