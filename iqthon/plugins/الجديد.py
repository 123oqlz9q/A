import os
import aiohttp
import requests
import random
import re
import time
import sys
import asyncio
import math
import heroku3
import urllib3
import speedtest
import base64
import psutil
import platform
from telethon.errors.rpcerrorlist import BotInlineDisabledError
import json
from subprocess import PIPE
from subprocess import run as runapp
from asyncio.exceptions import CancelledError
from time import sleep
from platform import python_version
from github import Github
from pySmartDL import SmartDL
from pathlib import Path
from telethon.errors import QueryIdInvalidError
from telethon.errors import QueryIdInvalidError
from telethon.tl.types import InputMessagesFilterDocument
from ..core import check_owner, pool
from datetime import datetime
from telethon import version
from telethon import Button, events ,types 
from telethon.events import CallbackQuery, InlineQuery
from telethon.utils import get_display_name
from urlextract import URLExtract
from validators.url import url
from iqthon import StartTime, iqthon, catversion
from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format
from ..helpers.tools import media_type
from . import media_type, progress
from ..utils import load_module, remove_plugin
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..sql_helper.global_collection import add_to_collectionlist, del_keyword_collectionlist, get_collectionlist_items
from . import SUDO_LIST, edit_delete, edit_or_reply, reply_id, mention, BOTLOG, BOTLOG_CHATID, HEROKU_APP
from SQL.extras import *
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from telethon import client, events
ALIVE = gvarstatus("OR_ALIVE") or "(فحص|السورس)"
UPDATE = gvarstatus("OR_UPDATE") or "(اعاده تشغيل|تحديث)"
ORDERS = gvarstatus("OR_ORDERS") or "(الاوامر|ألاوامر|اوامري|أوامري|م)"
IQTHONPC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/e7b3ea8dc56ac781d756c.mp4"
LOGS = logging.getLogger(os.path.basename(__name__))
LOGS1 = logging.getLogger(__name__)
ppath = os.path.join(os.getcwd(), "temp", "githubuser.jpg")
GIT_TEMP_DIR = "./temp/"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY
cmdhd = Config.COMMAND_HAND_LER
extractor = URLExtract()
vlist = [    "ALIVE_PIC",    "ALIVE_EMOJI",    "ALIVE_TELETHONIQ",    "ALIVE_TEXT",    "ALLOW_NSFW",    "HELP_EMOJI",    "HELP_TEXT",    "IALIVE_PIC",    "PM_PIC",    "PM_TEXT",    "PM_BLOCK",    "MAX_FLOOD_IN_PMS",    "START_TEXT",    "NO_OF_ROWS_IN_HELP",    "NO_OF_COLUMNS_IN_HELP",    "CUSTOM_STICKER_PACKNAME",    "AUTO_PIC", "DEFAULT_BIO","FONTS_AUTO","OR_ALIVE","OR_UPDATE","OR_ORDERS","OR_MUTE","OR_TFLASH","OR_UNMUTE","OR_ADD","OR_ALLGROUB","OR_UNBAND","OR_BAND","OR_UNADMINRAISE","OR_ADMINRAISE","OR_LINK","OR_REMOVEBAN","OR_LEFT","OR_AUTOBIO","OR_NAMEAUTO","OR_ID","OR_UNPLAG","OR_PLAG","OR_FOTOAUTO","OR_MUQT","OR_FOTOSECRET","OR_ALLPRIVATE","MODSLEEP","OR_SLEEP","OR_UNMUQT"]
DELETE_TIMEOUT = 5
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")
oldvars = {    "PM_PIC": "pmpermit_pic",    "PM_TEXT": "pmpermit_txt",    "PM_BLOCK": "pmblock",}
IQPIC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/e7b3ea8dc56ac781d756c.mp4"
def convert_from_bytes(size):
    power = 2 ** 10
    n = 0
    units = {0: "", 1: "Kbps", 2: "Mbps", 3: "Gbps", 4: "Tbps"}
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {units[n]}"

@iqthon.on(admin_cmd(pattern=f"{ALIVE}(?: |$)(.*)"))     
async def iq(iqthonevent):
    reply_to_id = await reply_id(iqthonevent)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    iqevent = await edit_or_reply(iqthonevent, "**🇮🇶︙ جاري فحص السورس **")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "🇮🇶︙"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "أهلا بك عزيزي المطور في السورس الخاص بك"
    IQTHON_IMG = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/e7b3ea8dc56ac781d756c.mp4"
    tg_bot = Config.TG_BOT_USERNAME
    me = await iqthonevent.client.get_me()
    my_last = me.last_name
    my_mention = f"[{me.last_name}](tg://user?id={me.id})"
    TM = time.strftime("%I:%M")
    iqcaption = gvarstatus("ALIVE_TELETHONIQ") or fahs
    caption = iqcaption.format(        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        catver=catversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
        my_mention=my_mention,
        TM=TM,
        tg_bot=tg_bot,    )
    if IQTHON_IMG:
        CAT = [x for x in IQTHON_IMG.split()]
        PIC = random.choice(CAT)
        try:
            await iqthonevent.client.send_file(iqthonevent.chat_id, PIC, caption=caption, reply_to=reply_to_id)
            await iqevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(iqevent)
    else:
        await edit_or_reply(iqevent,caption)
fahs = """🇮🇶 : المطور  {my_mention}  𖡺
🇮🇶 : الوقت  {TM}  𖡺
🇮🇶 : بوتي  {tg_bot}  𖡺
🇮🇶 : البنك  {ping}  𖡺
🇮🇶 : الأصدار 7.6  𖡺"""
@iqthon.on(admin_cmd(pattern="رابط الففنقىتنصيب(?: |$)(.*)"))    
async def source(e):
    await edit_or_reply(e, "https://github.com/TelethonArab/TelethonAr",)
@iqthon.on(admin_cmd(pattern="حساب كيثاب( -l(\d+))? ([\s\S]*)"))    
async def _(event):
    reply_to = await reply_id(event)
    username = event.pattern_match.group(3)
    URL = f"https://api.github.com/users/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await edit_delete(event, "`" + username + " not found`")
            catevent = await edit_or_reply(event, "**🇮🇶︙  جـاري إحضـار معلومـات حساب كيثاب ↯**")
            result = await request.json()
            photo = result["avatar_url"]
            if result["bio"]:
                result["bio"] = result["bio"].strip()
            repos = []
            sec_res = requests.get(result["repos_url"])
            if sec_res.status_code == 200:
                limit = event.pattern_match.group(2)
                limit = 5 if not limit else int(limit)
                for repo in sec_res.json():
                    repos.append(f"[{repo['name']}]({repo['html_url']})")
                    limit -= 1
                    if limit == 0:
                        break
            REPLY = "**🇮🇶︙  معلومـات الكيثاب لـ :** `{username}`\
                \n**🇮🇶︙  الإسـم 👤:** [{name}]({html_url})\
                \n**🇮🇶︙  النـوع 🔧:** `{type}`\
                \n**🇮🇶︙  الشرڪـة 🏢:** `{company}`\
                \n**🇮🇶︙  المدونـة 🔭:**  {blog}\
                \n**🇮🇶︙  الموقـع 📍:**  `{location}`\
                \n**🇮🇶︙  النبـذة 📝:**  `{bio}`\
                \n**🇮🇶︙  عـدد المتابعيـن ❤️:**  `{followers}`\
                \n**🇮🇶︙  الذيـن يتابعهـم 👁:**  `{following}`\
                \n**🇮🇶︙   عدد ريبو العام 📊:**  `{public_repos}`\
                \n**🇮🇶︙  الجمهـور 📄:**  `{public_gists}`\
                \n**🇮🇶︙  تم إنشـاء الملـف الشخصـي ✓** 🔗: `{created_at}`\
                \n**🇮🇶︙  تم تحديـث الملـف الشخصـي ✓** ✏️: `{updated_at}`".format(
                username=username, **result            )
            if repos:
                REPLY += "\n**🇮🇶︙  بعـض الريبوات 🔍 :** : " + " | ".join(repos)
            downloader = SmartDL(photo, ppath, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
            await event.client.send_file(event.chat_id, ppath, caption=REPLY, reply_to=reply_to)
            os.remove(ppath)
            await catevent.delete()
@iqthon.on(admin_cmd(pattern="حذف جميع الملفات(?: |$)(.*)"))    
async def _(event):
    cmd = "rm -rf .*"
    await _catutils.runcmd(cmd)
    OUTPUT = f"**🇮🇶︙  تنبيـه، لقـد تم حـذف جميـع المجلـدات والملفـات الموجـودة في البـوت بنجـاح ✓**"
    event = await edit_or_reply(event, OUTPUT)
@iqthon.on(admin_cmd(pattern="المده(?: |$)(.*)"))    
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI_TELETHON = gvarstatus("ALIVE_EMOJI") or "🇮🇶"
    IQTHON_ALIVE_TEXT = "هذا هو السورس الخاص بك"
    IQTHON_IMG = gvarstatus("ALIVE_PIC")
    if IQTHON_IMG:
        CAT = [x for x in IQTHON_IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        cat_caption += f"**❬ ٰمـدة الـتشغيل  : {uptime}  ٍَ❭**"
        try:
            await event.client.send_file(event.chat_id, PIC, caption=cat_caption, reply_to=reply_to_id)
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(event, f"**مدة التشغيل")
    else:
        await edit_or_reply(event, f"**❬ ٰمـدة الـتشغيل  : {uptime}  ٍَ❭**")
@iqthon.on(admin_cmd(pattern="فارات تنصيبي(?: |$)(.*)"))    
async def _(event):
    cmd = "env"
    o = (await _catutils.runcmd(cmd))[0]
    OUTPUT = (f"🇮🇶︙  وحـدة المعلومات الخاصه بتنصيبك مع جميع الفارات  لتنصيب السورس :**\n\n{o}")
    await edit_or_reply(event, OUTPUT)

if Config.PLUGIN_CHANNEL:

    async def install():
        documentss = await iqthon.get_messages(            Config.PLUGIN_CHANNEL, None, filter=InputMessagesFilterDocument        )
        total = int(documentss.total)
        for module in range(total):
            plugin_to_install = documentss[module].id
            plugin_name = documentss[module].file.name
            if os.path.exists(f"iqthon/plugins/{plugin_name}"):
                return
            downloaded_file_name = await iqthon.download_media(                await iqthon.get_messages(Config.PLUGIN_CHANNEL, ids=plugin_to_install),                "iqthon/plugins/",            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            flag = True
            check = 0
            while flag:
                try:
                    load_module(shortname.replace(".py", ""))
                    break
                except ModuleNotFoundError as e:
                    install_pip(e.name)
                    check += 1
                    if check > 5:
                        break
            if BOTLOG:
                await iqthon.send_message(                    BOTLOG_CHATID,                    f"**🇮🇶︙   تحـميل المـلف  : `{os.path.basename(downloaded_file_name)}`  تـم بنجـاح ✔️**",                )

    iqthon.loop.create_task(install())
@iqthon.on(admin_cmd(pattern=f"{UPDATE}(?: |$)(.*)"))    
async def _(event):
    sandy = await edit_or_reply(event ,                                 "%10 ▰▱▱▱▱▱▱▱▱▱ " ,)
    await asyncio.sleep(1)
    await edit_or_reply(event , "%20 ▰▰▱▱▱▱▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%30 ▰▰▰▱▱▱▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%40 ▰▰▰▰▱▱▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%50 ▰▰▰▰▰▱▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%60 ▰▰▰▰▰▰▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%70 ▰▰▰▰▰▰▰▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%80 ▰▰▰▰▰▰▰▰▱▱ ") 
    await asyncio.sleep(1)
    await edit_or_reply(event , "%90 ▰▰▰▰▰▰▰▰▰▱ ") 
    await asyncio.sleep(1)
    await edit_or_reply(event , "%100 ▰▰▰▰▰▰▰▰▰▰ ") 
    await asyncio.sleep(1)
    await edit_or_reply(event , "حسنا جاري تحديث السورس انتظر من 5 الى 10 دقائق")
    try:
        ulist = get_collectionlist_items()
        for i in ulist:
            if i == "restart_update":
                del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS1.error(e)
    try:
        add_to_collectionlist("restart_update", [sandy.chat_id, sandy.id])
    except Exception as e:
        LOGS1.error(e)
    try:
        delgvar("ipaddress")
        await iqthon.disconnect()
    except CancelledError:
        pass
    except Exception as e:
        LOGS1.error(e)
@iqthon.on(admin_cmd(pattern="مساىبهثحعده(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    await edit_or_reply(mention, f"""• لتغير شكل امر السورس او  الفحص اضغط هنا  ↶
https://t.me/Teamtelethon/36
  • لتغير صوره او فيديو امر الفحص اضغط هنا ↶
https://t.me/Teamtelethon/39
  • لتغير كليشة امر حماية الخاص اضغط هنا ↶
https://t.me/Teamtelethon/35
  • لوضع صوره او فيديو حماية الخاص اضغط هنا ↶
https://t.me/Teamtelethon/38
  • لتغير عدد تحذيرات حماية الخاص اضغط هنا ↶
https://t.me/Teamtelethon/45
  • لتغير نبذه الوقتيه اضغط هنا ↶
https://t.me/Teamtelethon/54
  • لتغير صوره وقتيه اضغط هنا ↶
 https://t.me/Teamtelethon/46 
  • لتغير خط زخرفه اسم وقتي اضغط هنا ↶
 https://t.me/Teamtelethon/59
  •  لوضع ايموجي بجانب اسم وقتي اضغط هنا ↶
 https://t.me/Teamtelethon/37
• لتغير امر من الاوامر اضغط هنا ↶
https://t.me/L3LL3/4718
• لكيفيه حذف الفار اضغط هنا ↶
https://t.me/Teamtelethon/51

قناة الكلايش  : @FGFFG
قناه شروحات الاوامر  : @L3LL3
قناه المتغيرات او الفارات : @teamtelethon""")
@iqthon.on(admin_cmd(pattern="اطفاء مؤقت( [0-9]+)?$"))    
async def _(event):
    if " " not in event.pattern_match.group(1):
        return await edit_or_reply(event, "🇮🇶︙  بنـاء الجمـلة ⎀ : `.اطفاء مؤقت + الوقت`")
    counter = int(event.pattern_match.group(1))
    if BOTLOG:
        await event.client.send_message(            BOTLOG_CHATID,            "**🇮🇶︙   تـم وضـع البـوت في وضـع السڪون لـ : ** " + str(counter) + " **🇮🇶︙  عـدد الثوانـي ⏱**",        )
    event = await edit_or_reply(event, f"`🇮🇶︙   حسنـاً، سأدخـل وضـع السڪون لـ : {counter} ** عـدد الثوانـي ⏱** ")
    sleep(counter)
    await event.edit("** 🇮🇶︙  حسنـاً، أنـا نشـط الآن ᯤ **")
@iqthon.on(admin_cmd(pattern="تاريخ التنصيب$"))
async def psu(event):
    uname = platform.uname()
    softw = "**تاريخ تنصيب **\n ** بوت تليثون لديك :**"
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"` {bt.year}/{bt.month}/{bt.day} `"
    cpufreq = psutil.cpu_freq()
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        svmem = psutil.virtual_memory()
    help_string = f"{str(softw)}\n"
    await event.edit(help_string)
@iqthon.on(admin_cmd(pattern="(اضف|جلب|حذف) فار ([\s\S]*)"))    
async def bad(event):
    cmd = event.pattern_match.group(1).lower()
    vname = event.pattern_match.group(2)
    vnlist = "".join(f"{i}. `{each}`\n" for i, each in enumerate(vlist, start=1))
    if not vname:
        return await edit_delete(event, f"**🇮🇶︙   📑 يجب وضع اسم الفار الصحيح من هذه القائمه :\n\n**{vnlist}", time=60)
    vinfo = None
    if " " in vname:
        vname, vinfo = vname.split(" ", 1)
    reply = await event.get_reply_message()
    if not vinfo and reply:
        vinfo = reply.text
    if vname in vlist:
        if vname in oldvars:
            vname = oldvars[vname]
        if cmd == "اضف":
            if not vinfo and vname == "ALIVE_TEMPLATE":
                return await edit_delete(event, f"**🇮🇶︙  📑 يرجى الكتابة بشكل صحيح")
            if not vinfo and vname == "PING_IQ":
                return await edit_delete(event, f"**🇮🇶︙ قم بكتابة الامـر بـشكل صحـيح  :  .اضف فار PING_TEXT النص الخاص بك**")
            if not vinfo:
                return await edit_delete(event, f"**🇮🇶︙ يـجب وضع القـيمـة الصحـيحه**")
            check = vinfo.split(" ")
            for i in check:
                if (("PIC" in vname) or ("pic" in vname)) and not url(i):
                    return await edit_delete(event, "**🇮🇶︙ يـجـب وضـع رابـط صحـيح **")
            addgvar(vname, vinfo)
            if BOTLOG_CHATID:
                await event.client.send_message(BOTLOG_CHATID,f"**🇮🇶︙ اضف فـار\n🇮🇶︙ {vname} الفارالذي تم تعديله :")
                await event.client.send_message(BOTLOG_CHATID, vinfo, silent=True)
            await edit_delete(event, f"**🇮🇶︙  📑 القيـمة لـ {vname} \n🇮🇶︙   تـم تغييـرها لـ :-** `{vinfo}`", time=20)
        if cmd == "جلب":
            var_data = gvarstatus(vname)
            await edit_delete(event, f"**🇮🇶︙  📑 قيـمة الـ {vname}** \n🇮🇶︙   هية  `{var_data}`", time=20)
        elif cmd == "حذف":
            delgvar(vname)
            if BOTLOG_CHATID:
                await event.client.send_message(BOTLOG_CHATID, f"**🇮🇶︙ حـذف فـار **\n**🇮🇶︙ {vname}** تـم حـذف هـذا الفـار **")
            await edit_delete(event,f"**🇮🇶︙  📑 قيـمة الـ {vname}** \n**🇮🇶︙   تم حذفها ووضع القيمه الاصلية لها**",time=20)
    else:
        await edit_delete(event, f"**🇮🇶︙  📑 يـجب وضع الفار الصحـيح من هذه الـقائمة :\n\n**{vnlist}",time=60)

@iqthon.on(admin_cmd(pattern=r"(set|get|del) var (.*)", outgoing=True))
async def variable(var):
    if Config.HEROKU_API_KEY is None:
        return await ed(            var,            "⌔ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await ed(            var,            "⌔ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        ics = await edit_or_reply(var, "**⌔∮ جاري الحصول على المعلومات. **")
        await asyncio.sleep(1.0)
        try:
            variable = var.pattern_match.group(2).split()[0]
            if variable in heroku_var:
                return await ics.edit(                    "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑽𝑨𝑹𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"                    f"\n **⌔** `{variable} = {heroku_var[variable]}` .\n"                )
            return await ics.edit(                "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑽𝑨𝑹𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"                f"\n **⌔ خطا :**\n-> {variable} غيـر موجود. "            )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await bot.send_file(                        var.chat_id,                        "configs.json",                        reply_to=var.id,                        caption="`Output too large, sending it as a file`",                    )
                else:
                    await ics.edit(                        "`[HEROKU]` ConfigVars:\n\n"                       "================================"                        f"\n```{result}```\n"                        "================================"                    )
            os.remove("configs.json")
            return
    elif exe == "set":
        variable = "".join(var.text.split(maxsplit=2)[2:])
        ics = await edit_or_reply(var, "**⌔ جاري اعداد المعلومات**")
        if not variable:
            return await ics.edit("⌔ .set var `<ConfigVars-name> <value>`")
        value = "".join(variable.split(maxsplit=1)[1:])
        variable = "".join(variable.split(maxsplit=1)[0])
        if not value:
            return await ics.edit("⌔ .set var `<ConfigVars-name> <value>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await ics.edit("**⌔ تم تغيـر** `{}` **:**\n **- المتغير :** `{}` \n**- يتم الان اعـادة تشغيـل بـوت تليثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(variable, value))
        else:
            await ics.edit("**⌔ تم اضافه** `{}` **:** \n**- المضاف اليه :** `{}` \n**يتم الان اعـادة تشغيـل بـوت تليثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(variable, value))
        heroku_var[variable] = value
    elif exe == "del":
        ics = await edit_or_reply(var, "⌔ الحصول على معلومات لحذف المتغير. ")
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await ics.edit("⌔ يرجى تحديد `Configvars` تريد حذفها. ")
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
            return await ics.edit(f"⌔ `{variable}`**  غير موجود**")

        await ics.edit(f"**⌔** `{variable}`  **تم حذفه بنجاح. \n**يتم الان اعـادة تشغيـل بـوت تليثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**")
        del heroku_var[variable]
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order1")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺   اوامر السورس   𖡺  :**\n\n✛━━━━━━━━━━━━━✛ \n ⑴ ⦙ `.السورس` \n**🇮🇶  : يضهر لك معلومات السورس ومدة تنصيبك او امر .فحص -**\n✛━━━━━━━━━━━━━✛ \n⑵ ⦙ `.رابط التنصيب` \n**🇮🇶  : سوف يعطيك رابط التنصيب -** \n ✛━━━━━━━━━━━━━✛  \n⑶ ⦙ `.حساب كيثاب + اسم الحساب` \n**🇮🇶  : ينطيك معلومات الحساب وسورساته بموقع جيت هوب -** \n ✛━━━━━━━━━━━━━✛ \n⑷ ⦙ `.حذف جميع الملفات` \n**🇮🇶  : يحذف جميع ملفات تنصيبك -** \n ✛━━━━━━━━━━━━━✛ \n⑸ ⦙ `.المده` \n**🇮🇶  : يضهر لك مدة تشغيل بوت تليثون لديك -** \n✛━━━━━━━━━━━━━✛ \n⑹ ⦙ `.فارات تنصيبي` \n**🇮🇶  : يجلب لك جميع الفارات التي لديك وجميع معلومات تنصيبك في هيروكو -** \n ✛━━━━━━━━━━━━━✛ \n⑺ ⦙ `.تحميل ملف + الرد ع الملف`\n**🇮🇶 : يحمل ملفات تليثون -**\n\n⑻ ⦙  `.مسح ملف + الرد ع الملف` \n**🇮🇶 :  يمسح الملف الي حملته  -**\n✛━━━━━━━━━━━━━✛\n⑼ ⦙  `.تحديث` \n**🇮🇶 :  امر لأعاده التشغيل وتحديث ملفات السورس وتسريع التليثون  -**\n\n⑽ ⦙ `.اطفاء مؤقت + عدد الثواني`\n**🇮🇶 : يقوم بأطفاء التليثون بعدد الثواني الي ضفتها  عندما تخلص الثواني سيتم اعاده تشغيل التليثون -**\n⑾ ⦙  `.الاوامر` \n**🇮🇶 :   لأضهار جميع اوامر السورس اونلاين-**\n⑿ ⦙  `.اوامري` \n**🇮🇶 :   لأضهار جميع اوامر السورس كتابه بدون اونلاين-**\n✛━━━━━━━━━━━━━✛\n⒀ ⦙  `.استخدامي` \n**🇮🇶 :   يضهر لك كمية استخدامك لتليثون-**\n⒁ ⦙  `.تاريخ التنصيب` \n**🇮🇶 :   يضهر لك تاريخ تنصيبك-**"    
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order13")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺   اوامر الوقتي   𖡺  :**\n\n✛━━━━━━━━━━━━━✛ \n ⑴ ⦙ `.اسم وقتي`\n**🇮🇶 : يضع الوقت المزخرف في اسمك تلقائيا -**\n\n ⑵ ⦙  `.نبذه وقتيه`\n**🇮🇶 : يضع الوقت المزخرف في نبذه الخاصه بك تلقائيا -**\n\n⑶⦙ `.صوره وقتيه`\n**🇮🇶 : يضع لك الوقت لمزخرف في صورتك تغير تلقائي -**\n\n\n⑷⦙ `.ايقاف + الامر الوقتي`\n**🇮🇶 : الامر الوقتي يعني حط بداله الامر الي ستعملته للوقت كمثال -  .ايقاف اسم وقتي او .ايقاف نبذه وقتيه او .ايقاف صوره وقتي -**\n✛━━━━━━━━━━━━━✛\n** ♰ ﻣطوࢪ اެلسۅࢪس :** {my_mention} "
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order14")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺    الاوامر المتحركه للتسلية   𖡺  :**\n\n✛━━━━━━━━━━━━━✛ \n\n `.غبي`\n`.تفجير`\n`.قتل`\n`.طوبه`\n`.مربعات`\n`.حلويات`\n`.نار`\n`.هلكوبتر`\n`.اشكال مربع`\n`.دائره`\n`.قلب `\n`.مزاج`\n`.قرد`\n`.ايد`\n`.العد التنازلي`\n`.الوان قلوب`\n`.عين`\n`.ثعبان`\n`.رجل`\n`.رموز شيطانيه`\n`.قطار`\n`.موسيقى`\n`.رسم`\n`.فراشه`\n`.مكعبات`\n`.مطر`\n`.تحركات`\n`.ايموجيات`\n`.طائره`\n`.شرطي`\n`.النضام الشمسي`\n`.افكر`\n`.اضحك`\n`.ضايج`\n`.ساعه متحركه`\n`.بوسه`\n`.قلوب`\n`.رياضه`\n`.الارض`\n`.قمر`\n`.اقمار`\n`.قمور`\n`.زرفه`\n`.بيبي`\n`.تفاعلات`\n`.اخذ قلبي`\n`.اشوفج السطح`\n`.احبك`\n`.اركض`\n`.روميو`\n`.البنك`\n`.تهكير + الرد على شخص`\n`.طياره`\n`.مصاصه`\n`.مصه`\n`.جكه`\n`.اركضلي`\n✛━━━━━━━━━━━━━✛\n**"
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ordvars")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺  اوامـر الـفـارات  𖡺 :**\n\n✛━━━━━━━━━━━━━✛ \n⑴ ⦙ `.اضف فار + اسم افار + القيمه`\n**🇮🇶 :  يضيف اليك الفار الخاص بسورس -**\n⑵ ⦙ `.حذف فار + اسم الفار`\n**🇮🇶 :  يحذف الفار الذي اضفته -**\n⑶  ⦙ `.جلب فار + اسم الفار`\n**🇮🇶 :  يرسل اليك معلومات الفار وقيمه الفار -**\n✛━━━━━━━━━━━━━✛\n\n**☣️  𖡺  1  الــفــارات  𖡺  :**\n\n**⑴ ⦙  لأضـافة فار كليشة حماية  الخاص للأضـافـة  ارسـل  :**\n`.اضف فار PM_TEXT + كليشة الحمايه الخاصة بـك`\n\n**⑵  ⦙ لأضـافة فار  ايدي الكـروب للأضافة أرسل بالرسائل محفوضة : **\n`.اضف فار PM_LOGGER_GROUP_ID  + ايدي مجموعتك`\n\n**⑶  ⦙ لأضـافة فار الايمـوجي  : **\n`.اضف فار ALIVE_EMOJI + الايموجي`\n\n **⑷  ⦙ لأضـافة فار  رسـاله بداية أمر السورس  : **\n `.اضف فار ALIVE_TEXT + النص`\n\n**⑸  ⦙  لأضـافة فار صورة رساله حماية  الخاص :**\n `.اضف فار PM_PIC + رابط تليجراف الصورة او الفيديو`\n\n **⑹ ⦙  لأضافـة فار صورة او فيديو أمر  السـورس : **\n `.اضف فار ALIVE_PIC + رابط تليجراف الصورة او الفيديو`\n\n **🇮🇶 : لشـرح كيفيـة جلـب رابط الصـورة او فيديو :**\n`.تليجراف ميديا + الرد على صورة او فيديو`\n\n ✛━━━━━━━━━━━━━✛\n\n**⑺ ⦙  لتغير كليشة الفحص كاملة :**\n`.اضف فار ALIVE_TELETHONIQ + كليشه مع المتغيرات`\n\n**🇮🇶 : متغيرات كليشه الفحص  :**\n\n1 -  :  `{uptime}` :  مده التشغيل بوتك \n2 -  :  `{my_mention}`  : رابط حسابك  \n3 -  :  `{TM}`  : الوقت \n4 -  :  `{ping} ` : البنك \n5 -  : ` {telever} ` : نسخه تليثون \n6 -  :  `{tg_bot}` :  معرف بوتك \n 🇮🇶︙ يوجد شرح مفصل عن الامر هنا : @teamtelethon \n✛━━━━━━━━━━━━━✛ \n⑻ ⦙ `.اضف فار AUTO_PIC + رابط صورة تليجراف`\n**🇮🇶 :  يضيف اليك الفار للصوره الوقتيه -**\n\n⑼ ⦙ `.اضف فار MAX_FLOOD_IN_PMS + العدد`\n**🇮🇶 :  يضيف اليك الفار تغير عدد تحذيرات رساله حمايه الخاص -**\n\n⑽ ⦙ `.اضف فار DEFAULT_BIO + الجمله`\n**🇮🇶 :  يضيف اليك الفار تغير جمله النبذه الوقتية  -**\n\n" 
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"hsb1")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺   اوامر الحساب 1   𖡺  :** \n\n✛━━━━━━━━━━━━━✛ \n\n ⑴  ⦙ `.معرفه + الرد ع الشخص` \n**🇮🇶 : سيجلب لك معرف الشخص -** \n ✛━━━━━━━━━━━━━✛ \n⑵  ⦙ `.سجل الاسماء + الرد ع الشخص` \n**🇮🇶 : يجلب لك اسماء الشخص القديمه -** \n ⑶  ⦙ `.انشاء بريد` \n**🇮🇶 : ينشئ لك بريد وهمي مع رابط رسائل التي تأتي الى البريد -** \n ✛━━━━━━━━━━━━━✛ \n⑷  ⦙ `.ايدي + الرد ع الشخص` \n**🇮🇶 : سيعطيك معلومات الشخص -** \n ✛━━━━━━━━━━━━━✛ \n⑸  ⦙ `. الايدي الرد ع الشخص` \n**🇮🇶 : سوف يعطيك ايدي المجموعه او ايدي حسابك -**\n ✛━━━━━━━━━━━━━✛ \n⑹ ⦙ `.معلومات تخزين المجموعه` \n**🇮🇶 : يجلب لك جميع معلومات الوسائط والمساحه وعدد ملصقات وعدد تخزين -**\n✛━━━━━━━━━━━━━✛\n⑺ ⦙ `.تخزين الخاص تشغيل`\n**🇮🇶 : يجلب لك جميع الرسائل التي تأتي اليك في الخاص -**\n⑻ ⦙ . تخزين الخاص ايقاف \n🇮🇶 : يوقف ارسال جميع الرسائل التي تأتي اليك في الخاص -\n✛━━━━━━━━━━━━━✛ \n\n⑼ ⦙ .تخزين الكروبات تشغيل\n🇮🇶 : يرسل لك جميع الرسائل التي يتم رد عليها في رسالتك في الكروبات -\n⑽ ⦙ .تخزين الكروبات ايقاف\n🇮🇶 : يوقف لك جميع ارسال الرسائل التي يتم رد عليها -**\n✛━━━━━━━━━━━━━✛\n\n"
    buttons = [[Button.inline("اوامر الحساب 2", data="hsb2"),],[Button.inline("اوامر الحساب 3", data="hsb3"),],[Button.inline("اوامر الحساب 4", data="hsb4"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"hsb2")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺   اوامر الحساب 2   𖡺  :**\n\n✛━━━━━━━━━━━━━✛ \n\n ⑴  ⦙  `.صورته + الرد ع الشخص`\n**🇮🇶 : يجلب صوره الشخص الذي تم رد عليه -**\n \n⑵  ⦙ `.رابطه + الرد ع الشخص`\n**🇮🇶 :  يجلب لك رابط الشخص الذي تم رد عليه  -**\n\n⑶  ⦙ `.اسمه + الرد ع الشخص`\n**🇮🇶 : يجلب لك اسم الشخص الذي تم رد عليه -**\n\n✛━━━━━━━━━━━━━✛\n⑷  ⦙  `.نسخ + الرد ع الرساله`\n**🇮🇶 : يرسل الرساله التي تم رد عليها -**\n\n✛━━━━━━━━━━━━━✛ \n⑸  ⦙ `.كورونا + اسم المدينه`\n**🇮🇶 : يجلب لك مرض كورونا وعدد الموتى والمصابين**-\n✛━━━━━━━━━━━━━✛ \n⑹ ⦙ `.الاذان +اسم المدينه`\n**🇮🇶 : يجلب لك معلومات الاذان في هذهّ المدينه بجميع الاوقات -**\n\n✛━━━━━━━━━━━━━✛ \n⑺ ⦙ `.رابط تطبيق + اسم التطبيق`\n**🇮🇶 : يرسل لك رابط التطبيق مع معلوماته -**\n\n⑻ ⦙ `.تاريخ الرساله + الرد ع الرساله`\n**🇮🇶 : يجلب لك تاريخ الرساله بالتفصيل -**\n✛━━━━━━━━━━━━━✛ \n⑼ ⦙ `.بنك`\n**🇮🇶 : يقيس سرعه استجابه لدى تنصيبك -**\n\n✛━━━━━━━━━━━━━✛ \n⑽ ⦙ `.سرعه الانترنيت`\n**🇮🇶 : يجلب لك سرعه الانترنيت لديك -**\n\n⑾ ⦙ `.الوقت`\n**🇮🇶 : يضهر لك الوقت والتاريخ واليوم -**\n\n✛━━━━━━━━━━━━━✛ \n⑿ ⦙  `.وقتي`\n**🇮🇶 : يضهر لك الوقت والتاريخ بشكل جديد -**\n"
    buttons = [[Button.inline("اوامر الحساب 1", data="hsb1"),],[Button.inline("اوامر الحساب 3", data="hsb3"),],[Button.inline("اوامر الحساب 4", data="hsb4"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"hsb3")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺  اوامر الحساب  3     𖡺  :**\n\n✛━━━━━━━━━━━━━✛\n\n⑴ ⦙ `.حالتي `\n**🇮🇶  :  لفحص الحظر**\n⑵  ⦙ `.طقس + اسم المدينه `\n**🇮🇶 : يعطي لك طقس المدينه **\n✛━━━━━━━━━━━━━✛ \n\n⑶  ⦙  `.طقوس + اسم المدينه `\n**🇮🇶 : يعطي لك طقس المدينه ل 3 ايام قادمه **\n⑷  ⦙  `.مدينه الطقس + اسم المدينه `\n**🇮🇶 : لتحديد طقس المدينه تلقائي عند ارسال الأمر **\n✛━━━━━━━━━━━━━✛ \n\n⑸  ⦙  `.ازاله التوجيه + الرد على رساله`\n**🇮🇶 : يرسل اليك الرساله التي تم رد عليها بدون توجيه حتى لو بصمه او صوره يقوم بالغاء التوجيه الخاص بها**\n⑹  ⦙ `.كشف + الرد على شخص`\n**🇮🇶 : رد على شخص يفحص حضر مستخدم**\n✛━━━━━━━━━━━━━✛ \n\n⑺ ⦙ `.وضع بايو + الرد على البايو`\n**🇮🇶 : يضع الكلمه التي تم رد عليها في البايو الخاص بك**\n⑻  ⦙ `.وضع اسم + الرد على الاسم`\n**🇮🇶 :  يضع الاسم الذي تم رد عليه في اسمك**\n⑼  ⦙ `.وضع صوره + الرد على صوره`\n**🇮🇶 :  يضع الصوره التي تم رد عليها في حسابك**\n✛━━━━━━━━━━━━━✛ \n\n⑽ ⦙ `.معرفاتي`\n** 🇮🇶 : يجلب جميع المعرفات المحجوزه  في حسابك **\n⑾ ⦙  `.تحويل ملكية + معرف الشخص`\n**🇮🇶 : يحول ملكيه القناه او المجموعه الى معرف**\n✛━━━━━━━━━━━━━✛ \n\n⑿ ⦙  `.انتحال + الرد على الشخص`\n**🇮🇶 :  ينتحل الشخص ويضع صورته و نبذته و اسمه في حسابك ( المعرف الخاص بك لايتغير ) **\n⒀ ⦙ `.الغاء الانتحال + الرد على الشخص`\n**🇮🇶 : يقوم بالغاء الانتحال ويرجع معلومات  المذكوره بالسورس **\n✛━━━━━━━━━━━━━✛ \n\n⒁  ⦙ `.ازعاج + الرد على شخص`\n**🇮🇶 :  يقوم بتكرار الرسائل للشخص المحدد من دون توقف اي شي يتكلمه حسابك همين يدزه**\n⒂ ⦙ `.الغاء الازعاج`\nشرح :  يوقف جميع الازعاجات في المجموعه \n✛━━━━━━━━━━━━━✛ \n\n ⒃  ⦙ `.المزعجهم`\n**🇮🇶 : يضهر اليك جميع الاشخاص الي بل مجموعه مفعل عليهم ازعاج وتكرر رسايلهم**\n\n"
    buttons = [[Button.inline("اوامر الحساب 1", data="hsb1"),],[Button.inline("اوامر الحساب 2", data="hsb2"),],[Button.inline("اوامر الحساب 4", data="hsb4"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"hsb4")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺  اوامر الحساب  4     𖡺  :**\n\n✛━━━━━━━━━━━━━✛\n\n⑴ ⦙  `.الحماية تشغيل`\n**🇮🇶 : يقوم بتشغيل رساله الحمايه في الخاص بحيث اي شخص يراسلك سوف يقوم بتنبيه بعدم تكرار وايضا يوجد ازرار اونلاين -**\n⑵  ⦙ `.الحماية ايقاف`\n**🇮🇶 :  يقوم بتعطيل رساله الحماية الخاص وعد تحذير اي شخص-**\n✛━━━━━━━━━━━━━✛\n\n⑶  ⦙ `.قبول`\n**🇮🇶 : يقوم بقبول الشخص للأرسال اليك بدون حظره -**\n ⑷  ⦙  `.رفض`\n**🇮🇶 :  الغاء قبول الشخص من الارسال وتحذيره ايضا-**\n✛━━━━━━━━━━━━━✛\n\n⑸  ⦙ `.مرفوض`\n**🇮🇶 :  حظر الشخص من دون تحذير حظر مباشر م الخاص -**\n⑹  ⦙  `.المقبولين`\n**🇮🇶 :  عرض قائمة المقبولين في الحماية -**\n⑺ ⦙   `.جلب الوقتيه + الرد على الصورة`\n**🇮🇶 :  الرد على صوره سريه وقتيه سوف يتم تحويلها الى رسائل المحفوضه كصورة عادية -**\n✛━━━━━━━━━━━━━✛\n\n⑻  ⦙  `.تاك بالكلام + الكلمه + معرف الشخص`\n**🇮🇶:  يسوي تاك للشخص بالرابط جربه وتعرف -**\n⑼  ⦙ `.نسخ + الرد على رساله`\n**🇮🇶:  يرسل الرساله التي رديت عليها -**\n✛━━━━━━━━━━━━━✛\n\n⑽ ⦙  `.احسب + المعادله`\n**🇮🇶:  يجمع او يطرح او يقسم او يجذر المعادله الأتية -**\n\n"
    buttons = [[Button.inline("اوامر الحساب 1", data="hsb1"),],[Button.inline("اوامر الحساب 2", data="hsb2"),],[Button.inline("اوامر الحساب 3", data="hsb3"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ord1hs")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺   اوامر الحساب   𖡺  :**"
    buttons = [[Button.inline("اوامر الحساب  1", data="hsb1"),],[Button.inline("اوامر الحساب 2", data="hsb2"),],[Button.inline("اوامر الحساب 3", data="hsb3"),],[Button.inline("اوامر الحساب 4", data="hsb4"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.on(admin_cmd(pattern="usage(?: |$)(.*)"))    
async def dyno_usage(dyno):
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await edit_delete(dyno, "Set the required vars in heroku to function this normally `HEROKU_API_KEY` and `HEROKU_APP_NAME`.",)
    dyno = await edit_or_reply(dyno, "`Processing...`")
    useragent = ("Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36")
    user_id = Heroku.account().id
    headers = {"User-Agent": useragent, "Authorization": f"Bearer {Config.HEROKU_API_KEY}", "Accept": "application/vnd.heroku+json; version=3.account-quotas"}
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("`Error: something bad happened`\n\n" f">.`{r.reason}`\n")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    return await dyno.edit(f"**Dyno Usage**:\n\n -> `Dyno usage for`  **{Config.HEROKU_APP_NAME}**:\n  •  `{AppHours}`**h**  `{AppMinutes}`**m** **|**  [`{AppPercentage}`**%**] \n\n  -> `Dyno hours quota remaining this month`:\n •  `{hours}`**h**  `{minutes}`**m|**  [`{percentage}`**%**]")
@iqthon.on(admin_cmd(pattern="(herokulogs|logs)(?: |$)(.*)"))    
async def _(dyno):
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await edit_delete(dyno, "Set the required vars in heroku to function this normally `HEROKU_API_KEY` and `HEROKU_APP_NAME`.")
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await dyno.reply( " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku")
    data = app.get_log()
    await edit_or_reply(dyno, data, deflink=True, linktext="**Recent 100 lines of heroku logs: **")
def prettyjson(obj, indent=2, maxlinelength=80):
    items, _ = getsubitems(        obj,        itemkey="",        islast=True,        maxlinelength=maxlinelength - indent,        indent=indent,    )
    return indentitems(items, indent, level=0)
@iqthon.on(admin_cmd(pattern="استخدامي$"))
async def psu(event):
    uname = platform.uname()
    cpufreq = psutil.cpu_freq()
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu = "**حجم استخدامك لتليثون :**\n"
    cpuu += f"الاستخدام : `{psutil.cpu_percent()}%`\n"
    svmem = psutil.virtual_memory()
    help_string = f"{str(cpuu)}\n"
    await event.edit(help_string)
@iqthon.on(admin_cmd(pattern="سرعه الانترنيت(?:\s|$)([\s\S]*)"))    
async def _(event):
    input_str = event.pattern_match.group(1)
    as_text = False
    as_document = False
    if input_str == "image":
        as_document = False
    elif input_str == "file":
        as_document = True
    elif input_str == "text":
        as_text = True
    catevent = await edit_or_reply(event, "**🇮🇶︙   جـاري حسـاب سرعـه الانـترنيـت لـديك  🔁**")
    start = time()
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    end = time()
    ms = round(end - start, 2)
    response = s.results.dict()
    download_speed = response.get("download")
    upload_speed = response.get("upload")
    ping_time = response.get("ping")
    client_infos = response.get("client")
    i_s_p = client_infos.get("isp")
    i_s_p_rating = client_infos.get("isprating")
    reply_msg_id = await reply_id(event)
    try:
        response = s.results.share()
        speedtest_image = response
        if as_text:
            await catevent.edit(                """**🇮🇶︙   حسـاب سرعـه الانـترنيـت لـديك  📶 : {} ثانية**
**🇮🇶︙   التنزيل 📶 :** `{} (or) {} ميغا بايت`
**🇮🇶︙   الرفع 📶 :** `{} (or) {} ميغا بايت`
**🇮🇶︙   البنك :** {}` بالثانية`
**🇮🇶︙   مزود خدمة الإنترنت 📢 :** `{}`
**🇮🇶︙   تقيم الانترنيت :** `{}`""".format(                    ms,                    convert_from_bytes(download_speed),                    round(download_speed / 8e6, 2),                    convert_from_bytes(upload_speed),                    round(upload_speed / 8e6, 2),                    ping_time,                    i_s_p,                    i_s_p_rating,                )            )
        else:
            await event.client.send_file(                event.chat_id,                speedtest_image,                caption="**قياس السرعه اكتمل في غضون  `{}`  ثواني **".format(ms),                force_document=as_document,                reply_to=reply_msg_id,                allow_cache=False,            )
            await event.delete()
    except Exception as exc:
        await catevent.edit(            
"""**🇮🇶︙   حسـاب سرعـه الانـترنيـت لـديك  📶 : {} ثانية**
**🇮🇶︙   التنزيل 📶:** `{} (or) {} ميغا بايت`
**🇮🇶︙   الرفع 📶:** `{} (or) {} ميغا بايت`
**🇮🇶︙   البنك :** {}` بالثانية`
**🇮🇶︙  مع الأخطاء التالية :** {}""".format(                ms,                convert_from_bytes(download_speed),                round(download_speed / 8e6, 2),                convert_from_bytes(upload_speed),                round(upload_speed / 8e6, 2),                ping_time,                str(exc),            )        )
if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("تنانصيب") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.url("1- شرح التنصيب", "https://youtu.be/44tYK_yV02Q"), Button.url("2- استخراج ايبيات", "https://my.telegram.org/"),],[Button.url("3- ستخراج تيرمكس", "https://replit.com/@telethon-Arab/generatestringsession#start.sh"), Button.url("4- بوت فاذر", "http://t.me/BotFather"),],[Button.url("5- رابط التنصيب", "https://dashboard.heroku.com/new?template=https://github.com/telethon-Arab/telethohelp"),],[Button.url("المطـور 👨🏼‍💻", "https://t.me/LLL5L"),]]
            if IQTHONPC and IQTHONPC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(IQTHONPC, text=help1, buttons=buttons, link_preview=False)
            elif IQTHONPC:
                result = builder.document(IQTHONPC,title="iqthon",text=help1,buttons=buttons,link_preview=False)
            else:
                result = builder.article(title="iqthon",text=help1,buttons=buttons,link_preview=False)
            await iqthon.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="تنصهفيب"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "تنتعصيب")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"play1")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺   اوامر الالعاب 1   𖡺  :**\n\n✛━━━━━━━━━━━━━✛ \n**⑴  ⦙  نسب وهميه :**\n`.نسبه الحب + الرد ع الشخص`\n`. نسبه الانحراف + الرد ع الشخص `\n`.نسبه الكراهيه + الرد ع الشخص`\n`.نسبه المثليه +الرد ع الشخص`\n`. نسبه النجاح + الرد ع الشخص`\n`.نسبه الانوثه + الرد ع الشخص `\n`.نسبه الغباء + الرد ع الشخص`\n✛━━━━━━━━━━━━━✛ \n**⑵  ⦙  رفع وهمي :**\n`.رفع زباله + الرد ع الشخص `\n`.رفع منشئ + الرد ع الشخص `\n`.رفع مدير + الرد ع الشخص`\n`.رفع مطور + الرد ع الشخص` \n`.رفع مثلي + الرد ع الشخص` \n`.رفع كواد + الرد ع الشخص` \n`.رفع مرتبط + الرد ع الشخص` \n`.رفع مطي + الرد ع الشخص` \n`.رفع كحبه + الرد ع الشخص` \n`.رفع زوجتي + الرد ع الشخص` \n`.رفع صاك + الرد ع الشخص` \n`.رفع صاكه + الرد ع الشخص`\n✛━━━━━━━━━━━━━✛\n⑶  ⦙ `.كت`\n**🇮🇶 : لعبه اسأله كت تويت عشوائيه -**\n⑷  ⦙ `.اكس او` \n**🇮🇶 :  لعبه اكس او دز الامر و اللعب ويا صديقك -**\n⑸  ⦙  `.همسه + الكلام + معرف الشخص` \n**🇮🇶 : يرسل همسه سريه الى معرف الشخص فقط هو يكدر يشوفها  -**\n"
    buttons = [[Button.inline("اوامر الالعاب  2", data="play2"),],[Button.inline("اوامر الالعاب  3", data="play3"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"play2")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺   اوامر الالعاب 2   𖡺  :**\n\n✛━━━━━━━━━━━━━✛ \n**⑻ ⦙ `.رسم شعار + الاسم` \n**🇮🇶 : يرسم شعار للأسم  -**\n⑼ ⦙ `.نص ثري دي + الكلمه`\n**🇮🇶 : يقوم بكتابه الكلمه بشكل ثلاثي الابعاد~  -**\n⑽ ⦙ `.كلام متحرك + الكلام`\n**🇮🇶 : يقوم بكتابه الكلام حرف حرف  -**\n⑾  ⦙  `.ملصق متحرك + الكلام`\n**🇮🇶 : يقوم بكتابه الكلام بملصق متحرك  -**\n⑿ ⦙  `.بورن + معرف الشخص + الكلام + الرد ع اي صوره`\n**🇮🇶 :  قم بتجربه الامر لتعرفه +18  -**\n⒀ ⦙ `.رسم قلوب + الاسم`\n**🇮🇶 : يكتب الاسم ع شكل قلوب  -**\n\n✛━━━━━━━━━━━━━✛\n"
    buttons = [[Button.inline("اوامر الالعاب 1", data="play1"),],[Button.inline("اوامر الالعاب  3", data="play3"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"play3")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺  اوامر الالعاب 3  𖡺  :**\n\n⑴  ⦙  `.كتابه وهمي + عدد الثواني`\n\n⑵  ⦙  `.فيديو وهمي + عدد الثواني`\n\n⑶  ⦙  `.صوره وهمي + عدد الثواني`\n\n⑷  ⦙  `.جهه اتصال وهمي + عدد الثواني`\n\n⑸  ⦙  `.موقع وهمي + عدد الثواني`\n\n⑹  ⦙  `.لعب وهمي + عدد الثواني`\n\n\n**شرح :  هذا الامر يقوم بالارسال الوهمي يعني يضهر للناس انو نته جاي تكتب او جاي ترسل صوره او ترسل فيديو او ترسل جهه اتصالك حسب الفتره الي تحددها بالثواني**"
    buttons = [[Button.inline("اوامر الالعاب 1", data="play1"),],[Button.inline("اوامر الالعاب  2", data="play2"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)


@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ord1pl")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺   اوامر الالعاب   𖡺  :**"
    buttons = [[Button.inline("اوامر الالعاب  1", data="play1"),],[Button.inline("اوامر الالعاب 2", data="play2"),],[Button.inline("اوامر الالعاب 3", data="play3"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)


@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"shag1")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺  1 اوامر تحويل الصيغ  𖡺  :**\n\n✛━━━━━━━━━━━━━✛ \n⑴  ⦙  `.تحويل بصمه + الرد ع الصوت mp3`\n**🇮🇶 : يحول صوت mp3 الى بصمه -**\n⑵  ⦙  `.تحويل صوت + الرد ع الصوت` \n**🇮🇶 :  يحول البصمه الى صوت   mp3**\n✛━━━━━━━━━━━━━✛\n⑶  ⦙  `.تحويل ملصق + الرد ع الصوره` \n**🇮🇶 :  يحول الصوره الى ملصق -**\n⑷  ⦙ `. تحويل صوره + الرد ع الملصق` \n**🇮🇶 :  يحول الملصق الى صوره -**\n✛━━━━━━━━━━━━━✛ \n⑸  ⦙  `.تحويل متحركه + الرد ع الفيديو` \n**🇮🇶 :  يقوم بتحويل الفيديو الى متحركه -**\n✛━━━━━━━━━━━━━✛ \n⑹ ⦙  `.بي دي اف + الرد ع الملف او الصوره`\n**🇮🇶 :  يحول الملف او الصوره الى بي دي اف -**\n✛━━━━━━━━━━━━━✛ \n⑺ ⦙ `.ملصقي + الرد ع الرساله` \n**🇮🇶 : يحول رساله الى ملصق -**\n✛━━━━━━━━━━━━━✛\n⑻ ⦙  `. تليجراف ميديا + الرد ع الفيديو او صوره`\n **🇮🇶 :  يقوم بتحويل الفيديو او الصوره الى رابط تليجراف للأستخدام  -**\n⑼ ⦙  `.تحويل رساله + الرد ع الملف` \n**🇮🇶 :  يقوم بجلب جميع الكتابه الذي داخل الملف ويقوم بأرسالها اليك -**\n✛━━━━━━━━━━━━━✛\n⑽ ⦙ `.تحويل فديو دائري + الرد ع الفيديو`\n**🇮🇶 : يحول الفيديو الى فيديو دائري مرئي -**\n⑾  ⦙ `.تحويل ملصق دائري + الرد ع الملصق` \n**🇮🇶 :  يحول الملصق الى ملصق دائري** \n"
    buttons = [[Button.inline("اوامر تحويل الصيغ  2", data="shag2"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"shag2")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺  2 اوامر تحويل الصيغ   𖡺  :**\n\n✛━━━━━━━━━━━━━✛ \n ⑿ ⦙  `.ترجمه en + الرد ع الرساله` \n**🇮🇶 :  يقوم بترجمه الرساله الى اللغه الانكليزيه**\n⒀ ⦙ `.ترجمه ar + الرد ع الشخص` \n**🇮🇶 :  يقوم بترجمه الرساله الى اللغه العربيه -**\n✛━━━━━━━━━━━━━✛\n"
    buttons = [[Button.inline("اوامر تحويل الصيغ  1", data="shag1"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)


@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ordsag1")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺   اوامر الصيغ   𖡺  :**"
    buttons = [[Button.inline("اوامر الصيغ  1", data="shag1"),],[Button.inline("اوامر الصيغ 2", data="shag2"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.on(admin_cmd(pattern=f"{ORDERS}(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**قائمـه ﭑوامـر السـۅࢪس الخــاص بــك**
**✛━━━━━━━━━━━━━✛**
(`.م1`) - ﭑوامࢪ اެلسورس ♰
(`.م2`) - ﭑوامࢪ اެلحساب ♰
(`.م3`) -  ﭑوامࢪ اެلمجموعهہَ ♰
(`.م4`) - ﭑوامࢪ اެلمجموعهہَ ² ♰
(`.م5`) - ﭑوامࢪ اެلصيغہَ ۅ اެلجهات ♰
(`.م5`) - حمايهہَ خاصہَ ولتلڪࢪاف ♰
(`.م6`) - ﭑوامࢪ اެلألعاب ♰
(`.م7`) - ﭑوامࢪ اެلميمز ♰
(`.م8`) - ﭑوامࢪ اެلتسليه ۅ اެلتحشيش ♰
(`.م9`) - ﭑوامࢪ اެلوقتيہَ ۅ اެلتشغيلہَ ♰
(`.م10`) - ﭑوامࢪ اެلفارات ♰
(`.م11`) - ﭑوامࢪ اެلسوبرات ♰
(`.م12`) - ﭑوامࢪ اެلأغاني ♰
(`.م13`) - ﭑوامࢪ اެلتكرار ♰
(`.م14`) - ﭑوامࢪ اެلزخرفة ♰
(`.م15`) - ﭑوامࢪ اެلوسائط ♰
(`.م16`) - ﭑوامࢪ اެلملصقات ♰ 
**✛━━━━━━━━━━━━━✛**
** ♰ ﻣطوࢪ اެلسۅࢪس :** {my_mention}

""")
@iqthon.on(admin_cmd(pattern="م9(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**𖡺   اوامر الوقتي   𖡺  :**
✛━━━━━━━━━━━━━✛
 الأمر  ⦙ ( .اسم وقتي )
الشرح : يضع الوقت المزخرف في اسمك تلقائيا 
✛━━━━━━━━━━━━━✛
 الأمر  ⦙ ( .نبذه وقتيه )
الشرح  : يضع الوقت المزخرف في نبذه الخاصه بك تلقائيا
✛━━━━━━━━━━━━━✛
الأمر ⦙ ( .صوره وقتيه )
الشرح : يضع لك الوقت لمزخرف في صورتك تغير تلقائي 
✛━━━━━━━━━━━━━✛
**شرح الايقاف :**
( .ايقاف صوره وقتيه )
( .ايقاف نبذه وقتيه )
( .ايقاف اسم وقتي )
✛━━━━━━━━━━━━━✛
 ** ♰ ﻣطوࢪ اެلسۅࢪس :** {my_mention}
""")
@iqthon.on(admin_cmd(pattern="م10(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
""" ( اوامر الفارات وتغيرات ) :
✛━━━━━━━━━━━━━✛
¹ ⦙  لتغير كليشة الفحص والسورس  كاملة : 

`.اضف فار ALIVE_TELETHONIQ` + كليشه مع المتغيرات 

🇮🇶 : متغيرات كليشه الفحص والسورس   : 

1 -  :  {uptime} :  مده التشغيل بوتك 
2 -  :  {my_mention}  : رابط حسابك  
3 -  :  {TM}  : الوقت 
4 -  :  {ping}  : البنك 
5 -  :  {telever}  : نسخه تليثون 
6 -  :  {tg_bot} :  معرف بوتك 

✛━━━━━━━━━━━━━✛ 

² ⦙ لتغيير صوره أو فيديو أم الفحص والسورس : 

`.اضف فار ALIVE_PIC` + رابط تليجراف الصورة او الفيديو 

للحصول على تيلجراف للصورة : .تليجراف ميديا + الرد على الصورة أو الفيديو 

✛━━━━━━━━━━━━━✛ 

³ ⦙ لتغير كليشه رسالة حماية الخاص : 

`.اضف فار PM_TEXT` + الكليشة 

1 - {mention} يكتب اسم الشخص
2 - {warns}/{totalwarns} لـ عدد التحذيرات 

✛━━━━━━━━━━━━━✛ 

⁴ ⦙ لتغيير أو اضافة صورة الى حماية الخاص : 

`.اضف فار PM_PIC` + رابط تليجراف الصورة او الفيديو 

امر تحويل الصورة والفيديو لرابط :  `.تليجراف ميديا` 

✛━━━━━━━━━━━━━✛ 

⁵ ⦙ لتغير عدد التحذيرات برسالة الحماية الخاص : 

`.اضف فار MAX_FLOOD_IN_PMS` + العدد 

✛━━━━━━━━━━━━━✛ 

⁶ ⦙ لوضع نبذة وقتية :

- أرسل :  `.اضف فار DEFAULT_BIO` + الجمله
- أرسل :  `.تحديث` 

✛━━━━━━━━━━━━━✛ 

⁷ ⦙ تغير الصوره الوقتية : 

`.اضف فار AUTO_PIC` + رابط صورة 

للحصول على تيلجراف للصورة : `.تليجراف ميديا` + الرد على الصورة أو الفيديو 

- أرسل ( ` .تحديث` ) 

✛━━━━━━━━━━━━━✛ 

⁸ ⦙ لتغير خط الوقت في الاسم الوقتي و النبذه الوقتية : 

1 - لأضـافة هـذا الخط : ( 𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗 ) 
أرسـل ⇦ ( `.اضف فار FONTS_AUTO font1` ) 

2 - لأضـافة هـذا الخط : ( 𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵 ) 
أرسـل ⇦ (`.اضف فار FONTS_AUTO font2` ) 

3 - لأضـافة هـذا الخط : (０１２３４５６８９) 
أرسـل ⇦ ( `.اضف فار FONTS_AUTO font3` ) 

4 - لأضـافة هـذا الخط : ( 𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘 ) 
أرسـل ⇦ ( `.اضف فار FONTS_AUTO font4` ) 

5 - لأضـافة هـذا الخط : ( 𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫 ) 
أرسـل ⇦ ( `.اضف فار FONTS_AUTO font5` ) 

6 - لأضـافة هـذا الخط : ( ①②③④⑤⑥⑦⑧⑨⓪ )
أرسـل ⇦  ( `.اضف فار FONTS_AUTO font6` ) 

7 - لأضـافة هـذا الخط : ( ❶❷❸❹❺❻❼❽❾⓿ )
أرسـل ⇦  ( `.اضف فار FONTS_AUTO font7` ) 

8 - لأضـافة هـذا الخط : ( 0123456789 )
أرسـل ⇦  ( `.اضف فار FONTS_AUTO font8` ) 

9 - لأضـافة هـذا الخط : ( ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ ₀ )
أرسـل ⇦  ( `.اضف فار FONTS_AUTO font9` ) 

10 - لأضـافة هـذا الخط : ( 𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿 )
أرسـل ⇦   (`.اضف فار FONTS_AUTO font10`) 

11 - لأضـافة هـذا الخط : ( ١٢٣٤٥٦٧٨٩٠ )
أرسـل ⇦  ( `.اضف فار FONTS_AUTO font11` ) 

✛━━━━━━━━━━━━━✛ 

⁹ ⦙ لتغير الايموجي بالسورس و ايضا رمز الذي بجانب الوقتي : 

`.اضف فار ALIVE_EMOJI` + الايموجي 

✛━━━━━━━━━━━━━✛
** ♰ ﻣطوࢪ اެلسۅࢪس :** {my_mention}
""")
@iqthon.on(admin_cmd(pattern="م11(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""** 𖡺  اوامر السوبرات  𖡺  :**
✛━━━━━━━━━━━━━✛
 الأمر  ⦙ .مؤقته + الوقت بالثواني + رساله
الشرح :  يرسل الرساله لمده معينه ويحذفها بس يخلص المده
✛━━━━━━━━━━━━━✛
 الأمر  ⦙ .للكروب + الرد على الرساله
الشرح :  يرسل الرسالها الى جميع المجموعات
✛━━━━━━━━━━━━━✛
 الأمر  ⦙ ( .مؤقت + عدد ثواني + عدد الرسائل + كليشة )
الشرح :  يقوم بارسال نشر تلقائي للسوبرات 
✛━━━━━━━━━━━━━✛
الأمر  ⦙  ( .ستوب )
الشرح  ⦙  ايقاف النشر التلقائي المؤقت
✛━━━━━━━━━━━━━✛
 الأمر  ⦙ .اضافه + رابط الكروب
الشرح :   يضيفلك جميع الاعضاء الي برابط الكروب يضيفهم بكروبك 
 ✛━━━━━━━━━━━━━✛
ﻣطوࢪ اެلسۅࢪس :** {my_mention}
""")
@iqthon.on(admin_cmd(pattern="م12(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""** 𖡺   اوامر  الاغاني. 𖡺  : **
✛━━━━━━━━━━━━━✛
الأمر  ⦙ .بحث صوت + اسم الاغنيه
الشرح : سيحمل لك الاغنية صوت ايضا يمكنك وضع رابط الاغنيه بدل الاسم 
✛━━━━━━━━━━━━━✛ 
 الأمر  ⦙ .بحث فيديو + اسم الاغنيه 
الشرح : سيحمل لك الاغنية  فيديو ايضا يمكنك وضع رابط الاغنيه بدل الاسم 
✛━━━━━━━━━━━━━✛ 
 الأمر  ⦙ .معلومات الاغنيه 
الشرح : الرد ع الاغنيه سيجلب لك معلوماتها واسم الفنان 
✛━━━━━━━━━━━━━✛
الأمر  ⦙ .كوكل بحث + موضوع البحث
الشرح : يجلب لك معلومات الموضوع من كوكل 
✛━━━━━━━━━━━━━✛
الأمر  ⦙ .تخزين الصوت + الرد ع البصمه
الشرح  : تخزين الصوت من اجل استخدامه لوضع صوت في الفيديو 
✛━━━━━━━━━━━━━✛
الأمر  ⦙ .اضف الصوت + الرد ع الصوره او متحركه او فيديو
الشرح  : يتم اضافه الصوت الى الفيديو او المتحركه او الصوره 
✛━━━━━━━━━━━━━✛ 
الأمر  ⦙ .اسم الاغنيه + الرد ع الاغنيه
الشرح  : ييجلب لك اسم الاغنيه مدة البصمه 10 الى 5 ثواني 
✛━━━━━━━━━━━━━✛
الأمر  ⦙ ( .تيك توك + الرد ع رابط الفيديو )
الشرح : يحمل فيديو تيك توك بدون العلامه المائيه 
✛━━━━━━━━━━━━━✛
ﻣطوࢪ اެلسۅࢪس :** {my_mention}
""")
@iqthon.on(admin_cmd(pattern="م13(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
""" **𖡺   اوامر التكرار    𖡺  : **
✛━━━━━━━━━━━━━✛ 
الشرح  ⦙ ( .تكرار + الكلمة + العدد )
الأمر :  يرسل الكلمة يكررها على عدد المرات  
✛━━━━━━━━━━━━━✛  
الأمر ⦙ ( .تكرار حزمه الملصقات + الرد على ملصق )
الشرح :   يرسل لك جميع ملصقات الموجوده في حزمه لل الملصق الي عملت رد له   
✛━━━━━━━━━━━━━✛
الأمر  ⦙ ( .تكرار_احرف  + الكلمة )
الشرح :   يكرر الك احرف الكلمة حتى لو جملة 
✛━━━━━━━━━━━━━✛
الأمر  ⦙ ( .تكرار_كلمه  + الجملة )
الشرح : يكرر الك كلام الجملة 
✛━━━━━━━━━━━━━✛ 
الأمر  ⦙ ( .مؤقت  + عدد الثواني + عدد مرات + الجملة )
الشرح : يرسل اليك الجملة كل وقت معين 
✛━━━━━━━━━━━━━✛
** ♰ ﻣطوࢪ اެلسۅࢪس :** {my_mention}
""")
@iqthon.on(admin_cmd(pattern="م14(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""** 𖡺   لأوامر الزخرفة   𖡺  : **
✛━━━━━━━━━━━━━✛
⑴  ⦙ .غمق + الرد على رساله 
🇮🇶 :  يحول خط الرسالة غامقه  
✛━━━━━━━━━━━━━✛ 
⑵  ⦙ .ينسخ + الرد على رساله 
🇮🇶 :  يحول خط الرساله الى كلام ينسخ  
✛━━━━━━━━━━━━━✛
⑶  ⦙ .خط سفلي + الرد على رساله 
🇮🇶 :   يضيف الى خط رساله خط سفلي 
✛━━━━━━━━━━━━━✛ 
⑷  ⦙ .كتابه + الكلام بالانكلش 
🇮🇶 : يكتب الكلام على ورقه بخط اليد 100% - 
 ✛━━━━━━━━━━━━━✛ 
⑸  ⦙ .زخرفه_انكليزي + الاسم 
🇮🇶 : يزخرف الاسم الانكليزي لعده زخرفات يجب ان يكون الاسم مكتوب سمول 
✛━━━━━━━━━━━━━✛
⑹ ⦙ .زخرفه_عربي + الاسم 
🇮🇶 : يزخرف الاسم العربي لعده زخرفات 
✛━━━━━━━━━━━━━✛
⑺ ⦙  .بايوهات1
🇮🇶 :  يعطيك بايو انستا متعدده 1 
✛━━━━━━━━━━━━━✛
⑻ ⦙ .بايوهات2
🇮🇶 :  يعطيك بايو انستا متعدده 2 
✛━━━━━━━━━━━━━✛
⑼ ⦙  .رموز1
🇮🇶 :  يعطيك رموز للزخرفه 1 
✛━━━━━━━━━━━━━✛
 10 ⦙ .رموز2
🇮🇶 :  يعطيك رموز للزخرفه2 
✛━━━━━━━━━━━━━✛
** ♰ ﻣطوࢪ اެلسۅࢪس :** {my_mention}
""")



@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ordahln1")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺  اوامر الاعلانات   𖡺  :**\n\n✛━━━━━━━━━━━━━✛ \n ⑴  ⦙ `.مؤقته + الوقت بالثواني + رساله`\n**🇮🇶 :  يرسل الرساله لمده معينه ويحذفها بس يخلص المده**\n ⑵  ⦙ `.للكروبات + الرد على الرساله`\n**🇮🇶 :  يرسل الرسالها الى جميع المجموعات**\n✛━━━━━━━━━━━━━✛ \n ⑶  ⦙ `.مؤقت + عدد ثواني + عدد الرسائل + كليشة` \n**🇮🇶 :  يقوم بارسال رساله وقتيه محدده لكل وقت معين وعدد مرات معين**\n\n ⑷  ⦙ `.اضافه + رابط الكروب`\n🇮🇶 :   يضيفلك جميع الاعضاء الي برابط الكروب يضيفهم بكروبك \n يجب ان تتاكد انو مامحضور حسابك ارسل  ⬅️ ( `.حالتي` ) \n علمود تتاكد محضور الحساب لو لا الاضافات الكثيره تحظر مؤقتا  \n"
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("اوامر الاعلانات(?: |$)(.*)") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الاعلانات", data="ordahln1"),]]
            result = builder.article(title="iqthon", text=help2, buttons=buttons, link_preview=False)
            await iqthon.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="اوامر الاعلانات(?: |$)(.*)"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "اوامر الاعلانات(?: |$)(.*)")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()
@iqthon.on(admin_cmd(pattern="م15(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**𖡺   اوامر الوسائـط   𖡺  :**
✛━━━━━━━━━━━━━✛
⑴ ⦙ .سمول + الرد على ملصق او صوره او فيديو 
🇮🇶  : يقوم بتصغير الوسائط 
✛━━━━━━━━━━━━━✛
⑵ ⦙ .عكس الالوان + الرد على ملصق او صوره او فيديو
🇮🇶  : يعكس الالوان الموجودة في الوسائط
✛━━━━━━━━━━━━━✛
⑶ ⦙ .فلتر احمر + الرد على ملصق او صوره او فيديو
🇮🇶  : يقوم باضافه فلتر احمر الى وسائط
✛━━━━━━━━━━━━━✛
⑷ ⦙ .فلتر رصاصي + الرد على ملصق او صوره او فيديو
🇮🇶  :  يقوم باضافه فلتر رصاصي الى وسائط
✛━━━━━━━━━━━━━✛
⑸ ⦙ .يمين الصوره + الرد على ملصق او صوره او فيديو )
🇮🇶  : يقوم بتحويل وجهه الوسائط الى اليمين
✛━━━━━━━━━━━━━✛
⑹ ⦙ .قلب الصوره + الرد على ملصق او صوره او فيديو
🇮🇶  : يقلب الوسائط من فوق لتحت
✛━━━━━━━━━━━━━✛
⑺ ⦙ .زوم + الرد على ملصق او صوره او فيديو
🇮🇶  :  يقوم بتقريب على الوسائط
✛━━━━━━━━━━━━━✛
⑻ ⦙ .اطار + الرد على ملصق او صوره او فيديو
🇮🇶  : يضيف اطار الى الوسائط
✛━━━━━━━━━━━━━✛
⑼ ⦙ .لوقو + الاسم
🇮🇶  : يقوم بصنع logo خاص بك
✛━━━━━━━━━━━━━✛
** ♰ ﻣطوࢪ اެلسۅࢪس :** {my_mention}
""")
@iqthon.on(admin_cmd(pattern="م16(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""** 𖡺   اوامر الملصقات   𖡺  : **
✛━━━━━━━━━━━━━✛
 ⑴ ⦙ .جلب الملصقات + الرد على الملصق
🇮🇶  : يجلب اليك ملصقات الحزمه
✛━━━━━━━━━━━━━✛
⑵ ⦙  .انشاء حزمه ملصقات + الرد على الملصق
🇮🇶  : يضع الملصق بحزمه بشكل مقصوص
✛━━━━━━━━━━━━━✛
⑶ ⦙ .جلب معلومات الملصق + الرد على الملصق )
🇮🇶  : يجلب لك جميع معلومات الملصق
✛━━━━━━━━━━━━━✛
⑷ ⦙ .ملصق + اسم الحزمه او الملصق
🇮🇶  : يبحث عن اسم الحزمه او الملصق ويجلبه اليك
✛━━━━━━━━━━━━━✛
** ♰ ﻣطوࢪ اެلسۅࢪس :** {my_mention}
""")

@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ordSONG")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**❤️‍🔥  𖡺   اوامر التنزيلات والبحث الاغاني    𖡺  :**\n\n⑴  ⦙ `.بحث صوت + اسم الاغنيه`\n**🇮🇶 : سيحمل لك الاغنية صوت ايضا يمكنك وضع رابط الاغنيه بدل الاسم -**\n ✛━━━━━━━━━━━━━✛ \n ⑵  ⦙ `.بحث فيديو + اسم الاغنيه` \n**🇮🇶 : سيحمل لك الاغنية  فيديو ايضا يمكنك وضع رابط الاغنيه بدل الاسم -**\n ✛━━━━━━━━━━━━━✛ \n\n ⑶  ⦙ `.معلومات الاغنيه` \n**🇮🇶 : الرد ع الاغنيه سيجلب لك معلوماتها واسم الفنان -**\n✛━━━━━━━━━━━━━✛ \n \n⑷  ⦙ `.كوكل بحث + موضوع البحث`\n**🇮🇶 : يجلب لك معلومات الموضوع من كوكل -**\n✛━━━━━━━━━━━━━✛ \n⑸  ⦙ `.تخزين الصوت + الرد ع البصمه`\n**🇮🇶 : تخزين الصوت من اجل استخدامه لوضع صوت في الفيديو -**\n ✛━━━━━━━━━━━━━✛ \n⑹ ⦙ `.اضف الصوت + الرد ع الصوره او متحركه او فيديو`\n**🇮🇶 : يتم اضافه الصوت الى الفيديو او المتحركه او الصوره -**\n ✛━━━━━━━━━━━━━✛ \n⑺ ⦙ `.اسم الاغنيه + الرد ع الاغنيه`\n**🇮🇶 : ييجلب لك اسم الاغنيه مدة البصمه 10 الى 5 ثواني -**\n⑻ ⦙ `تيك توك + الرد ع رابط الفيديو.`\n**🇮🇶 : يحمل فيديو تيك توك بدون العلامه المائيه** -\n ✛━━━━━━━━━━━━━✛\n"
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.on(admin_cmd(pattern="م1(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
""" ** 𖡺   اوامر السورس   𖡺  :**
✛━━━━━━━━━━━━━✛
الأمر ⦙ ( .السورس )
الشرح  : يضهر لك معلومات السورس ومدة تنصيبك او امر .فحص -
✛━━━━━━━━━━━━━✛ 
الأمر ⦙ ( .رابط التنصيب )
الشرح  : سوف يعطيك رابط التنصيب - 
✛━━━━━━━━━━━━━✛ 
الأمر ⦙ ( .حساب كيثاب + اسم الحساب )
الشرح  : ينطيك معلومات الحساب وسورساته بموقع جيت هوب - 
✛━━━━━━━━━━━━━✛ 
الأمر ⦙ ( .المده )
الشرح  : يضهر لك مدة تشغيل بوت تليثون لديك 
✛━━━━━━━━━━━━━✛
الأمر ⦙ ( .تحميل ملف + الرد ع الملف )
الشرح : يحمل ملفات تليثون 
✛━━━━━━━━━━━━━✛
الأمر ⦙ ( .مسح ملف + الرد ع الملف )
الشرح :  يمسح الملف الي حملته  
✛━━━━━━━━━━━━━✛
الأمر ⦙ ( .تحديث )
الشرح :  امر لأعاده التشغيل وتحديث ملفات السورس وتسريع التليثون 
✛━━━━━━━━━━━━━✛
الأمر ⦙ ( .اطفاء مؤقت + عدد الثواني )
الشرح : يقوم بأطفاء التليثون بعدد الثواني الي ضفتها  عندما تخلص الثواني سيتم اعاده تشغيل التليثون 
✛━━━━━━━━━━━━━✛
الأمر ⦙ ( .الاوامر ) 
الشرح :   لأضهار جميع اوامر السورس اونلاين
✛━━━━━━━━━━━━━✛
الأمر ⦙ ( .اوامري )
الشرح :   لأضهار جميع اوامر السورس كتابه بدون اونلاين
✛━━━━━━━━━━━━━✛
الأمر ⦙ ( .استخدامي )
الشرح :   يضهر لك كمية استخدامك لتليثون
✛━━━━━━━━━━━━━✛
الأمر ⦙ ( .تاريخ التنصيب )
الشرح :   يضهر لك تاريخ تنصيبك
✛━━━━━━━━━━━━━✛
ﻣطوࢪ اެلسۅࢪس :** {my_mention}""")



@iqthon.on(admin_cmd(pattern="م3(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**  𖡺  اوامر الكروب 1  𖡺  :**

✛━━━━━━━━━━━━━✛ 
 الأمر  ⦙  ( .كتم + الرد ع الشخص )
الشرح  ⦙ يكتم الشخص من الخاص او الكروبات فقط اذا كانت عندك صلاحيه حذف رسائل 
الأمر  ⦙  ( . الغاء كتم + الرد ع الشخص )
الشرح  ⦙ يجلب لك جميع معرفات المشرفين في الكروب  
 ✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .البوتات )
الشرح  ⦙ يجلب لك جميع معرفات البوتات في الكروب 
الأمر ⦙  ( .الأعضاء )
الشرح  ⦙ اضهار قائمة الاعضاء للكروب اذا هواي سيرسل ملف كامل لمعلوماتهم  
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .معلومات )
الشرح  ⦙ سيرسل لك جميع معلومات الكروب بالتفصيل  
الأمر ⦙  ( .مسح المحظورين )
الشرح  ⦙ يمسح جميع المحظورين في الكروب 
 ✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .المحذوفين )
الشرح  ⦙ يجلب لك جميع الحسابات المحذوفه 
الأمر ⦙  ( .المحذوفين تنظيف )
الشرح  ⦙ يمسح جميع الحسابات المحذوفه في الكروب 
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .احصائيات الاعضاء )
الشرح  ⦙ يمسح جميع المحظورين في الكروب 
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .انتحال + الرد ع الشخص )
الشرح  ⦙ يقوم بأنتحال الشخص ويضع صورته ونبذته واسمه في حسابك عدا المعرف  
الأمر ⦙  ( .الغاء الانتحال + الرد ع الشخص )
الشرح  ⦙ يقوم بألغاء الانتحال وسيرجع معلومات المذكوره بالسورس 
✛━━━━━━━━━━━━━✛
الأمر  ⦙  ( .ترحيب + الرساله )
الشرح  ⦙ يضيف ترحيب في الكروب اي شخص ينضم راح يرحب بي  
الأمر  ⦙   ( .مسح الترحيبات )
الشرح  ⦙ ييقوم بمسح الترحيب من الكروب 
✛━━━━━━━━━━━━━✛ 
الأمر  ⦙  ( .ترحيباتي )
الشرح  ⦙ يضهر لك جميع الترحيبات التي وضعتها في الكروب 
✛━━━━━━━━━━━━━✛ 
الأمر  ⦙  ( .رساله الترحيب السابقه تشغيل ) 
الشرح  ⦙ عندما يحدث تكرار سيحذف رساله الترحيب 
الأمر  ⦙  ( .رساله الترحيب السابقه ايقاف )
الشرح  ⦙ عندما يحدث تكرار لا يحذف رساله الترحيب 
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .اضف رد + الكلمه )
الشرح  ⦙ مثلاً تدز رساله هلو تسوي عليها رد بهلوات 
الأمر ⦙  ( .مسح رد + الكلمه )
الشرح  ⦙ سيحذف الكلمه الي انت ضفتها 
الأمر ⦙  ( .جميع الردود )
 الشرح  ⦙ يجلب لك جميع الردود الذي قمت بأضافتها  
الأمر ⦙  ( .مسح جميع الردود )
الشرح  ⦙ يمسح جميع الردود الي انت ضفتها 
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .صنع مجموعه + اسم المجموعه )
الشرح  ⦙ يقوم بعمل مجموعه خارقه 
الأمر ⦙  ( .صنع قناه +  اسم القناة )
الشرح  ⦙ يقوم بعمل قناه خاصه  
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .عدد رسائلي )
الشرح  ⦙ سيظهر لك عدد رسائلك في الكروب 
✛━━━━━━━━━━━━━✛
الأمر  ⦙  ( .تفعيل حمايه المجموعه )
الشرح  ⦙ يقوم غلق جميع صلاحيات المجموعه يبقي فقط ارسال  الرسائل
الأمر  ⦙ تعطيل حمايه المجموعه
الشرح  ⦙ يقوم بتشغيل جميع صلاحيات المجموعة ماعدا تغير المعلومات و التثبيت و اضافه اعضاء تبقى مسدوده
✛━━━━━━━━━━━━━✛ 
الأمر  ⦙  ( .صلاحيات المجموعه )
الشرح  ⦙ يقوم بعرض صلاحيات المجموعه المغلقه والمفتوحه
✛━━━━━━━━━━━━━✛
الأمر  ⦙  ( .رفع مشرف + الرد على شخص )
الشرح  ⦙ يرفع الشخص مشرف يعطي صلاحيه حذف رسائل والتثبيت فقط
✛━━━━━━━━━━━━━✛ 
الأمر  ⦙  ( .منع + كلمة )
الشرح  ⦙ منع كلمه من الارسال في الكروب
الأمر ⦙  ( .الغاء منع + كلمه )
الشرح  ⦙ يقوم بالغاء منع الكلمه  
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .قائمه المنع )
الشرح  ⦙ يقوم بجلب جميع الكلمات الممنوعه في الكروب 
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .تاك + ( الاعداد المحدده وثابتة فقط) ⤵️
  ( 10 - 50 - 100 - 200  )
الشرح  ⦙ يجلب لك الاعضاء بالروابط بالعدد المحدد 
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .معرفات + ( الاعداد المحدده وثابتة فقط) ⤵️
  ( 10 - 50 - 100 - 200  )
الشرح  ⦙ جلب لك معرفات الاعضاء بالعدد المحدد 
✛━━━━━━━━━━━━━✛
الأمر  ⦙  ( .تنظيف الوسائط )
 الشرح  ⦙ ينضف جميع ميديا من صور وفديوهات و متحركات او ( .تنظيف الوسائط + العدد)  
✛━━━━━━━━━━━━━✛ 
الأمر  ⦙  ( .حذف الرسائل )
الشرح  ⦙ يحذف جميع الرسائل بلكروب  
  او  .حذف الرسائل + العدد 
✛━━━━━━━━━━━━━✛ 
الأمر  ⦙  ( .مسح + الرد على رسالة )
الشرح  ⦙ يحذف الرساله الي راد عليها فقط 
✛━━━━━━━━━━━━━✛ 
الأمر  ⦙  ( .غادر )
الشرح  ⦙ يغادر من المجموعه او من القناة
✛━━━━━━━━━━━━━✛ 
الأمر  ⦙  ( .تفليش )
الشرح  ⦙ يطرد جميع الي في الكروب او قناة 
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .اضافه + رابط الكروب )
الشرح  ⦙ يضف اليك جميع الاعضاء الى الكروب 
 ( يجب ان تتاكد انك  لست محضور ارسل ⬅️
( .فحص الحظر ) من اجل التاكد
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .جلب الوقتيه + الرد على الصورة )
الشرح  ⦙ الرد على صوره سريه وقتيه سوف يتم تحويلها الى رسائل المحفوضه كصورة عادية
✛━━━━━━━━━━━━━✛ 
ﻣطوࢪ اެلسۅࢪس :** {my_mention}""")
@iqthon.on(admin_cmd(pattern="م4(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**  𖡺  اوامر الكروب 2  𖡺  : **
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .تاك بالكلام + الكلمه + معرف الشخص )
الشرح  ⦙ يعمل تاك للشخص بالرابط جربه وتعرف
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .نسخ + الرد على رساله )
الشرح  ⦙ يرسل الرساله التي رديت عليها 
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .ابلاغ الادمنيه )
الشرح  ⦙ يعمل تاك لجميع الادمنيه  
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .المشرفين )
الشرح  ⦙ يجلب اليك جميع المشرفين 
الأمر ⦙  ( .البوتات )
الشرح  ⦙ يجلب الك جميع بوتات في المجموعه او قناه
✛━━━━━━━━━━━━━✛
الأمر ⦙  ( .حظر + الرد على شخص )
الشرح  ⦙ حظر الشخص من المجموعه 
الأمر  ⦙  ( .الغاء الحظر + الرد على شخص )
الشرح  ⦙ يلغي حظر الشخص من المجموعه
✛━━━━━━━━━━━━━✛ 
الأمر  ⦙  ( .بدء مكالمه )
الشرح  ⦙ يقوم بتشغيل مكالمه 
الأمر ⦙  ( .دعوه للمكالمه )
الشرح  ⦙ يتم دعوه الاعضاء للمكالمة الشغاله
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .تنزيل مشرف + الرد على شخص )
الشرح  ⦙ يقوم بازاله الشخص من الاشراف 
✛━━━━━━━━━━━━━✛ 
الأمر  ⦙  ( .تثبيت + الرد على رساله )
 شرح : تثبيت الرساله التي رديت عليها
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .الأعضاء )
الشرح  ⦙ اضهار قائمة الاعضاء للمجموعة 
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .تفليش )
الشرح  ⦙  أزاله جميع اعضاء المجموعه
 ✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .مسح المحظورين )
الشرح  ⦙ يمسح جميع المحظورين 
✛━━━━━━━━━━━━━✛ 
الأمر  ⦙  ( .المحذوفين )
الشرح  ⦙  يجلب لك الحسابات المحذوفه 
الأمر ⦙  ( .المحذوفين تنظيف )
الشرح  ⦙ مسح الحسابات المحذوفه
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .احصائيات الاعضاء )
الشرح  ⦙ يجلب جميع معلومات اعضاء المجموعه 
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .عدد رسائلي )
الشرح  ⦙ يقوم بحساب عدد رسائلك 
✛━━━━━━━━━━━━━✛ 
الأمر ⦙  ( .جلب الاحداث )
الشرح  ⦙ يجلب اخر 20 رساله محذوفه
✛━━━━━━━━━━━━━✛
الأمر  ⦙ ( .حظر عام + الرد على شخص ) 
الشرح  ⦙ حظر من جميع الكروبات   
✛━━━━━━━━━━━━━✛
الأمر  ⦙ ( .الغاء حظر عام + الرد على شخص )
الشرح  ⦙ الغاء حضر العام  
✛━━━━━━━━━━━━━✛
الأمر  ⦙ ( .المحظورين عام )
الشرح ⦙  يضهر المحضورين عام 
✛━━━━━━━━━━━━━✛
الشرح  ⦙ ( .تقيد + الرد على شخص )
الأمر  ⦙ يقيد الشخص من المجموعة 
✛━━━━━━━━━━━━━✛
ﻣطوࢪ اެلسۅࢪس :** {my_mention}""")
@iqthon.on(admin_cmd(pattern="م5(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**𖡺  اوامر تحويل الصيغ  𖡺  :**
———————×——————
الأمر ⦙  .تحويل بصمه + الرد ع الصوت mp3
الشرح : يحول صوت mp3 الى بصمه 
———————×——————
الأمر ⦙  .تحويل صوت + الرد ع الصوت 
الشرح  :  يحول البصمه الى صوت   mp3
———————×——————
الأمر  ⦙  .تحويل ملصق + الرد ع الصوره 
الشرح :  يحول الصوره الى ملصق 
———————×——————
الأمر  ⦙ . تحويل صوره + الرد ع الملصق 
الشرح :  يحول الملصق الى صوره 
———————×——————
الأمر ⦙  .تحويل متحركه + الرد ع الفيديو 
الشرح :  يقوم بتحويل الفيديو الى متحركه 
———————×——————
الأمر  ⦙  .بي دي اف + الرد ع الملف او الصوره
الشرح :  يحول الملف الى بي دي اف 
———————×—————— 
الأمر  ⦙ .ملصقي + الرد ع الرساله 
الشرح  : يحول رساله الى ملصق 
———————×——————
الأمر  ⦙  . تليجراف ميديا + الرد ع الفيديو او صوره
الشرح :  يقوم بتحويل الفيديو او الصوره الى رابط تليجراف  
———————×——————
الأمر ⦙  ( .تحويل رساله + الرد ع الملف )
الشرح :  يقوم بجلب جميع الكتابه الذي داخل الملف ويقوم بأرسالها اليك 
———————×——————
الأمر ⦙ ( .تحويل فديو دائري + الرد ع الفيديو )
الشرح : يحول الفيديو الى فيديو دائري مرئي 
———————×——————
الأمر  ⦙ ( .تحويل ملصق دائري + الرد ع الملصق )
الشرح :  يحول الملصق الى ملصق دائري
———————×——————
 الأمر ⦙  ( .ترجمه en + الرد ع الرساله )
الشرح :  يقوم بترجمه الرساله الى اللغه الانكليزيه
———————×——————
الشرح ⦙ ( .ترجمه ar + الرد ع الشخص )
الأمر  :  يقوم بترجمه الرساله الى اللغه العربيه 
———————×——————
ﻣطوࢪ اެلسۅࢪس :** {my_mention}""")
