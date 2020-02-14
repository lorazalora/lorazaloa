#made by @DneZyeK
import asyncio
import re
import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^.lz(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	await typew.edit("`Connecting To Hacked Private Server...`")
	sleep(4)
	await typew.edit("0%")
	number = 1
	await typew.edit("`Target Selected.`")

	sleep(0.05)
	await typew.edit("`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")

	sleep(0.05)
	await typew.edit("`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")

	sleep(0.05)
	await typew.edit("`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
	
	sleep(0.05)
	await typew.edit("`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
	
	sleep(0.05)
	await typew.edit("`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
	sleep(0.05)
	await typew.edit("`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
sleep(0.05)
	await typew.edit("`Hacking... 84%\n█████████████████████▒▒▒▒ `")
sleep(0.05)
	await typew.edit("`Hacking... 100%\n█████████HACKED███████████ `")
	sleep(1)
	await typew.edit("`Targeted Account Hacked...\n\nPay 9999$ To @Lorazalora or a Plate of Samosas To Remove This Hack`")


CMD_HELP.update({
    'fakeload':
    '.lz\
        \nUsage: Tokek Goreng Dan makanan penutup.'
})
