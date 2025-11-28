import random #NEERAJ BOTS
import time #NEERAJ BOTS
import math #NEERAJ BOTS
import os #NEERAJ BOTS
from vars import CREDIT #NEERAJ BOTS
from pyrogram.errors import FloodWait #NEERAJ BOTS
from datetime import datetime,timedelta #NEERAJ BOTS

class Timer: #NEERAJ BOTS
    def __init__(self, time_between=5): #NEERAJ BOTS
        self.start_time = time.time() #NEERAJ BOTS
        self.time_between = time_between #NEERAJ BOTS

    def can_send(self): #NEERAJ BOTS
        if time.time() > (self.start_time + self.time_between): #NEERAJ BOTS
            self.start_time = time.time() #NEERAJ BOTS
            return True #NEERAJ BOTS
        return False #NEERAJ BOTS

#lets do calculations #NEERAJ BOTS
def hrb(value, digits= 2, delim= "", postfix=""): #NEERAJ BOTS
    """Return a human-readable file size. #NEERAJ BOTS
    """ #NEERAJ BOTS
    if value is None: #NEERAJ BOTS
        return None #NEERAJ BOTS
    chosen_unit = "B" #NEERAJ BOTS
    for unit in ("KB", "MB", "GB", "TB"): #NEERAJ BOTS
        if value > 1000: #NEERAJ BOTS
            value /= 1024 #NEERAJ BOTS
            chosen_unit = unit #NEERAJ BOTS
        else: #NEERAJ BOTS
            break #NEERAJ BOTS
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix #NEERAJ BOTS

def hrt(seconds, precision = 0): #NEERAJ BOTS
    """Return a human-readable time delta as a string. #NEERAJ BOTS
    """ #NEERAJ BOTS
    pieces = [] #NEERAJ BOTS
    value = timedelta(seconds=seconds) #NEERAJ BOTS

    if value.days: #NEERAJ BOTS
        pieces.append(f"{value.days}day") #NEERAJ BOTS

    seconds = value.seconds #NEERAJ BOTS

    if seconds >= 3600: #NEERAJ BOTS
        hours = int(seconds / 3600) #NEERAJ BOTS
        pieces.append(f"{hours}hr") #NEERAJ BOTS
        seconds -= hours * 3600 #NEERAJ BOTS

    if seconds >= 60: #NEERAJ BOTS
        minutes = int(seconds / 60) #NEERAJ BOTS
        pieces.append(f"{minutes}min") #NEERAJ BOTS
        seconds -= minutes * 60 #NEERAJ BOTS

    if seconds > 0 or not pieces: #NEERAJ BOTS
        pieces.append(f"{seconds}sec") #NEERAJ BOTS

    if not precision: #NEERAJ BOTS
        return "".join(pieces) #NEERAJ BOTS

    return "".join(pieces[:precision]) #NEERAJ BOTS

timer = Timer() #NEERAJ BOTS

async def progress_bar(current, total, reply, start): #NEERAJ BOTS
    if timer.can_send(): #NEERAJ BOTS
        now = time.time() #NEERAJ BOTS
        diff = now - start #NEERAJ BOTS
        if diff < 1: #NEERAJ BOTS
            return #NEERAJ BOTS
        else: #NEERAJ BOTS
            perc = f"{current * 100 / total:.1f}%" #NEERAJ BOTS
            elapsed_time = round(diff) #NEERAJ BOTS
            speed = current / elapsed_time #NEERAJ BOTS
            remaining_bytes = total - current #NEERAJ BOTS
            if speed > 0: #NEERAJ BOTS
                eta_seconds = remaining_bytes / speed #NEERAJ BOTS
                eta = hrt(eta_seconds, precision=1) #NEERAJ BOTS
            else: #NEERAJ BOTS
                eta = "-" #NEERAJ BOTS
            sp = str(hrb(speed)) + "/s" #NEERAJ BOTS
            tot = hrb(total) #NEERAJ BOTS
            cur = hrb(current) #NEERAJ BOTS
            bar_length = 10 #NEERAJ BOTS
            completed_length = int(current * bar_length / total) #NEERAJ BOTS
            remaining_length = bar_length - completed_length #NEERAJ BOTS

            symbol_pairs = [ #NEERAJ BOTS
                #("🟢", "⚪"), #NEERAJ BOTS
                #("⚫", "⚪"), #NEERAJ BOTS
                #("🔵", "⚪"), #NEERAJ BOTS
                #("🔴", "⚪"), #NEERAJ BOTS
                #("🔘", "⚪"), #NEERAJ BOTS
                ("🟩", "⬜") #NEERAJ BOTS
            ] #NEERAJ BOTS
            chosen_pair = random.choice(symbol_pairs) #NEERAJ BOTS
            completed_symbol, remaining_symbol = chosen_pair #NEERAJ BOTS

            progress_bar = completed_symbol * completed_length + remaining_symbol * remaining_length #NEERAJ BOTS

            try: #NEERAJ BOTS
                #await reply.edit(f'`╭──⌯═════𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋NEERAJ 𝘽𝙊𝙏𝙎🦋✨═══─╯`') 
                await reply.edit(f'<blockquote>`╭──⌯═════𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐢𝐜𝐬══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋NEERAJ🦋✨═══─╯`</blockquote>') 
            except FloodWait as e: #NEERAJ BOTS
                time.sleep(e.x) #NEERAJ BOTS 
