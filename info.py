import re
from os import environ,getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '24179601'))
API_HASH = environ.get('API_HASH', '386ee96911880799a0acd8a0476afc67')
BOT_TOKEN = environ.get('BOT_TOKEN', '6674455532:AAFohdrrFyL-qNGB8D-iZoju-lJal6sT2vU')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
PICS = (environ.get('PICS', 'https://graph.org/file/40379dba678f4368130da.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://te.legra.ph/file/a27dc8fe434e6b846b0f8.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://t.me/+XVkAQZ81xP8wZTBl")
SPELL_IMG = environ.get("SPELL_IMG", "https://te.legra.ph/file/15c1ad448dfe472a5cbb8.jpg")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ' -1002045867639'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1141220790 1800454242 786843013').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002086293621').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '786843013 1800454242').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1002187795622')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '@Telugu_Movie_Room')
reqst_channel = environ.get('REQST_CHANNEL_ID', '@kdrama_cdrama_multiverse')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', ' -1002086293621')).split()]
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI','mongodb+srv://sanjutyson:sanjutysonn@tyson.dgo5rff.mongodb.net/?retryWrites=true&w=majority')
DATABASE_NAME = environ.get('DATABASE_NAME', "NewFiles")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Test_Files')

# Premium And Referal Settings
PREMIUM_AND_REFERAL_MODE = bool(environ.get('PREMIUM_AND_REFERAL_MODE', False)) # Set Ture Or False

# If PREMIUM_AND_REFERAL_MODE is True Then Fill Below Variable, If Flase Then No Need To Fill.
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '20')) # number of referal count
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month')
PAYMENT_QR = environ.get('PAYMENT_QR', '0')
PAYMENT_TEXT = environ.get('PAYMENT_TEXT', '<b>- ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs - \n\n- 70ʀs - 1 ᴍᴏɴᴛʜs\n- 210ʀs - 3 ᴍᴏɴᴛʜs\n- 420ʀs - 6 ᴍᴏɴᴛʜs\n\n🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🎁\n\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ\n○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs\n○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ\n○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ\n○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs\n○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs\n○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ\n○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ\n\n✨ ᴜᴘɪ ɪᴅ - <code>tysonsanju2000@airtel</code>\n\nᴄʟɪᴄᴋ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /myplan\n\n💢 ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ to @Dontdisturbmeu ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ\n\n‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ</b>')
OWNER_USERNAME = environ.get('OWNER_USERNAME', 'Dontdisturbmeu') # owner username without @

# Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+XMluXFYaeAJkZGE1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/kdrama_cdrama_multiverse')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/Tyson_Channel_No1/20')
VERIFY_TUTORIAL = environ.get('VERIFY_TUTORIAL', 'https://t.me/Tyson_Channel_No1/20')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 't.me/+XMluXFYaeAJkZGE1') # Support Chat Link Without https:// or @

# True Or False
PM_SEARCH = bool(environ.get('PM_SEARCH', True)) # In Pm Search Currently Spell Check Doesn't Work.
SHORTLINK_MODE = bool(environ.get('SHORTLINK_MODE', False))
VERIFY = bool(environ.get('VERIFY', False))
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', False))
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "True"), True)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), False)
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

# Shortlink Info
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')

# Others
MAX_B_TN = environ.get("MAX_B_TN", "5")
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', '⚡ Hello My Dear Friends ⚡')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "⚡️<b>File uploaded by [@KDTDRAMA](https://t.me/K_dramasTelugudubbedinaha)</b>⚡️\n\n🎦 <b>File Name: </b> ➥  {file_caption} \n⚙️ <b>Size: </b><i>{file_size}</i>\n\n                ❤️<b>WE LOVE YOU</b>❤️\n🔥  ↭ <b>Join Now [KDTDRAMA](@K_dramasTelugudubbedinaha)</b> ↭  🔥")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)

# Choose Option Settings 
LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]
SEASONS = ["season 1", "season 2", "season 3", "season 4", "season 5", "season 6", "season 7", "season 8", "season 9", "season 10"]
EPISODES = ["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20", "E21", "E22", "E23", "E24", "E25", "E26", "E27", "E28", "E29", "E30", "E31", "E32", "E33", "E34", "E35", "E36", "E37", "E38", "E39", "E40"]
QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "2160p"]

                      

# Online Stream and Download
STREAM_MODE = bool(environ.get('STREAM_MODE', False)) # Set True or Flase

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = False    
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://fiscal-ebony-streamhab-3abf473f.koyeb.app/")


# Rename Info ; If True Then Bot Rename File Else Not
RENAME_MODE = bool(environ.get('RENAME_MODE', False)) # Set True or Flase
# Auto Approve Info ; If True Then Bot Approve New Upcoming Join Request Else Not
AUTO_APPROVE_MODE = bool(environ.get('AUTO_APPROVE_MODE', False)) # Set True or Flase

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
