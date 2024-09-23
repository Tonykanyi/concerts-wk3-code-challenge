from band import Band
from venue import Venue
from concert import Concert



def program():
    Band.drop_table()
    Venue.drop_table()
    Concert.drop_table()

    Band.create_table()
    Venue.create_table()
    Concert.create_table()
    
    sautiSol=Band("Chelsea","london")
    sautiSol.save()
    manchester_reds=Band.create("Man Utd","manchester")
    
    nyayo_stadium=Venue.create("Nyayo stadium","Nairobi")
    kasarani=Venue.create("KASARANI STADIUM","KASARANI")
    
    sato_concert=Concert("23-12-2023",sautiSol,kasarani)
    sato_concert.save()
    
    sunday_concert=Concert.create("24-12-2023",manchester_reds,nyayo_stadium)
    
  
    print(sautiSol.concerts())
    #
    
    
    print(sunday_concert.hometown_show())
    print(sato_concert.introduction())
    sautiSol.play_in_venue("KIBAKI STADIUM","23-06-2024")
   
    print(sautiSol.concerts())
    print(sautiSol.venues())
    print(sautiSol.all_introductions())
    
    print(Band.most_performances())
program()
