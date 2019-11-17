import room, item, character, curses

my_screen = curses.initscr()

def print_room(in_room, input_player):
	for (i, j) in in_room.coord_dict:
		my_screen.addstr(i, j*2, repr(in_room.coord_dict[(i, j)].has))
	my_screen.addstr(input_player.location[0], input_player.location[1] * 2, repr(input_player))

hero_player = character.Player()
main_room = room.Room([hero_player], 10, 10)

my_screen.keypad(True)

game_over = False
while game_over == False:
	my_screen.clear()
	print_room(main_room, hero_player)
	my_screen.addstr(14, 0, 'Push \'up\' or \'q\'')
	my_screen.addstr(15, 0, main_room.coord_dict[hero_player.location].announce()) # print what is at the player's location
	inkey = my_screen.getkey()
	if inkey == 'KEY_UP':
		new_loc = (hero_player.location[0] - 1, hero_player.location[1])
		hero_player.location = new_loc
	elif inkey == 'q':
		game_over = True	

curses.endwin()





 
