class Film:
    def __init__(self , title , year , producer , actor , link):
        self.title = title
        self.year = year
        self.producer = producer
        self.actor = actor
        self.link = link

avengers = Film("avengers endgame", 2019, "Marvel", "Robert Downey JR","https://altadefinizione.cloud/avengers-endgame-2019-streaming-4k/" )
it_2 = Film("it capitolo 2", 2019, "warner bros", "Bill Skarsgard", "https://altadefinizione.cloud/it-capitolo-2-streaming-hd/")    
top_gun = Film("top gun", 1986, "paramount pictures", "Tom Cruise","https://altadefinizione.cloud/top-gun/")
fast_and_furious = Film("fast and furious", 2001, "universal pictures", "ciao", "https://altadefinizione.cloud/fast-furious-streaming-4k/")

film = [avengers, it_2, top_gun, fast_and_furious]