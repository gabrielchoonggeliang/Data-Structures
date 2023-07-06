movies = ["Up", "Toy Story", "Coco", "Cars", "Pinocchio", "The Star",
          "The Sound of Music", "Mary Poppins", "Enchanted", "Arrival"]

movies.sort()

adj_matrix = {
    "Arrival": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    "Cars": [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    "Coco": [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    "Enchanted": [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    "Mary Poppins": [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    "Pinocchio": [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    "The Sound of Music": [0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    "The Star": [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    "Toy Story": [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    "Up": [0, 0, 0, 1, 1, 0, 1, 1, 0, 0]
}

import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def select():
    return int(input("> "))


def movie_list(adj_matrix):
    clear_screen()
    print("Select movie to watch:")
    for k, movie in enumerate(movies):
        print(f"{k + 1}. {movie}")

    try:
        movie_selection = select()
    except ValueError:
        print("Please enter a number between 1 and 10.")
        return

    clear_screen()
    if movie_selection < 1 or movie_selection > 10:
        print("Please try again")
        return

    selected_movie = movies[movie_selection - 1]

    if selected_movie not in adj_matrix:
        print(f"The movie '{selected_movie}' is not in the list.")
        return

    print(f"Selected movie: {selected_movie}")
    print("\nBFS or DFS? (1 for BFS, 2 for DFS), you can only choose once.")
    traverse_selection = select()
    clear_screen()

    # Actual index needs to subtract one, assume that only 1 or 2 will be the input
    if traverse_selection == 1:
        bfs(selected_movie)
    elif traverse_selection == 2:
        dfs(adj_matrix, selected_movie, {})
    else:
        print("Please try again")


def bfs_manual(start_movie):
    print(f"You chose manual BFS, watching {start_movie}")
    visited = {}
    queue = []
    queue.append(start_movie)

    while queue:
        current_movie = queue.pop(0)
        if current_movie in visited:
            continue

        print(f"Currently watching: {current_movie}")
        visited[current_movie] = True

        suggestions = []
        for idx, neighbor in enumerate(movies):
            if adj_matrix[current_movie][idx] == 1 and neighbor not in visited:
                suggestions.append(neighbor)

        if not suggestions:
            print("No more suggestions. Enjoy your movie marathon!")
            break

        print("Suggestions:")
        for i, suggestion in enumerate(suggestions):
            print(f"{i + 1}. {suggestion}")

        selection = select_movie(suggestions)
        if selection is None:
            print("Invalid selection. Exiting...")
            return
        selected_movie = suggestions[selection - 1]
        queue.append(selected_movie)


def dfs_manual(matrix, start_movie, visited):
    if start_movie not in movies:
        print(f"The movie '{start_movie}' is not in the list.")
        return

    if start_movie in visited:
        return

    print(f"Currently watching: {start_movie}")
    visited[start_movie] = True

    suggestions = []
    for idx, neighbor in enumerate(movies):
        if adj_matrix[start_movie][idx] == 1 and neighbor not in visited:
            suggestions.append(neighbor)

    if not suggestions:
        print("No more suggestions. Enjoy your movie marathon!")
        return

    print("Suggestions:")
    for i, suggestion in enumerate(suggestions):
        print(f"{i + 1}. {suggestion}")

    selection = select_movie(suggestions)
    if selection is None:
        print("Invalid selection. Exiting...")
        return
    selected_movie = suggestions[selection - 1]
    dfs_manual(matrix, selected_movie, visited)


def bfs_auto(start_movie):
    print(f"You chose automatic BFS, watching {start_movie}")
    visited = {}
    queue = []
    queue.append(start_movie)

    while queue:
        current_movie = queue.pop(0)
        if current_movie in visited:
            continue

        print(f"Currently watching: {current_movie}")
        visited[current_movie] = True

        for idx, neighbor in enumerate(movies):
            if adj_matrix[current_movie][idx] == 1 and neighbor not in visited:
                queue.append(neighbor)


def dfs_auto(matrix, start_movie, visited):
    if start_movie not in movies:
        print(f"The movie '{start_movie}' is not in the list.")
        return

    if start_movie in visited:
        return

    print(f"Currently watching: {start_movie}")
    visited[start_movie] = True

    for idx, neighbor in enumerate(movies):
        if adj_matrix[start_movie][idx] == 1 and neighbor not in visited:
            dfs_auto(matrix, neighbor, visited)


def select_movie(suggestions):
    print("\nManual Selection:")
    print("Select the next movie to watch (or enter 0 for automatic selection):")
    for i, suggestion in enumerate(suggestions):
        print(f"{i + 1}. {suggestion}")

    try:
        selection = select()
        if selection == 0:
            return None
        if selection < 1 or selection > len(suggestions):
            return None
        return selection
    except ValueError:
        return None


def movie_list(adj_matrix):
    clear_screen()
    print("Select movie to watch:")
    for k, movie in enumerate(movies):
        print(f"{k + 1}. {movie}")

    try:
        movie_selection = select()
    except ValueError:
        print("Please enter a number between 1 and 10.")
        return

    clear_screen()
    if movie_selection < 1 or movie_selection > 10:
        print("Please try again")
        return

    selected_movie = movies[movie_selection - 1]

    if selected_movie not in adj_matrix:
        print(f"The movie '{selected_movie}' is not in the list.")
        return

    print(f"Selected movie: {selected_movie}")
    print("\nChoose the traversal type:")
    print("1. Manual BFS")
    print("2. Manual DFS")
    print("3. Automatic BFS")
    print("4. Automatic DFS")

    try:
        traverse_selection = select()
    except ValueError:
        print("Please enter a number between 1 and 4.")
        return

    clear_screen()
    if traverse_selection == 1:
        bfs_manual(selected_movie)
    elif traverse_selection == 2:
        dfs_manual(adj_matrix, selected_movie, {})
    elif traverse_selection == 3:
        bfs_auto(selected_movie)
    elif traverse_selection == 4:
        dfs_auto(adj_matrix, selected_movie, {})
    else:
        print("Please try again")
        return


# run
if __name__ == "__main__":
    clear_screen()
    sorted_adj_matrix = dict(sorted(adj_matrix.items()))
    print("Matrix representation for the graph:")
    for movie in movies:
        print(adj_matrix[movie], movie)

    Continue = input("Continue? (Y/n) > ")
    if Continue.lower() == 'y':
        movie_list(adj_matrix)
    else:
        clear_screen()
        exit()
