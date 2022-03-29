
InfoDb = []
#List out 4 data appends for info db
InfoDb.append({  
               "FirstName": "Pierre",  
               "LastName": "Aubamyang",  
               "country": "gabon",  
               "position": "Striker",  
               "club": "Barcelona",  
               "Past clubs":["Nice","Lyon", "Dortmund","Arsenal"]  
              })  

InfoDb.append({  
              "FirstName": "Cristiano",  
               "LastName": "Ronaldo",  
               "country": "Portugal",  
               "position": "Striker",  
               "club": "Juventus",  
               "Past clubs":["Sporting lisbon","Man U", "Real Madrid","Juventus"]
              })  
InfoDb.append({  
               "FirstName": "Leo",  
               "LastName": "Messi",  
               "country": "Argentina",  
               "position": "Right Wing",  
               "club": "PSG",  
               "Past clubs":["Barca" ,"PSG"]
              })  
InfoDb.append({  
               "FirstName": "Neymar",  
               "LastName": "Dos Sontas silva",  
               "country": "brazil",  
               "position": "Left Wing",  
               "club": "PSG",  
               "Past clubs":["Santos","Barca" ,"PSG",]
              })  
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"]) 
    print("\t", "Clubs: ", end="")   
    print(", ".join(InfoDb[n]["Past clubs"]))  
    print()

def looop():
    for n in range(len(InfoDb)):
        print_data(n)
looop()
print()   

def whilelooop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
whilelooop(0)

def recursive(n):
    if n < len(InfoDb):
        print_data(n)
        recursive(n + 1)
    return # exit condition

   
print()
print()
recursive(0)

