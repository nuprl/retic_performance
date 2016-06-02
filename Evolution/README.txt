(typed/ directory used to be `cardplay/`)



Create the choose_feeding method and test harness & and dictate Dealer's interaction with it

Files in project:

cardplay/       : representation for step 3 card plays
  cardplay.py                 - abstract class for playing cards
  exchange_for_body_size.py   - to represent exchanging card for species body size
  exchange_for_pupulation.py  - to represent exchanging card for species population
  exchange_for_species.py     - to represent exchanging cards for species with traits
  replace_cards.py            - to represent replacing card on species
dealer/
  constants.py  - To represent dealer constants
  dealer.py     - To represent the dealer
  deck.py       - To represent a deck of cards
evo_json/         : JSON handler :
  convert_py_json/            : PyJSON converters :
    convert_choice.py         - Converts datatypes for choice harness
    convert_feeding.py        - Converts to/from PyJSON from/to Feeding
    convert_player.py         - Converts to/from PyJSON from/to ClientPlayerStatr
    convert_player_fields.py  - Handles Player field conversions to/from PyJSON
    convert_situation.py      - Converts to/from PyJSON from/to Situation
    convert_species.py        - Converts to/from PyJSON from/to Species
    convert_species_fields.py - Handles PyJSON conversion of specoes fields
    convert_step4.py          - Converts to/from PyJSON for step4 harness
    convert_trait.py          - Converts to/from PyJSON from/to TraitCard subclasses
  process_json/              : PyJSON converters:
    process_choice.py       - processes silly player harness
    process_confguration.py - processes to/from PyJSON Configuration
    process_step4.py        - processes step4 PyJSON harness
  __init__.py               - makes this folder a package
  data_def.py               - data definitions for conversions
  constants.py              - constants for conversions
evo_tests/         : tests for Evolution :
  fetch_json_tests/ - scrapes JSON tests off test-fest site
  json_configs/     - examples of JSON configuration scenarios
  json_feeding_6/   - examples of JSON feeding scenarios with full object returns
  json_feedings_7/  - examples of JSON feeding scenarios with index returns
  json_silly/       - JSON test cases for silly Player harness
  json_situations/  - examples of JSON attack situations
  json_step4/       - JSON test cases for step4
  test_cases/               : Test cases for Evolution :
    __init__.py             - makes directory a package
    test_convert_py_json.py - tests conversions to/from JSON to program data
    test_data_def.py        - tests data definitions in feeding/data_def.py
    jest_json.py            - tests all JSON interaction scripts (xfeed, xstream, etc.)
    test_player.py          - tests methods on Player
    test_processing.py      - test methods on JSON converter
    test_player_state.py    - tests methods on PlayerSate
    test_situation_flag.py  - tests for SituationFlag
    test_species.py         - tests methods for Species
    test_trait_cards.py     - tests methods on TraitCard and subclasses
  __init__.py       - makes directory a package
  all_tests.py      - runs all tests in all files starting "test_" in test_cases/
  constants.py
  test_util.py
  examples.py
evolution/
  player/ - classes and methods dealing with player
    __init__.py              -
    player_state.py          - holds player state
    player.py                - makes all player strategy decisions
    player_feeding_choice.py - holds feeding decision for a player
    species_keys.py          - keys for ordering species choices
  trait_cards/ - implementations of trait cards
    __init__.py             - imports all trait_cards to package namespace
    all_trait_cards.py      - logic for dealing with all trait cards
    ambush.py       - to represent an ambush card
    burrowing.py    - to represent a burrowing card
    cards.py        - abstract class to represent a trait card
    carnivore.py    - to represent a carnivore card
    climbing.py     - to represent a climbing card
    cooperation.py  - to represent a cooperation card
    fat_tissue.py   - to represent a fat tissue card
    fertile.py      - to represent a fertile card
    foraging.py     - to represent a foraging card
    hard_shell.py   - to represent a hard shell card
    herding.py      - to represent a herding card
    horn.py         - to represent a horn card
    long_neck.py    - to represent a long neck card
    pack_hunting.py - to represent a pack hunting card
    scavenger.py    - to represent a scavenger card
    symbiosis.py    - to represent a symbiosis card
    warning.py      - to represent a warning card
  constants.py          - The constants for evolution
  data_defs.py          - The data definitions for evolution
  feeding.py            - class that does the operations done on a JSON Feeding
  situation.py          - The evo Situation class that does the operations done on a JSON Situation
  situation_flag.py     - Enumeration to indicate the participant in a situation
  species.py            - To represent the Species
  species_types.py      - contains specific species like carnivore, vegetarian, fat-species
  util.py               - module for generic helper methods
executefeed1/   : To represent types of feed1 results
  feed1result.py      - Abstract class to represent result
  multiple_choices.py - Indicate multiple feeding choices
  no_choice           - Indicate no feeding choice
  one_choice          - Indicates an automatic feeding
gui/        : contains GUI files :
  constants.py              - GUI constants
  display.py                - Super-class for displaying GUI components
  display_card.py           - Displays a TraitCard
  display_dealer.py         - Displays a Dealer
  display_full_player.py    - Displays a PlayerState with its hand
  display_player.py         - Displays a PlayerState without hand
  display_self_player.py    - Displays a configuration for a PlayerState
  display_species.py        - Displays a Species
  horiz_scroll_frame        - A Frame with a scrollbar
/remote     : folder for remote protocol :
  remote.txt - remote protocols
/view_model : folder for view model :
  view_card.py          - view model for TraitCard
  view_dealer.py        - view model for Dealer
  view_deck.py          - view model for Deck
  view_player_state.py  - view model for PlayerState
  view_species.py       - view model for Species
feed.docx   - editable memo [n dealer interaction with choose_feeding
feed.pdf    - memo on Dealer interaction with choose_feeding
xattack     - executable launcher for xattack.py (chmod u+x xfeed; ./xattack)
xattack.py  - test harness for is_attackable method
xfeed       - executable launcher for xfeed.py (chmod u+x xfeed; ./xfeed)
xfeed.py    - test harness for choose_feeding
xgui        - JSON harness for dealer and player GUI
xstep.py    - test harness for feed1 method
xstep       - executable launcher for xstep.py (chmod u+x xfeed; ./xstep)

##########################################
#        Execution
##########################################

Running this program:
Note: before running an executable, may be necessary to run "chmod u+x <executable_name>"
Interactive programs (input taken from stdin, output sent to stdout):
  - run silly Player harness:
      ./xsilly
  - run main program with n players:
      ./main n
  - run GUI example harness:
      ./xgui
  - run JSON echo stream (while in ./Streaming/):
      ./xstream
  - run attack situation test-harness:
      ./xattack
  - run feeding scenario test-harness (indexed)
      ./xfeed
  - run server
      ./xserver_main
  - run client
      ./xclient_main

Testing programs:
  - run all tests
      ./xall_tests


##########################################
#  Running server and client
##########################################
Run server first
Run client (must connect with
at least three players to begin the game)




##########################################
#        Program structure
##########################################

Program structure:
  main.py runs the game by taking an argument n, which is the number of players. The main then sets
  up the game and runs it, then prints the results.
  dealer.py: Dealer.run_game() method runs a complete simulation of the game, and returns the
  score of the players.

  player.py contains the methods that implement the silly player strategy. get_card_choices selects which
  cards to play.
  feeding.player.player.Player contains player strategy for the game, working off of PlayerState.
  feeding.player.player_state.PlayerState is a container for information about a player, and is
    controlled by the game
  feeding.species_trait_other.Species contains information about a species board, including basic
    fields and the TraitCards that the species has
  feeding.species_trait_other.TraitCard is an abstract class representing a trait card, with
    implementations in the modules feeding.trait_card.*

As modular software, this code has a number of entry points.
The primary methods include:
  feeding.species_cards_other.Species.is_attackable()
  feeding.player.player.Player.choose_feeding()

JSON harnesses for is_attackable and choose_feeding can be run in the command line using ./xattack
and ./xfeed, respectively, as specified above. The echo stream is independent of the rest of the
program and can be started by running Streaming/xstream
