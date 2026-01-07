print("-----------Welcome-----------")
while True:
    player_id = input("Enter Player ID: ")
    if player_id == "":
        print("invalid player id ")
    else:
        break 

while True:
    try:    
        games = int(input("Enter the numbers of games played: "))
        if 5 <= games <= 10:
            break
        else:
            print("games played must be between 5 and 10")
    except(ValueError):
        print("Enter a valid number")
        
scores = []
times = []

for game_num in range(1, games + 1 ) : # for loops start and 1 and + 1 help protect the users input cus for loop bstops before the number
    while True:
        try:
            score = int(input(f"Enter the score for game {game_num}: "))
            scores.append(score)
            break
        except(ValueError):
            print("Invalid input")
            
    while True: 
        try:
            time_taken = int(input(f"Enter the time taken for game {game_num}: "))
            times.append(time_taken)
            break
        except(ValueError):
            print("Invalid input")
            
highest_score = max(scores)
average_time = sum(times) / len(times)

print(F"Player ID: {player_id}")
print(F"Highest score is {highest_score}")
print(F"Average time_taken spent playing: {average_time}")


with open("player_stat.txt", "x" ) as file:
    file.write(f"Player ID; {player_id}")
    file.write(f"\n Games played: {games}")
    file.write("\n Scores")
    for s in scores:
        file.write(f"\n {s}")
    file.write("\n Times (minutes)")
    for t in times:
        file.write(F"\n {t}")
    file.write(F"\nHighest score is {highest_score}")
    file.write(F"\nAverage time_taken spent playing: {average_time}")
    file.write("\n-------------------------------------------------")