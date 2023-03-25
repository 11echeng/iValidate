from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'iValidate API'

@app.route('/api/getData')
def get_data():
    data = [
    {
        "id": 0,
        "text": "To create our annual MLB Rank list of the top 100 players in the sport, we presented a panel of ESPN baseball experts with pairings upon pairings of the biggest names in the game and asked one simple question: Which player will be better in 2023?",
        "topic": "Sports"
    },
    {
        "id": 1,
        "text": "Brandon Fraser is such a underrated actor Hollywood definitely did him dirty along the way I'm glad he's found himself and we're going to be able to see him acting in movies for a long time to come",
        "topic": "Film"
    },
    {
        "id": 2,
        "text": "If Bom ever releases her own solo album, I hope she'll do a slow r&b track like this where it really shows how smooth her voice sounds when she doesn't have to hit such high notes.",
        "topic": "Music"
    },
    {
        "id": 3,
        "text": "Looks amazing my guy, your channel is gonna launch big soon and im gonna be here all for it.",
        "topic": "Film"
    },
    {
        "id": 4,
        "text": "He is only 23 years old, hit 56 homeruns in the NPB last season, with the triple crown. Glad he was able to come up clutch and show his offensive prowess after having such a difficult tournament. Go SAMURAIS.",
        "topic": "Sports"
    },
    {
        "id": 5,
        "text": "I gotta Give Tim legler his flowers this man is really my favorite espn analyst and should've had his own show because he talks hoops he doesn't dive into players personal lives he just talks hoops and he understands the game.",
        "topic": "Sports"
    },
    {
        "id": 6,
        "text": "I love how highly he speaks of the kids in his show. Like he's proud of all of them so much and is going to take a break from comedy to become a drama teacher",
        "topic": "Film"
    },
    {
        "id": 7,
        "text": "finally this comicbook was one of my favorites as a teen I can't wait to see its message spread out with these great actors and crew behind it all.",
        "topic": "Film"
    },
    {
        "id": 8,
        "text": "I do like the concept of them being actual teenagers when they’re usually depicted as young adults. You gotta love the Spider-Verse inspired animation style too. I won’t have too high of expectations but I’m definitely looking forward to this movie; I can’t imagine it being worse than Turtles In Time and the two Michael Bay movies.",
        "topic": "Film"
    },
    {
        "id": 9,
        "text": "this is hands down one of the hardest beats of the past 10 years",
        "topic": "Music"
    },
    {
        "id": 10,
        "text": "I cant wait until everyone realizes how talented Giveon is. I'm tired of people sleeping on him! (Which is my opinion, since it seems a lot of people has a problem with what I said)",
        "topic": "Music"
    },
    {
        "id": 11,
        "text": "Great to see volpe mash another one, geez that sounded good off the bat. Cole looked great too.",
        "topic": "Sports"
    },
    {
        "id": 12,
        "text": "I was obsessed with this song back in middle school, I learned the choreography and the lyrics, this song and mv brings back so many memories.",
        "topic": "Music"
    },
    {
        "id": 13,
        "text": "Many ppl will not understand the value of I paved the way for everyone that is pavin' the way,but only Tablo can give recognition to everything that the 2nd gen did without underestimating what new gens do.",
        "topic": "Music"
    },
    {
        "id": 14,
        "text": "This series deserves a lot more attention. It's really good, one of the best suspense/mistery/horror series I've seen in quite a while.",
        "topic": "Film"
    },
    {
        "id": 15,
        "text": "I want an honest economy that reflects peoples situations rather than just the wealthiest groups. I want this to burst already so it can be done with.",
        "topic": "Film"
    },
    {
        "id": 16,
        "text": "The stock market is so irrational that it keeps moving up. Market manipulation by the plunge protection team at its best.",
        "topic": "Film"
    },
    {
        "id": 17,
        "text": "Haven’t seen yet but know Colin not gonna give Westbrook credit",
        "topic": "Sports"
    },
    {
        "id": 18,
        "text": "If they do meet in the first round, it'll be a really tough series, especially if the Knicks defense shows up. It could go 6 or 7 games",
        "topic": "Sports"
    },
    {
        "id": 19,
        "text": "My man Hasan, you have joined the legends in my eyes. Steve Colbert, John Oliver, and Trevor Noah need to make a seat at the head of the table.",
        "topic": "Film"
    },
    {
        "id": 20,
        "text": "As a business major, I've always thought they predatory pricing is just the way companies do business... I just realized how evil my profession is.",
        "topic": "Film"
    }
]
    print("getData API endpoint")
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

