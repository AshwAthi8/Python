import os
import sys
import discord
from subprocess import getoutput

TOKEN = 'NzI5Njk4NjQwODc2MjczNzM2.XwQ9ZQ.fu_-aW2c3VpwJgRyG04YiDVSKjA'
# PCAP_CAPTURE_CHANNEL = 730327151747924079

CHANNEL_ID = 734025381962842183 #change here
CHALL_PORT = 9001 #change here
FOLDER_NAME = "poolcide"

client = discord.Client()


async def send_pcap():
    # challenge=sys.argv[1]
    await client.wait_until_ready()
    counter = 0
    channel = client.get_channel(734025381962842183) #change here
    while not client.is_closed():
        counter += 1
        # cpu_count, cpu_curr_freq, cpu_percent, ram_usage, ram_avail, ram_total, disk_usage, disk_free, disk_total, uptime = system_stats()

        os.system("timeout 180 tcpdump -w /root/pcaps/{}/{}.pcap".format(FOLDER_NAME, counter, CHALL_PORT))
        d = getoutput("curl https://bashupload.com/file%7B%7D.pcap --data-binary @/root/pcaps/{}/{}.pcap".format(counter, FOLDER_NAME, counter))
        print(d)
        print("\n\n")
        ind = d.find("https")
        url = d[ind::]
        embed = discord.Embed(title='New Capture',url=url,description='Click on the title to download the capture',color=0x14dc0b)
        # await channel.send("New capture is here for the cartography challenge, try finding exploits from this!!")
        await channel.send(embed=embed)
