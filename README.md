# AttainU_Projects
#Requirements:
Installation:
    Install Python3,
    install pip install requests==2.18.4 
    Install IFTTT Mobile app
    Install Telegram app

Two Important things to be done in IFTTT app:
    1)creating an applet for reciving "Bitcoin Price Notifications"
    2)creating an applet for reciving "Bitcoin Emergency Price notification"
Steps to be followed in creating "Bitcoin Price Notifications" IFTTT applet:-
    1)Choose "Get more" option in IFTTT app
    2)Scrolldown and you can find "Make your own applet form scratch" choose that option
    3)prompted with IF This Then That
    4)choose "+This" and search "webhooks"  and select 'webhooks'
    5)Select "Recive web request " option
    6)prompted with "Event Name" edit text box & Enter eventname as "Bitcoin_Tracker"
    7)Redirected to applet page and select "+That "option & search for "telegram" and select it 
    8)promted with many options select "send message"option
    9)In next page, following needs to done
        -->select target chat as "Private chat with @IFTTT",
        -->In Message format it to the following format
                "Latest Bitcoin Price :-<br>
                {{Value1}}"
        -->Select noting for "Include web page preview"
    10)choose "recive notification when this runs" if you want to recive nofification when code is up and running.
Steps to be followed in creating "Bitcoin Emergency Price notification" IFTTT applet:-
    1)Choose "Get more" option in IFTTT app
    2)Scrolldown and you can find "Make your own applet form scratch" choose that option
    3)prompted with IF This Then That
    4)choose "+This" and search "webhooks"  and select 'webhooks'
    5)Select "Recive web request " option
    6)prompted with "Event Name" edit text box & Enter eventname as "Bitcoin_Tracker"
    7)Redirected to applet page and select "+That "option & search for "Notification" and select it 
    8)promted with many options select "send a rich notification from the IFTTT app"option
    9)In next page, following needs to done
            -->set Title as "Bitcoin Emergency Price"
            -->Message as 
            "Bitcoin price is at ${{Value1}},Buy or Sell now."
            -->Link URL as "https://coinmarketcap.com/currencies/bitcoin"
            -->Image URL is optional,
            -->Select "save"
    10)Finish setting up
