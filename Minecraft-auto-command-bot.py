import DiscordFunctions
import time



Token = input("Tokeni Giriniz:")
Kanalid='1085908186537668608'



while True:
    if(DiscordFunctions.MadenKontrol(Token,Kanalid)):
        DiscordFunctions.SendMessage(Token,Kanalid,"!sil")
        time.sleep(3)
        DiscordFunctions.SendMessage(Token,Kanalid,"<@520282851925688321> m")
        time.sleep(3)
        DiscordFunctions.SendMessage(Token,Kanalid,"<@520282851925688321> m")
        time.sleep(2)
    if(DiscordFunctions.Kazmakontrol(Token,Kanalid)):
        time.sleep(2)
        DiscordFunctions.SendMessage(Token,Kanalid,'<@520282851925688321> repair')
        time.sleep(2)
        DiscordFunctions.SendMessage(Token,Kanalid,"!sil")
        time.sleep(1)
        DiscordFunctions.SendMessage(Token,Kanalid,"<@520282851925688321> m")
    time.sleep(1)
