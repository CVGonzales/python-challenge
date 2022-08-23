import os
import csv


os.chdir(os.path.dirname(__file__))

election_csv = os.path.join("Resources", "election_data.csv")

votes = []
candidate = []


with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for column in csv_reader:
        votes.append(column[0])
        candidate.append(column[2])

    total_votes = (len(votes))
    print("Election Results")
    print("-----------------------------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------------------------")

    Stockham = int(candidate.count("Charles Casper Stockham"))
    DeGette = int(candidate.count("Diana DeGette"))
    Doane = int(candidate.count("Raymon Anthony Doane"))
    Stockham_percent = round((Stockham/total_votes) * 100, 3)
    DeGette_percent = round((DeGette/total_votes) * 100, 3)
    Doane_percent = round((Doane/total_votes) * 100, 3)

    print(f"Charles Casper Stockham: {Stockham_percent}% ({Stockham})")
    print(f"Diana DeGette: {DeGette_percent}% ({DeGette})")
    print(f"Raymon Anthony Doane: {Doane_percent}% ({Doane})")
    print("-----------------------------------------")

    if Stockham > DeGette > Doane:
        Winner = "Charles Casper Stockham"
    elif DeGette > Stockham > Doane:
        Winner = "Diana DeGette"
    elif Doane > Stockham > DeGette:
        Winner = "Raymon Anthony Doane"

    print(f"Winner: {Winner}")
    print("-----------------------------------------")

output_path = os.path.join("analysis", "electionresults.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results" + "\n")
    txtfile.write("-----------------------------------------" + "\n")
    txtfile.write(f"Total Votes: {total_votes}" + "\n")
    txtfile.write("-----------------------------------------" + "\n")
    txtfile.write(f"Charles Casper Stockham: {Stockham_percent}% ({Stockham})" + "\n")
    txtfile.write(f"Diana DeGette: {DeGette_percent}% ({DeGette})" + "\n")
    txtfile.write(f"Raymon Anthony Doane: {Doane_percent}% ({Doane})" + "\n")
    txtfile.write("-----------------------------------------" + "\n")
    txtfile.write(f"Winner: {Winner}" + "\n")
    txtfile.write("-----------------------------------------" + "\n")
