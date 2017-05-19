'''
This is example configuration for Stratum server.
Please rename it to config.py and fill correct values.

This is already setup with sane values for solomining.
You NEED to set the parameters in BASIC SETTINGS
'''

# ******************** BASIC SETTINGS ***************
# These are the MUST BE SET parameters!

CENTRAL_WALLET = 'set_valid_addresss_in_config!'	# local litecoin address where money goes

LITECOIN_TRUSTED_HOST = 'localhost'
LITECOIN_TRUSTED_PORT = 8332
LITECOIN_TRUSTED_USER = 'user'
LITECOIN_TRUSTED_PASSWORD = 'somepassword'

# ******************** BASIC SETTINGS ***************
# Backup Litecoind connections (consider having at least 1 backup)
# You can have up to 99

#LITECOIN_TRUSTED_HOST_1 = 'localhost'
#LITECOIN_TRUSTED_PORT_1 = 8332
#LITECOIN_TRUSTED_USER_1 = 'user'
#LITECOIN_TRUSTED_PASSWORD_1 = 'somepassword'

#LITECOIN_TRUSTED_HOST_2 = 'localhost'
#LITECOIN_TRUSTED_PORT_2 = 8332
#LITECOIN_TRUSTED_USER_2 = 'user'
#LITECOIN_TRUSTED_PASSWORD_2 = 'somepassword'

# ******************** GENERAL SETTINGS ***************

# Enable some verbose debug (logging requests and responses).
DEBUG = False

# Destination for application logs, files rotated once per day.
LOGDIR = 'log/'

# Main application log file.
LOGFILE = None		# eg. 'stratum.log'

# Possible values: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOGLEVEL = 'INFO'

# Logging Rotation can be enabled with the following settings
# It if not enabled here, you can set up logrotate to rotate the files. 
# For built in log rotation set LOG_ROTATION = True and configrue the variables
LOG_ROTATION = True
LOG_SIZE = 10485760 # Rotate every 10M
LOG_RETENTION = 10 # Keep 10 Logs
# How many threads use for synchronous methods (services).
# 30 is enough for small installation, for real usage
# it should be slightly more, say 100-300.
THREAD_POOL_SIZE = 30

ENABLE_EXAMPLE_SERVICE = True

# ******************** TRANSPORTS *********************

# Hostname or external IP to expose
HOSTNAME = 'localhost'

# Port used for Socket transport. Use 'None' for disabling the transport.
LISTEN_SOCKET_TRANSPORT = 3333
# Port used for HTTP Poll transport. Use 'None' for disabling the transport
LISTEN_HTTP_TRANSPORT = None
# Port used for HTTPS Poll transport
LISTEN_HTTPS_TRANSPORT = None
# Port used for WebSocket transport, 'None' for disabling WS
LISTEN_WS_TRANSPORT = None
# Port used for secure WebSocket, 'None' for disabling WSS
LISTEN_WSS_TRANSPORT = None

# Hostname and credentials for one trusted Bitcoin node ("Satoshi's client").
# Stratum uses both P2P port (which is 8333 already) and RPC port
# LITECOIN_TRUSTED_* 	-- in basic settings above

IRC_NICK = None

# Salt used when hashing passwords
PASSWORD_SALT = 'some_crazy_string'

# ******************** Database  *********************

DATABASE_DRIVER = 'sqlite'	# Options: none, sqlite, postgresql or mysql
DATABASE_EXTEND = False		# False = pushpool db layout, True = pushpool + extra columns

# SQLite
DB_SQLITE_FILE = 'pooldb.sqlite'
# Postgresql
DB_PGSQL_HOST = 'localhost'
DB_PGSQL_DBNAME = 'pooldb'
DB_PGSQL_USER = 'pooldb'
DB_PGSQL_PASS = '**empty**'
DB_PGSQL_SCHEMA = 'public'
# MySQL
DB_MYSQL_HOST = 'localhost'
DB_MYSQL_DBNAME = 'pooldb'
DB_MYSQL_USER = 'pooldb'
DB_MYSQL_PASS = '**empty**'

# ******************** Adv. DB Settings *********************
#  Don't change these unless you know what you are doing

DB_LOADER_CHECKTIME = 15	# How often we check to see if we should run the loader
DB_LOADER_REC_MIN = 10		# Min Records before the bulk loader fires
DB_LOADER_REC_MAX = 50		# Max Records the bulk loader will commit at a time

DB_LOADER_FORCE_TIME = 300      # How often the cache should be flushed into the DB regardless of size.

DB_STATS_AVG_TIME = 300		# When using the DATABASE_EXTEND option, average speed over X sec
				#	Note: this is also how often it updates
DB_USERCACHE_TIME = 600		# How long the usercache is good for before we refresh

# ******************** Pool Settings *********************

# User Auth Options
USERS_AUTOADD = False		# Automatically add users to db when they connect.
USERS_AUTOADD_ACCOUNTID = 1     # Automatically add users to db when they connect.
				# 	This basically disables User Auth for the pool.
USERS_CHECK_PASSWORD = False	# Check the workers password? (Many pools don't)

# Transaction Settings
# CENTRAL_WALLET	---- In basic settings at top
COINBASE_EXTRAS = '/stratumPool/'			# Extra Descriptive String to incorporate in solved blocks
ALLOW_NONLOCAL_WALLET = False				# Allow valid, but NON-Local wallet's

# Litecoind communication polling settings (In Seconds)
PREVHASH_REFRESH_INTERVAL = 5 	# How often to check for new Blocks
				#	If using the blocknotify script (recommended) set = to MERKLE_REFRESH_INTERVAL
				#	(No reason to poll if we're getting pushed notifications)
MERKLE_REFRESH_INTERVAL = 60	# How often check memorypool
				#	This effectively resets the template and incorporates new transactions.
				#	This should be "slow"

INSTANCE_ID = 31		# Not a clue what this is for... :P

# ******************** Pool Difficulty Settings *********************
#  Again, Don't change unless you know what this is for.

# Pool Target (Base Difficulty)
POOL_TARGET = 16			# Pool-wide difficulty target int >= 1

# Variable Difficulty Enable
VARIABLE_DIFF = True		# Master variable difficulty enable

# Variable diff tuning variables
#VARDIFF will start at the POOL_TARGET. It can go as low as the VDIFF_MIN and as high as min(VDIFF_MAX or Liteconin's difficulty)
DIFF_UPDATE_FREQUENCY = 86400 # Update the litecoin difficulty once a day for the VARDIFF maximum
VDIFF_MIN_TARGET = 15		#  Minimum Target difficulty 
VDIFF_MAX_TARGET = 1000		# Maximum Target difficulty 
VDIFF_TARGET_TIME = 30		# Target time per share (i.e. try to get 1 share per this many seconds)
VDIFF_RETARGET_TIME = 120		# Check to see if we should retarget this often
VDIFF_VARIANCE_PERCENT = 20	# Allow average time to very this % from target without retarget

# ******************** Stats Settings *********************

BASIC_STATS = True		# Enable basic stats page. This has stats for ALL users.
				#   (Requires advanced database to be enabled)
				#	Human : http://<hostname>:<BASIC_STATS_PORT>/
				#	JSON  : http://<hostname>:<BASIC_STATS_PORT>/stats
				#   (Disable if you have your own frontend)

BASIC_STATS_PORT = 8889		# Port to listen on

# ******************** Getwork Proxy Settings *********************
# This enables a copy of slush's getwork proxy for old clients
# It will also auto-redirect new clients to the stratum interface
# so you can point ALL clients to: http://<yourserver>:<GW_PORT>

GW_ENABLE = False		# Enable the Proxy (If enabled you MUST run update_submodules)
GW_PORT = 8331			# Getwork Proxy Port
GW_DISABLE_MIDSTATE = False	# Disable midstate's (Faster but breaks some clients)
GW_SEND_REAL_TARGET = False	# Propigate >1 difficulty to Clients (breaks some clients)

# ******************** Archival Settings *********************

ARCHIVE_SHARES = False		# Use share archiving?
ARCHIVE_DELAY = 86400		# Seconds after finding a share to archive all previous shares
ARCHIVE_MODE = 'file'		# Do we archive to a file (file) , or to a database table (db)

# Archive file options
ARCHIVE_FILE = 'archives/share_archive'	# Name of the archive file ( .csv extension will be appended)
ARCHIVE_FILE_APPEND_TIME = True		# Append the Date/Time to the end of the filename (must be true for bzip2 compress)
ARCHIVE_FILE_COMPRESS = 'none'		# Method to compress file (none,gzip,bzip2)

# ******************** E-Mail Notification Settings *********************

NOTIFY_EMAIL_TO = ''		# Where to send Start/Found block notifications
NOTIFY_EMAIL_TO_DEADMINER = ''	# Where to send dead miner notifications
NOTIFY_EMAIL_FROM = 'root@localhost'	# Sender address
NOTIFY_EMAIL_SERVER = 'localhost'	# E-Mail Sender
NOTIFY_EMAIL_USERNAME = ''		# E-Mail server SMTP Logon
NOTIFY_EMAIL_PASSWORD = ''
NOTIFY_EMAIL_USETLS = True



# ******************** Admin settings *********************

# Use scripts/generateAdminHash.sh <password> to generate the hash
# for calculating SHA256 of your preferred password
ADMIN_PASSWORD_SHA256 = '9e6c0c1db1e0dfb3fa5159deb4ecd9715b3c8cd6b06bd4a3ad77e9a8c5694219' # SHA256 of the password

# If ADMIN_PORT is set, you can issue commands to that port to interact with 
# the system for things such as user management. It's a JSON interface following 
# REST principles, so '/users' returns a list of users, '/users/1' or '/users/username'
# returns a single user. POSTs are done to lists (so /users), PUTs are done to 
# items (so /users/1)
ADMIN_PORT = 8085 #Port for JSON admin commands, None to disable

