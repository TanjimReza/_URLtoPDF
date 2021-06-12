#--------------------- Requirements ---------------------#
from discord import file
import requests
import discord
from discord.ext import commands
import asyncio
import pdfkit
from PyPDF2 import PdfFileReader, PdfFileWriter
#--------------------------------------------------------#

#Setting Bot Command 
bot = commands.Bot(command_prefix='>')

#---------------------- Necessary Variables ----------------------#
LOG_CHANNEL_ID = 853294509340622906 #Bot will print logs in this channel 
BOT_TOKEN = "ODUyOTQ3NzAyMDA1ODkxMTAy.YMOPcw.KOcym0-UOkjbMHrJiQ1slq8bYjI"
ONLINE_MESSAGE = "Bot Online!"
PDF_NAME = "" #Important? Check below
#-----------------------------------------------------------------#



#Sending Starting Message 
@bot.event
async def on_ready():
	channel = bot.get_channel(LOG_CHANNEL_ID)
	await channel.send(ONLINE_MESSAGE)
	print("Bot Online message sent!")
	await bot.change_presence(activity=discord.Game(name="PDFing"))
	print("Set Online Activity")
	await channel.send("Ready to make PDF")
#----------------------------------------------------------#

#Getting Command From User 
@bot.command()
async def mpdf(ctx, arg):
	tempMessage = await ctx.message.reply("Process started, Please wait...")
	url = arg
	authorName = ctx.message.author.name
	PDF_NAME = url + authorName + ".pdf"
	print("Current URL:", url)
	print("URL to PDF: ", url)
	pdf = pdfkit.from_url(url,False)
	# Need to write as bytes 
	with open(PDF_NAME,'wb') as f: 
		f.write(pdf)
		f.close()
	#>>>> In this stage our PDF Creation is complete <<<<# 
	# PDF Cropping is not necessary, if required we can create another command 
	# The Code for PDF Creation is commented out below 
	
	print("PDF Creation Complete!")
	
#--------------------------------------------------------------#	
	
	#----------------------------------------------------------#
	#--------------Optional PDF Cropping ----------------------#
	#----------------------------------------------------------#
	
	###### Initiating PDF Cropping ######
	# reader = PdfFileReader(PDF_NAME,'r')
	# print("PDF Opened..\n")
	# print("Number of pages:",reader.getNumPages())

	# #Setting Current Page to Page 1
	# page = reader.getPage(0)
	# print("Current Page=",page)
	# #Getting Upper Left Co-Ordinates 
	# upperLeft = page.cropBox.getUpperLeft()
	# print("upperLeft:", upperLeft)
	# #Changing Upper Left Co-Ordinates
	# upperLeftList = list(upperLeft)
	# upperLeftListChangedRight = int(upperLeftList[1] - 50)
	# #Changed Co-Ordinates
	# print("Changed:",upperLeftList[0],upperLeftListChangedRight)
	# #Getting Upper Right Co-Ordinates
	# upperRight = page.cropBox.getUpperRight()
	# print("upperRight:", upperRight)
	# #Changing Upper Right Co-Ordinates
	# upperRightList = list(upperRight)
	# upperRightListChangedRight = int(upperRightList[1] - 50)
	# #Changed Co-Ordinates
	# print("Changed:",upperRightList[0],upperRightListChangedRight)
	# print("Got Co-Ordinates")
	# ################################################################


	# ###### Cropping PDF ######
	# writer = PdfFileWriter()
	# #Cropping first page only
	# page = reader.getPage(0)
	# page.mediaBox.setUpperLeft((upperLeftList[0],upperLeftListChangedRight))
	# page.mediaBox.setUpperRight((upperRightList[0],upperRightListChangedRight))
	# writer.addPage(page)
	# print("First Page Cropped.")
	# #Adding other pages without cropping 
	# for i in range(1,reader.getNumPages()):
	# 	page = reader.getPage(i)
	# 	writer.addPage(page)
	# 	#output
	# print("Other pages done!")
	# outstream = open(PDF_NAME,'wb')
	# writer.write(outstream)
	# outstream.close()
	# print("PDF Cropping Completed!")
#--------------------------------------------------------------#




	#----------------------------------------------------------#
	#------------- Creating Embed Message to send  ------------#
	#----------------------------------------------------------#	

	embed=discord.Embed(title="URLToPDF", description="Turning your URLs into PDF")
	embed.set_author(name="Tanjim Reza", icon_url="https://i.pinimg.com/originals/25/73/26/257326e230467a71781d564ee22fa906.jpg")
	embed.set_thumbnail(url="https://s4.gifyu.com/images/AgedPlainCornsnake-mobile.gif")
	embed.add_field(name="Given Link:", value=arg, inline=True)
	#Getting Command issuer to mention in Embed
	mention = ctx.author.mention
	embed.add_field(name="Command issuer:", value=mention,inline=True)
	embed.add_field(name="PDF of Website:",value="Attached below")
	messageInfo = "The bot currently has limited functionality. \n [WIP] User verification and adding role depending on Sheets Data \n [WIP] Custom User-Agent"
	embed.add_field(name="About:",value=messageInfo,inline=False)
	print("Created Embed!")


	await ctx.send(embed=embed)
	print("Embed SENT!")
	await ctx.send(file=discord.File(PDF_NAME))
	print("PDF File SENT!")
	print("DONE!")
	await tempMessage.delete()
	await ctx.message.add_reaction("✅")
	await ctx.message.add_reaction("☑️")
#----------------------------------------------------------#

print("Initating BOT")
bot.run(BOT_TOKEN)





