api_key =                   # your coinbase api-key
api_secret =                # your coinbase api secret
period = 60                 # number of seconds to ping for prices and financial analisys
pair = "LTC-EUR"            # crypto currency and currency for trading operations
lengthOfMA = 120            # dimension of periods (120 x period of sampling)
market_fees = 0.15          # coinbase per-transaction fee in dollars
min_profit_margin = 3     	# minimum % increase before we sell out 
strategy = "Combined"       # classic, MACD, RSI, Combined # not completed
webserver = False          	# activate web server and chart report on http://localhost/index.html
interpolation = "yes"		    # lines become smooth
graphical = True			      # trace a chart of operation and signaling system  
