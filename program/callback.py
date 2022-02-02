# Copyright (C) 2021 By VeezMusicProject


# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("arbic"))
async def arbic(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""مرحباً بك \n
⌁ ⁞  بوت تشغيل الأغاني والفيديو  في المكالمه ' المرئية
 البوت قيد التشغيل الان ...... ⚡♥️
⌁ ⁞ my developer [𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶](https://t.me/ahmedelnqyb)
⌁ ⁞  قم بإضافة البوت اللي مجموعتك واستمع إلى الموسيقى ومشاهدة الفيديوهات ♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضف البوت اللي مجموعتك ⚡♥️",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("طريقة التفعيل", callback_data="bhowtouse")],
                [
                    InlineKeyboardButton("طريقة التشغيل", callback_data="bcmds"),
                    InlineKeyboardButton("المطور", url=f"https://t.me/ahmedelnqyb"),
                ],
                [
                    InlineKeyboardButton(
                        "الجروب", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "القناة", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶", url="https://t.me/ahmedelnqyb"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex("english"))
async def english(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"A Telegram Music Bot Based Mongodb \n Add Me To Ur Chat For and Help and And Support Click On Buttons \n 💞  These Features AI Based \nPowered By [𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶](https://t.me/ahmedelnqyb)",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Add me to your Group ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(" Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton(" Commands", callback_data="cbcmds"),
                    InlineKeyboardButton(" Donate", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶", url="https://t.me/ahmedelnqyb"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""❓ **Basic Guide for using this bot:**
1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**
📌 **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**
💡 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**
⚡ __ Developer by [𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶](https://t.me/ahmedelnqyb)""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
» **press the button below to read the explanation and see the list of available commands !**
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""🏮 here is the basic commands:
» /play (song name/link) - play music on video chat
» /vplay (video name/link) - play video on video chat
» /vstream - play live video from yt live/m3u8
» /playlist - show you the playlist
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /lyric (query) - scrap the song lyric
» /search (query) - search a youtube video link
» /ping - show the bot ping status
» /speedtest - run the bot server speedtest
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in group)
⚡️ __ Developer by [𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶](https://t.me/ahmedelnqyb)""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""🏮 here is the admin commands:
» /pause - pause the stream
» /resume - resume the stream
» /skip - switch to next stream
» /stop - stop the streaming
» /vmute - mute the userbot on voice chat
» /vunmute - unmute the userbot on voice chat
» /volume `1-200` - adjust the volume of music (userbot must be admin)
» /reload - reload bot and refresh the admin data
» /userbotjoin - invite the userbot to join group
» /userbotleave - order userbot to leave from group
⚡️ __ Developer by [𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶](https://t.me/ahmedelnqyb)""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:
» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /sysinfo - show the system information
» /update - update your bot to latest version
» /restart - restart your bot
» /leaveall - order userbot to leave from all group
⚡ __ Developer by [𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶](https://t.me/ahmedelnqyb)""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("bhowtouse"))
async def acbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" **طريقة تفعيل البوت في مجموعتك ⚡♥️:**
1.) **اولا قم بإضافة البوت اللي مجموعتك ⚡.**
2.) **قم بترقيى البوت مشرف مع الصلاحيات المطلوبة ⚡.**
3.) ** لتحديث قائمة الادمن /Reload قم بكتابة الامر ⚡.**
3.) ** /uesrbotjoin قم بإضافة الحساب المساعد اللي المجموعة عن طريق كاتبة الامر /انضم او ⚡.**
4.) **تاكد كن تشغيل المحادثة المرئية ⚡.**
5.) ** /Reload اذا واجهت خطأ قم بكتابة الامر ⚡.**
📌 ** في حال لم يستطع الحساب المساعد الانضمام اللي المحادثة المرئية قم بطرد الحساب المساعد بالأمر /غادر ⚡.  \n ودعوتة من جديد عنريق الامر /انضم ⚡.**
💡 **في حال واجهت اي مشكلة اخري يمكنك التواصل مع احمد النقيب من هن : @ahmedelnqyb **
⚡ __ Developer by [𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶](https://t.me/ahmedelnqyb)""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶", callback_data="ahmedelnqyb")]]
        ),
    )


@Client.on_callback_query(filters.regex("bcmds"))
async def acbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
» **اتبع الازرار بالاسفل لمعرفة طريقة التشغيل ⚡**
⚡ __ Developer by [𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶](https://t.me/ahmedelnqyb)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("اوامر التشغيل", callback_data="cbbasic"),
                    InlineKeyboardButton("اوامر الادمن", callback_data="cbadmin"),
                ],[
                    InlineKeyboardButton("اوامر المطورين", callback_data="cbsudo")
                ],[
                    InlineKeyboardButton("𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶", callback_data="ahmedelnqyb")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("bbasic"))
async def acbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""اوامر التشغيل ⚡:
» /play (اسم الموسيقي / link ) - لتشغيل الموسيقى في المحادثة الصوتية 
» /stream ( قم بالرد علي الملف /link) - لتشغيل مقطع فيديو موجود في الدردشة
» /vplay (اسم الفيديو /link) - لتشغيل مقطع فيديو 
» /vstream - لنشغيل بث مباشر
» /playlist - لعرض قائمة التشغيل
» /video - لتحميل مقطع فيديو
» /song - لتحميل ملف صوتي 
» /lyric - لجلب كلمات الاغنية 
» /search - البحث عن روابط يوتيوب
» /ping - عرض سرعة الاستجابة
» /uptime - وقت تشغيل البوت
» /alive - لعرض معلومات البوت 
⚡️ __ Developer by [𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶](https://t.me/ahmedelnqyb)""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("badmin"))
async def acbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""اوامر التحكم للخاصة بالادمنية:
» /pause - ايقاف التشغيل موقتأ
» /resume - لاستكمال التشغيل
» /skip - لتخطي تشغيل الحالي
» /stop - لايقاف تشغيل الحالي
» /vmute - لكتم الحساب المساعد في المحادثة الصوتية
» /vunmute - الغاء كتم الحساب المساعد
» /volume `1-200` - لتحكم في درجة الصوت
» /reload - لتحديث قائمة الادمن للتحكم في البوت
» /userbotjoin - لدعوة الحساب المساعد للدردشة
» /userbotleave - لطرد الحساب المساعد من الدردشة
⚡️ __ Developer by [𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶](https://t.me/ahmedelnqyb)""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("bsudo"))
async def acbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""اوامر المطورين :
» /rmw - لمسح جميع الملفات المتخزنة
» /rmd - تنظيف التخزين المؤقت
» /sysinfo - لعرض قدرات التشغيل
» /update - لتحديث اصدار السورس
» /restart - إعادة تشغيل البوت
» /leaveall - خروج الحساب المساعد من جميع المحادثات
⚡ __ Developer by [𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶](https://t.me/ahmedelnqyb)""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbmenu"))
async def acbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.message.delete()

@Client.on_callback_query(filters.regex("ahmedelnqyb"))
async def ahmedelnqyb(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>◉ انا احمد النقيب يمكنك التواصل معي..↑↓ \n\n◉ عن طريق معرفي اول جروب التواصل بلاسفل..↑↓ \n\n [𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶](https://t.me/ahmedelnqyb)</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("الجروب", url=f"https://t.me/barelnqyb"),
                    InlineKeyboardButton("القناة", url=f"https://t.me/elnqyb"),
                ],
                [
                    InlineKeyboardButton("البوت", url=f"https://t.me/ahmedebot"),
                    InlineKeyboardButton("التواصل", url=f"https://t.me/elnqybsp"),
                ],
                [InlineKeyboardButton("𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶", url=f"https://t.me/ahmedelnqyb")],
            ]
        ),
    )
