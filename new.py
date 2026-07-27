cgpa=float(input("Enter your CGPA: "))
backlog: str=input("Do you have any backlogs? (True/False): ").lower()== "true"
if  cgpa>=8.5 and not backlog:
    print("You are eligible for the interview")
else:
    print("You are not eligible for the interview")