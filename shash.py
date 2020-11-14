
from  os import system
from time import sleep
sleep(1)
system("clear")
print("""/$$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$  /$$_____/ /$$_____/ |____  $$ /$$__  $$ /$$__ |  $$$$$$ | $$        /$$$$$$$| $$  \__/| $$$$  \____  $$| $$       /$$__  $$| $$      | $$__  /$$$$$$$/|  $$$$$$$|  $$$$$$$| $$      |  $$$ |_______/  \_______/ \_______/|__/       \____""")
sleep(2)
print("""▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒
▒▒█▒▒▒▄██████████▄▒▒▒▒
▒█▐▒▒▒████████████▒▒▒▒
▒▌▐▒▒██▄▀██████▀▄██▒▒▒
▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒
▐┼▐▒▒██████████████▒▒▒
▐▄▐████─▀▐▐▀█─█─▌▐██▄▒
▒▒█████──────────▐██
▒▒█▀▀██▄█─▄───▐─▄███▀▒
▒▒█▒▒███████▄██████▒▒▒
▒▒▒▒▒██████████████▒▒▒
▒▒▒▒▒██████████████▒▒▒
▒▒▒▒▒█████████▐▌██▌▒▒▒
▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ """)
sleep(2)
print ("--------------tool by segun-balleriv")
sleep(1)
print("-------------------------------------")
sleep(1)
print(">>>>>>>>>>> on github @segun-balleriv")
sleep(1)
print("-------------------------------------")
sleep(1)
print(">>>>>>>> on Facebook @anonghostballer")
sleep (1)
print ("-------------------------------------")
sleep(1)
print(">>> on Instagram @shegzyy_official404")
system(" clear")
sleep(1)
print(" $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
sleep(1)
print("-_-_-_-_-_-_-_-_-_-_-_-_welcome-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
sleep(1)
print(" $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
sleep(1)
import sys
sleep(1)
x=input("type n to see the system you are using >>> ")
if  x =="n":
	print(sys.platform)
else:
	print("wrong option...retype first command")
print (" please wait while process is loading....... tool by Segun")
sleep(6)
system(" clear")
sleep (1)
print("""________  ____ ___  ______   / ___/ _ \/ __ `/ / / / __ \  (__  )  __/ /_/ / /_/ / / / / /____/\___/\__, /\__,_/_/ /_/           /____/""")
sleep (1)

flag = 0
pass_hash = input ( "enter md5 hash>> " )
sleep (1)
wordlist = input( "File name>>> " )
sleep (2)
try :
	pass_file = open (wordlist, "r" )
except :
	print( "No file found :(" )
quit()
for word in pass_file:
	enc_wrd = word.encode( 'utf-8' )
digest = hashlib.md5(enc_wrd.strip()).hexdigest()
# print(word)
# print(digest)
# print(pass_hash)
if digest.strip() == pass_hash.strip():
	print( "password found" )
	print( "Password is " + word)
	flag = 1		
if flag == 0 :
	print("password not in list")
quit()