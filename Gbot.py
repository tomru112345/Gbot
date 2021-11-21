#!/usr/bin/python
# -*- coding: <encoding name> -*-
# -*- coding: utf-8 -*-

import discord
import subprocess
import sys
from datetime import datetime, timedelta
from pdf2image import convert_from_path
import re
import os
import glob
import tokenGbot

# 自分のBotのアクセ
TOKEN = tokenGbot.TOKEN
keigo_sever = tokenGbot.keigo_sever
VC_ID = tokenGbot.VC_ID
voice_chat_ID = tokenGbot.voice_chat_ID
pubglite_VC_ID = tokenGbot.pubglite_VC_ID
Text_ID = tokenGbot.Text_ID
Genkai_log_ID = tokenGbot.Genkai_log_ID

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理


@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('システムログ: ログインしました')

# メッセージ受信時に動作する処理


@client.event
async def on_message(message):
    # シャットダウンコマンド
    if message.author.bot:
        pass
    # コマンド
    else:
        if message.content == '#shutdown':
            await message.channel.send('Shutdown now')
            print('システムログ: シャットダウンします')
            await client.logout()
            await sys.exit()

        elif message.content.startswith("#convert word2pdf"):
            if message.attachments:
                if message.attachments[0].filename.endswith(".docx"):
                    print("システムログ: Word を PDF に変換します")
                    docx_path = "./docx/" + message.attachments[0].filename
                    await message.attachments[0].save(docx_path)
                    args = ['./word2pdf.sh', docx_path, "./pdf/" +
                            message.attachments[0].filename[:-4] + "pdf"]
                    subprocess.run(args)
                    print(
                        "./pdf/"+message.attachments[0].filename[:-4] + "pdf")
                    await message.channel.send(file=discord.File("./pdf/"+message.attachments[0].filename[:-4] + "pdf"))
            else:
                print("エラー: 添付ファイルを用意してください")

        elif message.content.startswith("#convert md2pdf"):
            if message.attachments:
                if message.attachments[0].filename.endswith(".md"):
                    print("システムログ: Markdown を PDF に変換します")
                    md_path = "./Markdown/" + message.attachments[0].filename
                    await message.attachments[0].save(md_path)
                    args = ['./md2pdf.sh', md_path, "./pdf/" +
                            message.attachments[0].filename[:-2] + "pdf"]
                    subprocess.run(args)
                    print(
                        "./pdf/"+message.attachments[0].filename[:-2] + "pdf")
                    await message.channel.send(file=discord.File("./pdf/"+message.attachments[0].filename[:-2] + "pdf"))
            else:
                print("エラー: 添付ファイルを用意してください")

        elif message.content.startswith("#convert md2pptx"):
            if message.attachments:
                if message.attachments[0].filename.endswith(".md"):
                    print("システムログ: Markdown を PowerPoint に変換します")
                    md_path = "./Markdown/" + message.attachments[0].filename
                    await message.attachments[0].save(md_path)
                    args = ['./md2pptx.sh', md_path, "./pptx/" +
                            message.attachments[0].filename[:-2] + "pptx"]
                    subprocess.run(args)
                    print(
                        "./pptx/"+message.attachments[0].filename[:-2] + "pptx")
                    await message.channel.send(file=discord.File("./pptx/"+message.attachments[0].filename[:-2] + "pptx"))
            else:
                print("エラー: 添付ファイルを用意してください")

        elif message.content.startswith("#convert md2word"):
            if message.attachments:
                if message.attachments[0].filename.endswith(".md"):
                    print("システムログ: Markdown を Word に変換します")
                    md_path = "./Markdown/" + message.attachments[0].filename
                    await message.attachments[0].save(md_path)
                    args = ['./md2word.sh', md_path, "./docx/" +
                            message.attachments[0].filename[:-2] + "docx"]
                    subprocess.run(args)
                    print(
                        "./docx/"+message.attachments[0].filename[:-2] + "docx")
                    await message.channel.send(file=discord.File("./docx/"+message.attachments[0].filename[:-2] + "docx"))
            else:
                print("エラー: 添付ファイルを用意してください")

        elif message.content.startswith("#convert md2tex"):
            if message.attachments:
                if message.attachments[0].filename.endswith(".md"):
                    print("システムログ: Markdown を tex に変換します")
                    md_path = "./Markdown/" + message.attachments[0].filename
                    await message.attachments[0].save(md_path)
                    args = ['./md2tex.sh', md_path, "./tex/" +
                            message.attachments[0].filename[:-2] + "tex"]
                    subprocess.run(args)
                    print(
                        "./tex/"+message.attachments[0].filename[:-2] + "tex")
                    await message.channel.send(file=discord.File("./tex/"+message.attachments[0].filename[:-2] + "tex"))
            else:
                print("エラー: 添付ファイルを用意してください")

        elif message.content.startswith("#show pdf"):
            sp_args = message.content.split()
            print(sp_args)
            if message.attachments:
                if message.attachments[0].filename.endswith(".pdf"):
                    print("システムログ: PDF を jpg で展開します")
                    pdf_path = "./pdf/" + message.attachments[0].filename
                    await message.attachments[0].save(pdf_path)
                    img_path = "./image"
                    convert_from_path(pdf_path, output_folder=img_path, fmt='jpeg',
                                      output_file=message.attachments[0].filename[:-4])

                    result = glob.glob(os.path.join("./image", '*'))

                    t = 0
                    for i in result:
                        result[t] = discord.File(i)
                        t = t + 1

                    await message.channel.send(files=result[:10])
                    result = glob.glob(os.path.join("./image", '*'))
                    for i in result:
                        args = ['rm', i]
                        subprocess.run(args)
            else:
                print("エラー: 添付ファイルを用意してください")

        # todo

        elif message.content.startswith("#show docx"):
            sp_args = message.content.split()
            print(sp_args)
            if message.attachments:
                if message.attachments[0].filename.endswith(".docx"):
                    print("システムログ: PDF を jpg で展開します")
                    pdf_path = "./pdf/" + message.attachments[0].filename
                    await message.attachments[0].save(pdf_path)
                    img_path = "./image"
                    convert_from_path(pdf_path, output_folder=img_path, fmt='jpeg',
                                      output_file=message.attachments[0].filename[:-4])

                    result = glob.glob(os.path.join("./image", '*'))

                    t = 0
                    for i in result:
                        result[t] = discord.File(i)
                        t = t + 1

                    await message.channel.send(files=result[:10])
                    result = glob.glob(os.path.join("./image", '*'))
                    for i in result:
                        args = ['rm', i]
                        subprocess.run(args)
            else:
                print("エラー: 添付ファイルを用意してください")

# voicechannelへの入退室アナウンス


@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == keigo_sever and (before.channel != after.channel):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(Genkai_log_ID)
        if before.channel is None:
            msg = f'{member.name} が {after.channel.name} 参加'
            await alert_channel.send(msg)
        elif after.channel is None:
            msg = f'{member.name} が {before.channel.name} 退出'
            await alert_channel.send(msg)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
