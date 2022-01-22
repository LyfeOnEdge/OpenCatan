#MAINLOOP PHASES
PHASE_SETUP	= 			-1
PHASE_ROLL = 			0
PHASE_DEAL	= 			1
PHASE_BUILD_AND_TRADE= 	2
PHASE_END_TURN = 		3
PHASE_END_GAME = 		4

#RESOURCE_TYPES
RESOURCE_WATER = -2
RESOURCE_WASTELAND	= -1
RESOURCE_CATTLE	= 1
RESOURCE_WHEAT	= 2
RESOURCE_IRON	= 3
RESOURCE_WOOD	= 4
RESOURCE_BRICK	= 5
RESOURCE_GOLD	= 6 #NYI

RESOURCES = [
	RESOURCE_CATTLE,
	RESOURCE_WHEAT,
	RESOURCE_IRON,
	RESOURCE_WOOD,
	RESOURCE_BRICK,
]

RESOURCE_TILES = [
	RESOURCE_CATTLE,
	RESOURCE_WHEAT,
	RESOURCE_IRON,
	RESOURCE_WOOD,
	RESOURCE_BRICK,
	RESOURCE_WASTELAND,
]

ALL_TILE_TYPES = [
	RESOURCE_CATTLE,
	RESOURCE_WHEAT,
	RESOURCE_IRON,
	RESOURCE_WOOD,
	RESOURCE_BRICK,
	RESOURCE_WASTELAND,
	RESOURCE_WATER
]

RESOURCE_MAP_INT_TO_NAME = {
	RESOURCE_CATTLE : "Cattle",
	RESOURCE_WHEAT : "Wheat",
	RESOURCE_IRON : "Iron",
	RESOURCE_WOOD : "Wood",
	RESOURCE_BRICK : "Brick",
	RESOURCE_WASTELAND : "Barren",
	RESOURCE_WATER : "Water",
	"*":"*",
}

RESOURCE_MAP_INT_TO_COLOR = {
	RESOURCE_CATTLE : (70, 255, 70),
	RESOURCE_WHEAT : (230, 240, 0),
	RESOURCE_IRON : (120,120,120),
	RESOURCE_WOOD : (14, 140, 31),
	RESOURCE_BRICK : (255, 160, 100),
	RESOURCE_WASTELAND : (181, 121, 20),
	RESOURCE_WATER : (60,100,230),
}

#RECIPES
RECIPE_KEY_ROAD			=0
RECIPE_KEY_SETTLEMENT	=1
RECIPE_KEY_CITY			=2
RECIPE_KEY_ACHIEVEMENT	=3
RECIPES = {
	RECIPE_KEY_ROAD : {
		RESOURCE_WOOD 	: 1,
		RESOURCE_BRICK	: 1
	},
	RECIPE_KEY_SETTLEMENT : {
		RESOURCE_CATTLE	: 1,
		RESOURCE_WHEAT	: 1,
		RESOURCE_BRICK	: 1,
		RESOURCE_WOOD	: 1,
	},
	RECIPE_KEY_CITY : {
		RESOURCE_IRON 	: 3,
		RESOURCE_WHEAT	: 2,
	},
	RECIPE_KEY_ACHIEVEMENT : {
		RESOURCE_CATTLE	: 1,
		RESOURCE_WHEAT	: 1,
		RESOURCE_IRON	: 1,
	},
}
RECIPE_MAP_INT_TO_NAME = {
	RECIPE_KEY_ROAD : "Road",
	RECIPE_KEY_SETTLEMENT : "Town",
	RECIPE_KEY_CITY : "Capital",
	RECIPE_KEY_ACHIEVEMENT : "Achievement",
}

RESOURCE_MAP_NAME_TO_INT = {RESOURCE_MAP_INT_TO_NAME[k]:k for k in RESOURCE_MAP_INT_TO_NAME.keys()}

DEFAULT_BANK_EXCHANGE_RATES = {
	"*":4, #4 of any card, base trade
}

DEFAULT_PORT_EXCHANGE_RATES = {
	"*":3,
	RESOURCE_CATTLE:2,
	RESOURCE_WHEAT:2,
	RESOURCE_IRON:2,
	RESOURCE_BRICK:2,
	RESOURCE_WOOD:2,
}

#BUILD PHASE OPTIONS
OPTION_CANCEL 			 = -1
OPTION_BUILD_ROAD		 = 1
OPTION_BUILD_SETTLEMENT	 = 2
OPTION_BUILD_CITY		 = 3

OPTION_BUILD_ACHIEVEMENT = 4
OPTION_NATURAL_PAVIMENTUM	= 40
OPTION_BOUNTIFUL_HARVEST	= 41
OPTION_CLAIMED_PRODUCT		= 42
OPTION_USE_PATROL			= 43

OPTION_REQUEST_TRADE	 = 5
OPTION_END_TURN			 = 6








BUILD_PHASE_OPTIONS = [
	OPTION_BUILD_ROAD,
	OPTION_BUILD_SETTLEMENT,
	OPTION_BUILD_CITY,
	OPTION_BUILD_ACHIEVEMENT,
	OPTION_REQUEST_TRADE,
	OPTION_END_TURN
]


#3-4 PLAYER DEFINITIONS
DEFAULT_PIECE_LIMITS_3_4 = {
	RECIPE_KEY_ROAD: 15,
	RECIPE_KEY_SETTLEMENT: 5,
	RECIPE_KEY_CITY: 4,
}

DEFAULT_TILE_COUNTS_3_4 = {
	RESOURCE_CATTLE : 4,
	RESOURCE_WHEAT : 4,
	RESOURCE_IRON : 3,
	RESOURCE_WOOD : 4,
	RESOURCE_BRICK : 3,
	RESOURCE_WASTELAND : 1,
}

DEFAULT_RESOURCE_CARD_COUNT_3_4 = {
	RESOURCE_CATTLE : 19,
	RESOURCE_WHEAT : 19,
	RESOURCE_IRON : 19,
	RESOURCE_WOOD : 19,
	RESOURCE_BRICK : 19,
}

DEFAULT_CHIT_COUNT_3_4 = {
	2:1,
	3:2,
	4:2,
	5:2,
	6:2,
	8:2,
	9:2,
	10:2,
	11:2,
	12:1,
}

DEFAULT_NUMBER_OF_TRADING_PORT_ATTEMPTS = 20
DEFAULT_PORT_CHANCE = 0.65

DEFAULT_MIN_ROADS_FOR_VIA_DOMINI = 5
DEFAULT_MIN_PORTS_FOR_PORTUM_DOMINI = 3
DEFAULT_MIN_PATROLS_FOR_MILITUM_DOMINUS = 3

# DEFAULT_NUM_EACH_TYPE_ACTION_CARDS = 2
# DEFAULT_NUM_EACH_TYPE_GOAL_CARDS = 1
# DEFAULT_ACHIEVEMENT_PATROL_COUNT = 14

DEFAULT_NUM_EACH_TYPE_ACTION_CARDS = 5
DEFAULT_NUM_EACH_TYPE_GOAL_CARDS = 5
DEFAULT_ACHIEVEMENT_PATROL_COUNT = 10

# ACHIEVEMENT_KNIGHT		:14,
# ACHIEVEMENT_PROGRESS	:6,
# ACHIEVEMENT_VICTORY		:5,

# DEFAULT_ACHIEVEMENT_CARD_COUNT = {
# 	ACHIEVEMENT_KNIGHT		:14,
# 	ACHIEVEMENT_PROGRESS	:6,
# 	ACHIEVEMENT_VICTORY		:5,
# }

# #5-6 PLAYER DEFINITIONS
# DEFAULT_TILE_COUNTS_5_6 = {
# 	RESOURCE_CATTLE : ,
# 	RESOURCE_WHEAT : ,
# 	RESOURCE_IRON : ,
# 	RESOURCE_WOOD : ,
# 	RESOURCE_BRICK : ,
# }

# DEFAULT_RESOURCE_CARD_COUNT_5_6 = {
# 	RESOURCE_CATTLE : ,
# 	RESOURCE_WHEAT : ,
# 	RESOURCE_IRON : ,
# 	RESOURCE_WOOD : ,
# 	RESOURCE_BRICK : ,
# }