import re
import time
from datetime import datetime
from iqthon import StartTime, iqthon
from iqthon.Config import Config
from iqthon.plugins import mention
help1 = ("**🇮🇶 ⦙ كيفيه التنصيب :**")
help2 = ("**🇮🇶 ⦙ قـائمـه الاوامـر :**\n - اوامر الاونلاين تشتغل فقط في المجموعات ")
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Sour = f"**🇮🇶 : version 7.6  𓇡.** \n🇮🇶 : me  {mention}  𓇡. \n**🇮🇶 : time  {TM}  𓇡.**\n**🇮🇶 : My Bot {TG_BOT} 𓇡.**"
