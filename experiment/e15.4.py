import webbrowser

user_data = input("Enter a search team: ").replace(" ", "+")
webbrowser.open(f"https://www.google.com/search?q={user_data}")
