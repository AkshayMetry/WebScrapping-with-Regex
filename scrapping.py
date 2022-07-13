# import webbrowser
# webbrowser.open('https://suvenconsultants.com//')

str = """
<body>
<div id="listings_prices">
<div class="item">
<li class="item_name">Watch</li>
<div class="main_price"> 5464646465 </div>
	<div class="discounted_price"> Discounted Price : $56.68 </div>
</div>
<div class="item">
<li class="item_name">Watch2</li>
<div class="main_price"> Price : $56.68 </div>
</div>
</body>
"""

import bs4
textDataForParsing = bs4.BeautifulSoup(str, features='lxml')  
# lxml is specification for the parser.
# default is html.parser
elements = textDataForParsing.select('div.main_price')
print(elements)