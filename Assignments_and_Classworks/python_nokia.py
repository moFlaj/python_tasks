menu_page = True

while menu_page:
	menu = """
1. PhoneBook
2. Messages
3. Chat
4. Call Register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM Services
"""
	phone_book = True
	message_dir = True
	chat = True
	call_register = True
	tones = True
	settings = True
	reminders = True
	games = True
	call_divert = True
	clock = True
	sim_services = True
	profiles = True
	
	print(menu)
	user_input = input('')
	match user_input:
		case "0": 
			menu_page = False
		case "1": 
			while(phone_book):
				phone_book_dir = """
1. Search
2. Service Numbers
3. Add Name
4. Erase
5. Edit
6. Assign tone
7. Send b'card
8. Options
9. Speed dials
10. Voice tags
"""

				print(phone_book_dir)
				service_nos = True
				search = True
				add_name = True
				erase = True
				assign_tone = True
				edit = True
				b_card = True
				options = True
				speed_dials = True
				voice_tags = True
				print('Enter 0 to return') 
				user_input = input('')
				match user_input:
					case "0": 
						phone_book = False

					case "1": 
						while(search):
							print('Search')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									search = False
									
								case "01": 
									search = False
									phone_book = False
									
								case _: print("Invalid directory")
	
					case "2": 
						while(service_nos):
							print('Service Nos')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									service_nos = False
									
								case "01": 
									service_nos = False
									phone_book = False
									
								case _: print("Invalid directory")
					case "3": 
						while(add_name):
							print('Add Name')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									add_name = False
									
								case "01": 
									add_name = False
									phone_book = False
									
								case _: print("Invalid directory")
					case "4": 
						while(erase):
							print('Erase')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									erase = False
									
								case "01": 
									erase = False
									phone_book = False
									
								case _: print("Invalid directory")
	
					case "5": 
						while(edit):
							print('Edit')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									edit = False
									
								case "01": 
									edit = False
									phone_book = False
									
								case _: print("Invalid directory")

					case "6": 
						while(assign_tone):
							print('Edit')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									assign_tone = False
									
								case "01": 
									assign_tone = False
									phone_book = False
									
								case _: print("Invalid directory")

					case "7": 
						while(b_card):
							print('Edit')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									b_card = False
									
								case "01": 
									b_card = False
									phone_book = False
									
								case _: print("Invalid directory")

					case "8":
						while(options):
							op_tions = """
1. Type of view
2. Memory status
"""
							print(op_tions)
							print('Enter 0 to return or 01 to return to menu')
							type_of_view = True
							memory_status = True
							user_input = input('')
							match user_input:
								case "0":
									options = False
								case "01":
									options = False 
									phone_book = False
								case "1":
									while(type_of_view):
										print('Type of view')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												type_of_view = False
									
											case "01": 
												type_of_view = False
												options = False
												phone_book = False
									
											case _: print("Invalid directory")	
								case "2":
									while(memory_status):
										print('Memory status')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												memory_status = False
									
											case "01": 
												memory_status = False
												options = False
												phone_book = False
									
											case _: 
												print("Invalid directory")	
								case _: 
									print("Invalid directory")	

					case "9":
						while(speed_dials):
							print('Speed dials')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									speed_dials = False
									
								case "01": 
									speed_dials = False
									phone_book = False
									
								case _: 
									print("Invalid directory")	
					case "10":
						while(voice_tags):
							print('Voice tags')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									voice_tags = False
									
								case "01": 
									voice_tags = False
									phone_book = False
									
								case _: 
									print("Invalid directory")							
						
					case _: 
						print('Invalid directory')


		case "2":
			while(message_dir):
				messages = """
1. Write Messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info Service
9. Voice mailbox number
10. Service command editor
"""
				write_messages = True
				inbox = True
				outbox = True
				pic_messages = True
				templates = True
				smileys = True
				message_settings = True
				info_service = True
				command_editor = True
				voice_mailbox = True
				info_service = True
				print(messages)
				print('Enter 0 to return or 01 to return to menu')
				user_input = input('')
				match user_input:
					case "0": 
						message_dir = False
					case "1": 
						while(write_messages):
							print('Write messages')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									write_messages = False
									
								case "01": 
									write_messages = False
									message_dir = False

								case "00":
									inbox = False
									message_dir = False
									menu_page = False
									
								case _: print("Invalid directory")
					case "2":
						while(inbox):
							print('Inbox')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									inbox = False
									
								case "01": 
									inbox = False
									message_dir = False
									
								case "00":
									inbox = False
									message_dir = False
									menu_page = False
									
								case _: print("Invalid directory")
					
					case "3":
						while(outbox):
							print('Outbox')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									outbox = False
									
								case "01": 
									outbox = False
									message_dir = False
									
								case "00":
									outbox = False
									message_dir = False
									menu_page = False
									
								case _: print("Invalid directory")
			
					
					case "4":
						while(pic_messages):
							print('Picture messages')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									pic_messages = False
									
								case "01": 
									pic_messages = False
									message_dir = False
									
								case "00":
									pic_messages = False
									message_dir = False
									menu_page = False
									
								case _: print("Invalid directory")

					case "5":
						while(templates):
							print('Templates')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									templates = False
									
								case "01": 
									templates = False
									message_dir = False
									
								case "00":
									templates = False
									message_dir = False
									menu_page = False
									
								case _: print("Invalid directory")
		
					case "6":
						while(smileys):
							print('Smileys')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									smileys = False
									
								case "01": 
									smileys = False
									message_dir = False
									
								case "00":
									smileys = False
									message_dir = False
									menu_page = False
									
								case _: print("Invalid directory")

					case "7":
						while(message_settings):
							message_set = """
1. Set
2. Common
"""
							print(message_set)
							print('Enter 0 to return or 01 to return to menu')
							set = True
							common_dir = True
							user_input = input('')
							match user_input:
								case "0": 
									message_settings = False
								case "1": 
									while(set):
										set_list = """
1. Message centre number
2. Messages sent as
3. Message validity
"""
										validity = True
										centre_number = True
										sent_as = True
										print(set_list)
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												set = False
											case "01":
												set = False 
												message_settings = False
												message_dir = False
											case "1":
												while(centre_number):
													print('Message centre number')
													print('Enter 0 to return to last page or 01 to return to menu')
													user_input = input('')
													match user_input:
														case "0": 
															centre_number = False
												
														case "01":
															centre_number = False
															set = False
															message_settings = False
															message_dir = False
											case "2":
												while(sent_as):
													print('Message sent as')
													print('Enter 0 to return to last page or 01 to return to menu')
													user_input = input('')
													match user_input:
														case "0": 
															sent_as = False
									
														case "01":
															sent_as = False
															set = False
															message_settings = False
															message_dir = False
											case "3":
												while(validity):
													print('Message validity')
													print('Enter 0 to return to last page or 01 to return to menu')
													user_input = input('')
													match user_input:
														case "0": 
															validity = False
												
														case "01":
															validity = False
															set = False
															message_settings = False
															message_dir = False

											case _: 
												print("Invalid directory")
								case "2":
									while(common_dir):
										common = """
1. Delivery reports
2. Reply via same centre
3. Character support
"""
										print(common)
										print('Enter 0 to return or 01 to return to menu')
										reply_same_centre = True
										delivery_report = True
										support = True
										user_input = input('')
										match user_input:
											case "0": 
												common_dir = False
											case "01":
												common_dir = False 
												message_settings = False
												message_dir = False
											case "1":
												while(delivery_report):
													print('Delivery Reports')
													print('Enter 0 to return to last page or 01 to return to menu')
													user_input = input('')
													match user_input:
														case "0": 
															delivery_report = False
												
														case "01":
															delivery_report = False
															common_dir = False
															message_settings = False
															message_dir = False
											case "2":
												while(reply_same_centre):
													print('Reply via same centre')
													print('Enter 0 to return to last page or 01 to return to menu')
													user_input = input('')
													match user_input:
														case "0": 
															reply_same_centre = False
									
														case "01":
															reply_same_centre = False
															common_dir = False
															message_settings = False
															message_dir = False
											case "3":
												while(support):
													print('Character support')
													print('Enter 0 to return to last page or 01 to return to menu')
													user_input = input('')
													match user_input:
														case "0": 
															support = False
												
														case "01":
															support = False
															common_dir = False
															message_settings = False
															message_dir = False

											case _: 
												print("Invalid directory")
								case _:
									print("Invalid directory")

					case "8": 
						while(info_service):
							print('Info service')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									info_service = False
									
								case "01": 
									info_service = False
									message_dir = False
									
								case _: print("Invalid directory")

					case "9": 
						while(voice_mailbox):
							print('Voice mailbox number')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									voice_mailbox = False
									
								case "01": 
									voice_mailbox = False
									message_dir = False
									
								case _: print("Invalid directory")

					case "10": 
						while(command_editor):
							print('Service command editor')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									command_editor = False
									
								case "01": 
									command_editor = False
									message_dir = False
									
								case _: print("Invalid directory")
							

					case _:
						print("Invalid directory")
										

		case "3":
			while(chat):
				print('Chat')
				print('Enter 0 to return or 01 to end')
				user_input = input('')
				match user_input:
					case "0": 
						chat = False
									
					case "01": 
						chat = False
						menu_page = False
									
					case _: print("Invalid directory")

		case "4":
			while(call_register):
				call_register_dir = """
1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
"""
				print(call_register_dir)
				print('Enter 0 to return or 01 to end')
				missed_calls = True
				received_calls = True
				dialled_calls = True
				erase_recent = True
				call_duration = True
				show_callcosts = True
				call_cost_set = True
				prepaid_costs = True
				user_input = input('')
				match user_input:
					case "0": 
						call_register = False
									
					case "01": 
						call_register = False
						menu_page = False

					case "1":
						while missed_calls:
							print('Missed calls')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									missed_calls = False
									
								case "01": 
									missed_calls = False
									call_register = False
								case _:
									print("Invalid directory")
									
					case "2":
						while received_calls:
							print('Received calls')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									received_calls = False
									
								case "01": 
									received_calls = False
									call_register = False
								case _:
									print("Invalid directory")
					case "3":
						while dialled_calls:
							print('Received calls')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									dialled_calls = False
									
								case "01": 
									dialled_calls = False
									call_register = False
								case _:
									print("Invalid directory")
					case "4":
						while erase_recent:
							print('Erase recent call lists')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									erase_recent = False
									
								case "01": 
									erase_recent = False
									call_register = False
								case _:
									print("Invalid directory")

					case "5": 
						while call_duration:
							cull_duration_dir = """
1. Last call duration
2. All calls duration
3. Received calls duration
4. Dialled calls duration
5. Clear timers
"""
							print(cull_duration_dir)
							print('Enter 0 to return or 01 to return to menu')
							last_call = True
							all_calls = True
							received_calls_duration = True
							dialled_calls_duration = True
							clear_timers = True
							user_input = input('')
							match user_input:
								case "0": 
									call_duration = False
									
								case "01": 
									call_duration = False
									call_register = False

								case "1":
									while last_call:
										print('Last call duration')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												last_call = False
									
											case "01": 
												last_call = False
												call_duration = False
												call_register = False
											case _:	
												print("Invalid directory")

								case "2":
									while all_calls:
										print('All calls duration')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												all_calls = False
									
											case "01": 
												all_calls = False
												call_duration = False
												call_register = False
											case _:	
												print("Invalid directory")

								case "3":
									while received_calls_duration:
										print('Received calls duration')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												received_calls_duration = False
									
											case "01": 
												received_calls_duration = False
												call_duration = False
												call_register = False
											case _:	
												print("Invalid directory")
								case "4":
									while dialled_calls_duration:
										print('Dialled calls duration')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												dialled_calls_duration = False
									
											case "01": 
												dialled_calls_duration = False
												call_duration = False
												call_register = False
											case _:	
												print("Invalid directory")

								case "5":
									while clear_timers:
										print('Clear Timers')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												clear_timers = False
									
											case "01": 
												clear_timers = False
												call_duration = False
												call_register = False
											case _:	
												print("Invalid directory")

								case _:
									print("Invalid directory")

					case "6":
						while show_callcosts:
							show_call_costs = """
1. Last call cost
2. All calls costs
3. Clear counters
"""
							last_call_cost = True
							all_calls_costs = True
							clear_counters = True
							print(show_call_costs)
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									show_callcosts = False
									
								case "01": 
									show_callcosts = False
									call_register = False
								case "1":
									while last_call_cost:
										print('Last call cost')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												last_call_cost = False
									
											case "01": 
												last_call_cost = False
												show_call_costs = False
												call_register = False
											case _:	
												print("Invalid directory")
								case "2":
									while all_calls_costs:
										print('All call costs')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												all_calls_costs = False
									
											case "01": 
												all_calls_costs = False
												show_call_costs = False
												call_register = False
											case _:	
												print("Invalid directory")
								case "3":
									while clear_counters:
										print('Clear counters')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												clear_counters = False
									
											case "01": 
												clear_counters = False
												show_call_costs = False
												call_register = False
											case _:	
												print("Invalid directory")
								case _:	
									print("Invalid directory")


					case "7":
						while call_cost_set:
							call_cost_settings = """
1. Call cost limit
2. Show costs in
"""
							call_cost_limit = True
							show_cost_in = True
							print(call_cost_settings)
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									call_cost_set = False
									
								case "01": 
									call_cost_set = False
									call_register = False
								case "1":
									while call_cost_limit:
										print('Call cost limit')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												call_cost_limit = False
									
											case "01": 
												call_cost_limit = False
												call_cost_set = False
												call_register = False
											case _:	
												print("Invalid directory")
								case "2":
									while show_cost_in:
										print('Show costs in')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												show_cost_in = False
									
											case "01": 
												show_cost_in = False
												call_cost_set = False
												call_register = False
											case _:	
												print("Invalid directory")
								case _:	
									print("Invalid directory")
					case "8":
						while prepaid_costs:
							print('Prepaid costs')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									prepaid_costs = False
									
								case "01": 
									prepaid_costs = False
									call_register = False
								case _:
									print("Invalid directory")
					case _: print("Invalid directory")
		case "5":
			while(tones):
				tones_dir = """
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warning and game tones
8. Vibrating alert
9. Screen saver
"""
				print(tones_dir)
				print('Enter 0 to return or 01 to return to menu')
				ringing_tone = True
				ringing_volume = True
				incoming_alert = True
				composer = True
				message_alert_tone = True
				keypad_tones = True
				warning_game_tones = True
				vibrating_alert = True
				screen_saver = True
				user_input = input('')
				match user_input:
					case "0": 
						tones = False
									
					case "01": 
						tones = False
						menu_page = False
					case "1":
						while ringing_tone:
							print('Ringing tone')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									ringing_tone = False
									
								case "01": 
									ringing_tone = False
									tones = False
								case _:
									print("Invalid directory")
					case "2":
						while ringing_volume:
							print('Ringing volume')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									ringing_volume = False
									
								case "01": 
									ringing_volume = False
									tones = False
								case _:
									print("Invalid directory")
					case "3":
						while incoming_alert:
							print('Incoming call alert')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									incoming_alert = False
									
								case "01": 
									incoming_alert = False
									tones = False
								case _:
									print("Invalid directory")
					case "4":
						while composer:
							print('Composer')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									composer = False
									
								case "01": 
									composer = False
									tones = False
								case _:
									print("Invalid directory")
					case "5":
						while message_alert_tone:
							print('Message alert tone')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									message_alert_tone = False
									
								case "01": 
									message_alert_tone = False
									tones = False
								case _:
									print("Invalid directory")
					case "6":
						while keypad_tones:
							print('Keypad tones')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									keypad_tones = False
									
								case "01": 
									keypad_tones = False
									tones = False
								case _:
									print("Invalid directory")
					case "7":
						while warning_game_tones:
							print('Warning and game tones')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									warning_game_tones = False
									
								case "01": 
									warning_game_tones = False
									tones = False
								case _:
									print("Invalid directory")
					case "8":
						while vibrating_alert:
							print('Vibrating alert')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									vibrating_alert = False
									
								case "01": 
									vibrating_alert = False
									tones = False
								case _:
									print("Invalid directory")
					case "9":
						while screen_saver:
							print('Screen saver')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									screen_saver = False
									
								case "01": 
									screen_saver = False
									tones = False
								case _:
									print("Invalid directory")
					case _:	
						print("Invalid directory")
		case "6":
			while settings:
				setting = """
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
"""
				print(setting)
				print('Enter 0 to return')
				phone_set = True
				call_settings = True
				security_set = True
				factory_settings = True
				user_input = input('')
				match user_input:
					case "0": 
						settings = False
					case "1":
						while call_settings:
							call_settings_dir = """
1. Automatic redial
2. Speed dialing
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic answer
"""
							print(call_settings_dir)
							print('Enter 0 to return or 01 to return to menu')
							auto_redial = True
							speed_dialing = True
							call_waiting_options = True
							own_number_sending = True
							phone_line_in_use = True
							automatic_answer = True
							user_input = input('')
							match user_input:
								case "0": 
									call_settings = False
									
								case "01": 
									call_settings = False
									settings = False
								case "1":
									while auto_redial:
										print('Automatic redial')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												auto_redial = False
									
											case "01": 
												auto_redial = False
												call_settings = False
												settings = False
											case _:
												print("Invalid directory")
								case "2":
									while speed_dialing:
										print('Speed dialing')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												speed_dialing = False
									
											case "01": 
												speed_dialing = False
												call_settings = False
												settings = False
											case _:
												print("Invalid directory")
								case "3":
									while call_waiting_options:
										print('Call waiting options')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												call_waiting_options = False
									
											case "01": 
												call_waiting_options = False
												call_settings = False
												settings = False
											case _:
												print("Invalid directory")
								case "4":
									while own_number_sending:
										print('Own number sending')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												own_number_sending = False
									
											case "01": 
												own_number_sending = False
												call_settings = False
												settings = False
											case _:
												print("Invalid directory")
								case "5":
									while phone_line_in_use:
										print('Phone line in use')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												phone_line_in_use = False
									
											case "01": 
												phone_line_in_use = False
												call_settings = False
												settings = False
											case _:
												print("Invalid directory")
								case "6":
									while automatic_answer:
										print('Automatic answer')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												automatic_answer = False
									
											case "01": 
												automatic_answer = False
												call_settings = False
												settings = False
											case _:
												print("Invalid directory")
								case _:
									print("Invalid directory")

					case "2":
						while phone_set:
							phone_settings = """
1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Lights
6. Confirm SIM service actions
"""
							print(phone_settings)
							print('Enter 0 to return or 01 to return to menu')
							lang = True
							cell_info_display = True
							welcome_note = True
							network_select = True
							lights = True
							cofirm_sim = True
							user_input = input('')
							match user_input:
								case "0": 
									phone_set = False
									
								case "01": 
									phone_set = False
									settings = False
								case "1":
									while lang:
										print('Language')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												lang = False
									
											case "01": 
												lang = False
												phone_set = False
												settings = False
											case _:
												print("Invalid directory")
								case "2":
									while cell_info_display:
										print('Cell info display')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												cell_info_display = False
									
											case "01": 
												cell_info_display = False
												phone_set = False
												settings = False
											case _:
												print("Invalid directory")
								case "3":
									while welcome_note:
										print('Welcome note')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												welcome_note = False
									
											case "01": 
												welcome_note = False
												phone_set = False
												settings = False
											case _:
												print("Invalid directory")
								case "4":
									while network_select:
										print('Network selection')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												network_select = False
									
											case "01": 
												network_select = False
												phone_set = False
												settings = False
											case _:
												print("Invalid directory")
								case "5":
									while lights:
										print('Lights')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												lights = False
									
											case "01": 
												lights = False
												phone_set = False
												settings = False
											case _:
												print("Invalid directory")
								case "6":
									while cofirm_sim:
										print('Confirm SIM service actions')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												cofirm_sim = False
									
											case "01": 
												cofirm_sim = False
												phone_set = False
												settings = False
											case _:
												print("Invalid directory")
								case _:
									print("Invalid directory")

					case "3": 
						while security_set:
							security_settings = """
1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Phone security
6. Change access codes
"""
							print(security_settings)
							print('Enter 0 to return or 01 to return to menu')
							pin_code = True
							call_barring = True
							fixed_dialling = True
							closed_user_group = True
							phone_security = True
							access_codes = True
							user_input = input('')
							match user_input:
								case "0": 
									security_set = False
									
								case "01": 
									security_set = False
									settings = False
								case "1":
									while pin_code:
										print('PIN code request')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												pin_code = False
									
											case "01": 
												pin_code = False
												security_set = False
												settings = False
											case _:
												print("Invalid directory")
								case "2":
									while call_barring:
										print('Call barring service')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												call_barring = False
									
											case "01": 
												call_barring = False
												security_set = False
												settings = False
											case _:
												print("Invalid directory")
								case "3":
									while fixed_dialling:
										print('Fixed dialling')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												fixed_dialling = False
									
											case "01": 
												fixed_dialling = False
												security_set = False
												settings = False
											case _:
												print("Invalid directory")
								case "4":
									while closed_user_group:
										print('Closed user group')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												closed_user_group = False
									
											case "01": 
												closed_user_group = False
												security_set = False
												settings = False
											case _:
												print("Invalid directory")
								case "5":
									while phone_security:
										print('Phone security')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												phone_security = False
									
											case "01": 
												phone_security = False
												security_set = False
												settings = False
											case _:
												print("Invalid directory")
								case "6":
									while access_codes:
										print('Change access codes')
										print('Enter 0 to return or 01 to return to menu')
										user_input = input('')
										match user_input:
											case "0": 
												access_codes = False
										
											case "01": 
												access_codes = False
												security_set = False
												settings = False
											case _:
												print("Invalid directory")
								case _:
									print("Invalid directory")
					case "4":
						while factory_settings:
							print('Restore factory settings')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									factory_settings = False
									
								case "01": 
									factory_settings = False
									settings = False
								case _:
									print("Invalid directory")
	
					case _:
						print("Invalid directory")
		case "7":
			while call_divert:
				print('Call divert')
				print('Enter 0 to return to menu')
				user_input = input('')
				match user_input:
					case "0": 
						call_divert = False
					case _:
						print("Invalid directory")
		case "8":
			while games:
				print('Games')
				print('Enter 0 to return to menu')
				user_input = input('')
				match user_input:
					case "0": 
						games = False
					case _:
						print("Invalid directory")
		case "10":
			while reminders:
				print('Reminders')
				print('Enter 0 to return to menu')
				user_input = input('')
				match user_input:
					case "0": 
						reminders = False
					case _:
						print("Invalid directory")
		case "11":
			while clock:
				clock_dir = """
1. Alarm clock
2. Clock settings
3. Date settings
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
"""
				print(clock_dir)
				print('Enter 0 to return to menu')
				alarm_clock = False
				clock_settings = True
				date_settings = True
				stopwatch = True
				countdown_timer = True
				auto_update_date_time = True
				user_input = input('')
				match user_input:
					case "0": 
						clock = False
					case "1":
						while access_codes:
							print('Alarm clock')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									alarm_clock = False
										
								case "01": 
									alarm_clock = False
									clock_dir = False
								case _:
									print("Invalid directory")
					case "2":
						while clock_settings:
							print('Clock settings')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									clock_settings = False
										
								case "01": 
									clock_settings = False
									clock_dir = False
								case _:
									print("Invalid directory")
					case "3":
						while date_settings:
							print('Date settings')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									date_settings = False
										
								case "01": 
									date_settings = False
									clock_dir = False
								case _:
									print("Invalid directory")
					case "4":
						while stopwatch:
							print('Stopwatch')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									stopwatch = False
										
								case "01": 
									stopwatch = False
									clock_dir = False
								case _:
									print("Invalid directory")
					case "5":
						while countdown_timer:
							print('Countddown timer')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									countdown_timer = False
										
								case "01": 
									countdown_timer = False
									clock_dir = False
								case _:
									print("Invalid directory")
					case "6":
						while auto_update_date_time:
							print('Auto update of date and time')
							print('Enter 0 to return or 01 to return to menu')
							user_input = input('')
							match user_input:
								case "0": 
									auto_update_date_time = False
										
								case "01": 
									auto_update_date_time = False
									clock_dir = False
								case _:
									print("Invalid directory")
						
					case _:
						print("Invalid directory")
		case "12":
			while profiles:
				print('Profiles')
				print('Enter 0 to return to menu')
				user_input = input('')
				match user_input:
					case "0": 
						profiles = False
					case _:
						print("Invalid directory")
		case "13":
			while sim_services:
				print('SIM services')
				print('Enter 0 to return to menu')
				user_input = input('')
				match user_input:
					case "0": 
						sim_services = False
					case _:
						print("Invalid directory")
		case _: 
			print('Invalid directory')
			continue
				