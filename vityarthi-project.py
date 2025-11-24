# -------------------------------------------------------------
#           CINEMA TICKET BOOKING SYSTEM  (Student Version)
# -------------------------------------------------------------

# Movie list with prices (just made simple)
movies = {
    1: ("Avengers: Endgame", 180),
    2: ("KGF Chapter 2", 200),
    3: ("Leo", 150),
    4: ("Joker", 170)
}

print("\n   🎬 Welcome to Cinema Ticket Booking System\n")

# showing movie list
print("Movies Available:\n")
for num, info in movies.items():
    print(num, ".", info[0], " - Rs.", info[1])

# asking user for movie
choice = int(input("\nEnter the movie number: "))

# checking if valid
if choice not in movies:
    print("Oops! Wrong movie number. Try again.")
    exit()

movie_name, base_price = movies[choice]

print("\nYou selected:", movie_name)
print("Ticket Price: Rs.", base_price)

# number of tickets
tickets = int(input("\nHow many tickets do you need? "))

# seat types
print("\nSeat Types:")
print("1. Normal   (no extra)")
print("2. Premium  (+50)")
print("3. Recliner (+120)\n")

seat = int(input("Choose seat type: "))

# deciding extra amount
if seat == 1:
    extra = 0
elif seat == 2:
    extra = 50
elif seat == 3:
    extra = 120
else:
    print("Invalid seat choice!")
    exit()

# calculating total
total = (base_price + extra) * tickets

# final summary
print("\n---------------- BOOKING SUMMARY ----------------")
print("Movie            :", movie_name)
print("Tickets          :", tickets)
print("Seat Extra       : Rs.", extra)
print("Final Amount     : Rs.", total)
print("--------------------------------------------------")
print("\n🎉 Booking Confirmed! Enjoy your Movie! 🎥\n")
