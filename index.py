from re import A
import discord, asyncio, datetime, pytz
from discord.embeds import Embed
import random
import ffmpeg

import time
import asyncio
from selenium.webdriver.chrome.options import *
from selenium import webdriver

from discord import client
from discord import colour
from discord import activity
token = "ODU4NjQ3MTIwNjU4MzAwOTY4.YNhLcg.n9R6KsN7PSAuBg6YAPQki_07cJ8"
client = discord.Client()

@client.event
async def on_ready():
    print("Online")
    game = discord.Game("설명서")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "안녕":
        await message.channel.send("응 안녕")
    if message.content == "아 졸리다":
        await message.channel.send("어쩔티비 저쩔티비 안물티비 안궁티비 ")
    if message.content == "뭐함":
        await message.channel.send("니가 알아서 뭐하게")
    if message.content == "10초 타이머":
        await message.channel.send(" 10초 타이머 시작!")
    if message.content == "1분 타이머":
        await message.channel.send(" 1분 타이머 시작!")
    if message.content == "5분 타이머":
        await message.channel.send(" 5분 타이머 시작!")
    if message.content == "10분 타이머":
        await message.channel.send(" 10분 타이머 시작!")
    if message.content == "999999999999999999999999999초 타이머":
        await message.channel.send("999999999999999999999999999초 타이머 시작!")
    if message.content == "흑흑":
        await message.channel.send("?")
    if message.content == "ㅎ그흑":
        await message.channel.send("?")
    

    if message.content == "%모든 명령어":
         embed = discord.Embed(colour=discord.Colour.red(), title="여기", description="1.청소. (뒤에 숫자) 2.임베드 3.뽑기 4.운세 5.안녕 6. 아 졸리다 6.아니 7.뭐함 8.10초 타이머 9.1분 타이머 10.5분 타이머 11.10분 타이머 12.내정보 13.'투표/(제목)/(투표내용) 14.이모지 15.죽어 16.야 17.초성퀴즈")
         await message.channel.send(embed=embed)

    if message.content == "임베드":
         embed = discord.Embed(colour=discord.Colour.red(), title="여기", description="임베드")
         await message.channel.send(embed=embed)

    if message.content.startswith ("&청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="채팅 {}개가\n {}의 의해 삭제됨.".format(amount, message.author), color=0x000000)
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{} 당신의 대한 관리자 권한 없음.".format(message.author.mention))

    if message.content == "뽑기":
        ran = random.randint(0,1)
        if ran == 0:
            d = "꽝"
        if ran == 1:
            d = "당첨"
        await message.channel.send(d)

    if message.content == "10초 타이머":
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention}, 10초가 지났어요!")

    if message.content == "1분 타이머":
        await asyncio.sleep(60)
        await message.channel.send(f"{message.author.mention}, 1분이 지났어요!")

    if message.content == "5분 타이머":
        await asyncio.sleep(300)
        await message.channel.send(f"{message.author.mention}, 5분이 지났어요!")

    if message.content == "10분 타이머":
        await asyncio.sleep(600)
        await message.channel.send(f"{message.author.mention}, 10분이 지났어요!")

    if message.content == "999999999999999999999999999초 타이머":
        await asyncio.sleep(999999999999999999999999999)
        await message.channel.send(f"{message.author.mention}, 999999999999999999999999999초가 지났어요!")

    if message.content.startswith("내정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(colour=0x08080)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년 " + str(date.month) + "월 " + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("&투표"):
        vote = message.content[4:].split("/")
        if len(vote) > 5:
            await message.channel.send(' 투표 항목은 5개 이하로 해주세요.')
        elif len(vote) <= 5:
            await message.channel.send("투표 - " + vote[0])
            for i in range(1, len(vote)):
                    choose = await message.channel.send("```" + vote[i] + "```")
                    await choose.add_reaction('👍')

    if message.content == "운세":
        await message.channel.send(random.choice(['뷔페감', '밖에서 똥 밟음', '컴퓨터 압수', '폰 압수', '유튜브 정지', '혼남', '밖에서 놀려고 나왔는데 비와서 우산 챙기고 나갔는데 비그침']))
            
    if message.content.startswith('죽어'):
        channel = message.channel
        await channel.send(' 죽으라니...')

        def check(m):
            return m.content == '죽으라고' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('꽥'.format(msg))

    if message.content == "초성퀴즈":
        await message.channel.send(random.choice(['ㅇㄴㅎㅅㅇ ㅈㄴ ㅂ ㅇㄴㄷ', 'ㅇ ㅇㅉㄹㄱ', 'ㅇ ㅅㅂ ㅁㅊㄴ', 'ㅁㅎㄴ', 'ㅁㅁㅁ ㅎㅎㅅㅇ']))

    if message.content.startswith('이모지'):
        channel = message.channel
        await channel.send(' 이 메시지에 👍반응을 해주세요. ')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')

    if message.content == "설명서":
        embed = discord.Embed(title="설명서", description="*모든 명령어를 두눈에!*",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name="1.&청소 (뒤에 숫자)", value="예 : 청소. 10", inline=False)
        embed.add_field(name="2.임베드", value="예 : 임베드", inline=False)

        embed.add_field(name="3.뽑기", value="예 : 뽑기", inline=False)
        embed.add_field(name="4.운세", value="예 : 운세", inline=False)

        embed.add_field(name="5.10초 타이머", value="예 : 10초 타이머", inline=False)
        embed.add_field(name="6.1분 타이머", value="예 : 1분 타이머", inline=True)


        embed.add_field(name="7.5분 타이머", value="예 : 5분 타이머", inline=False)
        embed.add_field(name="8.10분 타이머", value="예 : 10분 타이머", inline=False)

        embed.add_field(name="9.내정보", value="예 : 내정보", inline=False)
        embed.add_field(name="10.&투표", value="예 : &투표/(투표 제목)/(투표 항목)", inline=False)

        embed.add_field(name="11.이모지", value="예 : 이모지", inline=False)
        embed.add_field(name="12.초성퀴즈", value="예 : 초성퀴즈", inline=False)
        embed.add_field(name="13.&모든 명령어(구)", value="예 : %모든 명령어", inline=False)

        embed.add_field(name="14.999999999999999999999999999초 타이머", value="예 : 999999999999999999999999999초 타이머", inline=False)

        embed.set_footer(text="Bot Made by. waw_05", icon_url="https://cdn.discordapp.com/icons/767964771651682325/77893d482cfc8dc93fe388f1e697af12.png?size=128&quot")
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/767964771651682325/77893d482cfc8dc93fe388f1e697af12.png?size=128&quot")
        await message.channel.send (embed=embed)

    if message.content == "핑":
        la = client.latency
        await message.channel.send(f'🏓퐁! 일줄 알았나 인간? `{str(round(la * 1000))}ms`임')



client.run(token)
