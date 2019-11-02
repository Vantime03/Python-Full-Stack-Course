import room, item, character

hero_player = character.Player()
main_room = room.Room([hero_player], 10, 10)



keep_playing = True
while keep_playing:
	print(main_room.__repr__())
	inkey = input("Next command: ")
	if inkey[0] in ['w', 'W']:
		new_loc = (hero_player.location[0] - 1, hero_player.location[1])
		hero_player.location = new_loc
	elif inkey[0] in ['e', 'E']:
		new_loc = (hero_player.location[0] + 1, hero_player.location[1])
		hero_player.location = new_loc
	elif inkey[0] in ['n', 'N']:
		new_loc = (hero_player.location[0], hero_player.location[1] + 1)
		hero_player.location = new_loc
	elif inkey[0] in ['s', 'S']:
		new_loc = (hero_player.location[0], hero_player.location[1] - 1)
		hero_player.location = new_loc
	elif inkey[0] in ['q', 'Q']:
		keep_playing = False

	





 
