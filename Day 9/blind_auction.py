logo = r'''
        -----------------
       /                 \
     )/                   (\
     |"""""""""""""""""""|
     |                   |
     |                   |
     |                   |
     |"""""""""""""""""""|
     )/                   (\
    /_______________________\
   / .-------------------. \
  / /                     \ \
 / /                       \ \
 \ \                       / /
  \ \_____________________/ /
   \_______________________/
           .       .       .
'''
print(logo)
print("------------------------------------------------------------------------------------------------")
auction_bids ={}
show_questions = True
def highest_bid():
    highest =''
    value = 0
    for bid in auction_bids:
        if auction_bids[bid] > value:
            highest = bid
    print(f"The winner is {highest} with a bid of ${auction_bids[highest]}")

while show_questions:
    print("welcome to the secret auction program.")
    name = input("what is your name?\n")
    bid = int(input("what's your bid?:\n$"))
    auction_bids[name]= bid
    state = input("Are there any other bidders? Type 'yes' or 'no'\n")
    print("\n"*100)
    if state == "no":
        show_questions = False
        highest_bid()

