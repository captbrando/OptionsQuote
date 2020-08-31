# OptionsQuote README

Google Sheets has some awesome integrations to track stock trading. Pulling a live (or near live) quote and then doing calculations (like modeled gains/losses) is pretty sweet. Sure, it's not a trading platform, but for a basic trading strategy it can be very useful. The one problem (that is WELL documented at this point) is that you cannot reliably get option quotes in your sheet. It's really sneaky. You drop a quick importhtml() in a cell and it works for a few minutes, but then it quickly barfs and goes #N/A on you.

So I got to playing around. I've been working with basic web scrapers for a few months and decided to really fix this. So this little script is basically a helper for Google Sheets to get the extra functionality I need to reliably pull options quotes.

Few assumptions or notes:

* This is a python script. You can run it locally or configure it to be a web service. By default, that's what it is doing (it expects to be called as a URI with one value "c" that equals the option contract you want).
* To configure it locally, you would need to modify the top to accept an argument (the contract ticker symbol).
* In order to get Google Sheets to refresh, you need to build a quick script and trigger to create a random value and rebuild your urls. [I used this one](http://stackoverflow.com/a/33875957/1677912) as my guide and it works great. Since the script ignores any other value you pass it, you can simply add a variable to send that random number in.
* You need to create a time-based trigger to run the script periodically. If you want to pass the random value into the script for tracking you can. It will guarantee that Google sheets sees it as a new formula and calculates it. Just be careful not to abuse this and get blocked.

## Google Sheets integration
If you are integrating with Google Sheets, you need a formula to call the script. I found the `=IMPORTXML()` function to be the most reliable. The assumption in my case is that the above random value script will put the random value in cell T1, so I pass that in as an argument to ensure things refresh. Here's an example to get you started:

`=importxml(concatenate("https://www.example.net/path/to/optprice.py?c=",B4,"&rand=",$T$1), "//body"),0)`

Then it just comes down to formatting the cells and boom. You will also need to create a time-based trigger to run the

## Bugs & Contact
This script is provided to you free of charge with no expressed or implied warranty. USE AT YOUR OWN RISK. To file a bug, suggest a patch, or contact me, [visit GitHub](https://github.com/captbrando/OptionsQuote/).
