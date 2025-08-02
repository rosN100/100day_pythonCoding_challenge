true = ["T","R","U","E"]
love = ["L","O","V","E"]
def calculate_love_score(name1,name2):
    true_score = 0
    love_score = 0
    word = (name1+name2).upper()
    for letter in word:
        if letter in true:
            true_score += 1
        if letter in love:
            love_score += 1
    love_score = str(true_score)+ str(love_score)
    print(love_score)

calculate_love_score("Kanye West", "Kim Kardashian")