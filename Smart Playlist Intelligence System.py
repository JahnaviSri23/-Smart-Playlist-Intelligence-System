user_input = input("Enter song durations in seconds separated by space: ")

durations = list(map(int, user_input.split()))

if any(d <= 0 for d in durations):
    print("Invalid Playlist: Contains non-positive duration values.")
else:
    total_duration = sum(durations)
    number_of_songs = len(durations)

    if total_duration < 300:
        category = "Too Short Playlist"
        recommendation = "Add more songs to extend listening time."

    elif total_duration > 3600:
        category = "Too Long Playlist"
        recommendation = "Consider shortening the playlist."

    elif any(durations.count(d) > 1 for d in durations):
        category = "Repetitive Playlist"
        recommendation = "Add variety to your playlist."

    elif 300 <= total_duration <= 3600 and len(set(durations)) == number_of_songs:
        category = "Balanced Playlist"
        recommendation = "Good listening session!"

    else:
        category = "Irregular Playlist"
        recommendation = "Review playlist structure."

    print("Total Duration:", total_duration, "seconds")
    print("Songs:", number_of_songs)
    print("Category:", category)
    print("Recommendation:", recommendation)