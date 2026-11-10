# --- Steps 1-2: the Album class ---
# define a class called Album
class Album:
    # constructor takes album_name, album_artist, number_of_songs
    # and stores each one as an instance variable
    def __init__(self, album_name, album_artist, number_of_songs):
        self.album_name = album_name
        self.album_artist = album_artist
        self.number_of_songs = number_of_songs

    # __str__: return the text (album_name, album_artist, number_of_songs)
    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"

    # __repr__: return the same text as __str__, so printed lists look right
    def __repr__(self):
        return self.__str__()


# --- Helper functions for sorting ---
# get_songs(album): return the album's number_of_songs
def get_songs(album):
    return album.number_of_songs


# get_name(album): return the album's album_name
def get_name(album):
    return album.album_name


# --- Step 3: albums1 ---
# make a list called albums1 holding five Album objects
albums1 = [
    Album("Vibes These Days", "Abuti", 12),
    Album("Home Coming", "BLXCK FVTHR", 8),
    Album("3AM", "KELO", 15),
    Album("SMD", "AWE", 10),
    Album("I AM", "MYY", 6),
]
# print albums1
print(albums1)

# --- Step 4: sort by songs ---
# sort albums1 using get_songs as the key (smallest to largest)
albums1.sort(key=get_songs)
# print albums1
print(albums1)

# --- Step 5: swap ---
# swap the album at index 0 with the album at index 1
albums1[0], albums1[1] = albums1[1], albums1[0]
# print albums1
print(albums1)

# --- Steps 6-7: albums2 ---
# make a list called albums2 holding five Album objects
albums2 = [
    Album("Album Six", "Artist F", 11),
    Album("Album Seven", "Artist G", 14),
    Album("Album Eight", "Artist H", 9),
    Album("Album Nine", "Artist I", 13),
    Album("Album Ten", "Artist J", 7),
]
# print albums2
print(albums2)

# --- Step 8: copy ---
# for every album in albums1:
for album in albums1:
    # add it to albums2
    albums2.append(album)

# --- Step 9: add two more ---
# add (Dark Side of the Moon, Pink Floyd, 9) to albums2
albums2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
# add (Oops!... I Did It Again, Britney Spears, 16) to albums2
albums2.append(Album("Oops!... I Did It Again", "Britney Spears", 16))

# --- Step 10: sort by name ---
# sort albums2 using get_name as the key (A to Z)
albums2.sort(key=get_name)
# print albums2
print(albums2)

# --- Step 11: search ---
# set found_index to None (nothing found yet)
found_index = None
# for every position in albums2:
for index in range(len(albums2)):
    # if the album's name is "Dark Side of the Moon":
    if albums2[index].album_name == "Dark Side of the Moon":
        # save the position in found_index and stop looping
        found_index = index
        break

# if found_index is not None, print the index; otherwise say it was not found
if found_index is not None:
    print(f"Dark Side of the Moon is at index {found_index} in albums2.")
else:
    print("Dark Side of the Moon was not found in albums2.")