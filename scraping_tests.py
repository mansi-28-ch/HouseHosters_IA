# trial 1:
import requests
from bs4 import BeautifulSoup

url="https://www.airbnb.com/s/Stuttgart--Germany/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-12-01&monthly_length=3&price_filter_input_type=0&channel=EXPLORE&query=Stuttgart%2C%20Germany&date_picker_type=calendar&checkin=2023-12-01&checkout=2023-12-09&adults=1&source=structured_search_input_header&search_type=autocomplete_click&price_filter_num_nights=1&zoom_level=15&place_id=ChIJ04-twTTbmUcR5M-RdxzB1Xk"
from IPython.display import IFrame
IFrame (src=url,width='100%', height='300px')

answer = requests.get(url)

soup = BeautifulSoup(answer.content,'html.parser')

#print(soup.prettify())

listings=soup.findAll('span','r1dxllyb dir dir-ltr')

for i in range(len(listings)):
    new=listings[i].get_text()
    print(new)



# trial 2 (generated)




from bs4 import BeautifulSoup
from urllib.request import urlopen

url = ('https://www.airbnb.com/rooms/606801579780717669?source_impression_id=p3_1701245339_FFeQadf3JxBkC%2BuR')

# Open the page
page = urlopen(url)

# Read HTML as string and assign to html variable
html = page.read().decode("utf-8")

print(html)

# Create BeautifulSoup object and assign to soup variable
soup = BeautifulSoup(html, "html.parser")


# Find the element containing the rating using the appropriate class or tag
try:
    element = soup.find('span[data-testid="t1rl3yjt dir dir-ltr"]')
    text_data = element.text

    #span.t1r|3yjt.dir.dir-Itr

    #rating_element = soup.select_one('r1lutz1s dir dir-ltr')
    #rating = rating_element.text.strip()
    print(f'The property has a rating of: {text_data}')
except Exception as e:
    print(f'Error: {e}')




# trial 3



from bs4 import BeautifulSoup
from urllib.request import urlopen

url = ('https://www.airbnb.com/rooms/606801579780717669?source_impression_id=p3_1701245339_FFeQadf3JxBkC%2BuR')

# Open the page
page = urlopen(url)

# Read HTML as string and assign to html variable
html = page.read().decode("utf-8")

print(html)

# Create BeautifulSoup object and assign to soup variable
soup = BeautifulSoup(html, "html.parser")


# Find the element containing the rating using the appropriate class or tag
try:
    element = soup.find('span[data-testid="t1rl3yjt dir dir-ltr"]')
    text_data = element.text

    #span.t1r|3yjt.dir.dir-Itr

    #rating_element = soup.select_one('r1lutz1s dir dir-ltr')
    #rating = rating_element.text.strip()
    print(f'The property has a rating of: {text_data}')
except Exception as e:
    print(f'Error: {e}')

Error output:
Error: 'NoneType' object has no attribute 'text'


Selenium scrape script:

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.airbnb.com/rooms/606801579780717669?source_impression_id=p3_1701245339_FFeQadf3JxBkC%2BuR'

# Setup webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open the page
driver.get(url)

# Find the element containing the rating using the appropriate class
try:
    rating_element = driver.find_element('css selector', 'span[class*="a8jt5op"]')
    rating = rating_element.text.strip()
    print(f'The property has a rating of: {rating}')
except Exception as e:
    print(f'Error: {e}')

# Close the browser
driver.quit()

