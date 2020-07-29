from bs4 import BeautifulSoup
from collections import Counter
import requests
import itertools
import math



urls = ["https://www.nebo.edu/",
"http://landmark.nebo.edu/adult-ed/",
"https://www.nebo.edu/athletics",
"https://www.nebo.edu/board-education",
"http://cte.nebo.edu/",
"https://www.nebo.edu/child-nutrition",
"https://www.nebo.edu/pr",
"https://www.nebo.edu/community-school",
"https://www.nebo.edu/curriculum",
"https://www.nebo.edu/elementary",
"https://www.nebo.edu/federal-programs",
"https://www.nebo.edu/finance",
"https://www.nebo.edu/finance/payroll",
"https://www.nebo.edu/finance",
"https://www.nebo.edu/hr",
"https://www.nebo.edu/employees",
"https://tcplus.nebo.edu/app/webclock/#/EmployeeLogOn",
"https://nebout.infinitecampus.org/campus/nebo.jsp",
"https://finweb.nebo.edu/ESP/",
"https://dbweb.nebo.edu/",
"https://nebo.parentlink.net/",
"https://login.frontlineeducation.com/login?signin=e2a1a70a5d16a308ffa6b62011bbd34e&productId=ABSMGMT&clientId=ABSMGMT#/login",
"https://dbweb.nebo.edu/?Nebo_return_app=/etcapp/user",
"https://www.observertab.net/index.php/v3/login",
"https://www.nebo.edu/schools/boundaries",
"https://www.nebo.edu/schools/websites?different=",
"http://goshen.nebo.edu/",
"http://hobblecreek.nebo.edu/",
"http://mapleridge.nebo.edu/",
"http://mapleton.nebo.edu/",
"http://mmhs.nebo.edu/",
"http://barnett.nebo.edu/",
"http://parkview.nebo.edu/",
"http://springlake.nebo.edu/",
"http://taylor.nebo.edu/",
"http://wilson.nebo.edu/",
"http://mnjhs.nebo.edu/",
"http://pjhs.nebo.edu/",
"http://phs.nebo.edu/",
"http://foothills.nebo.edu/",
"http://mtloafer.nebo.edu/",
"http://salem.nebo.edu/",
"http://sajhs.nebo.edu/",
"http://shhs.nebo.edu/",
"http://applevalley.nebo.edu/",
"http://orchardhills.nebo.edu/",
"http://santaquin.nebo.edu/",
"http://brockbank.nebo.edu//",
"http://canyon.nebo.edu/",
"http://eastmeadows.nebo.edu/",
"http://larsen.nebo.edu/",
"http://park.nebo.edu/",
"http://rees.nebo.edu/",
"http://riverview.nebo.edu/",
"http://sierrabonita.nebo.edu/",
"http://spanishoaks.nebo.edu/",
"http://dfjhs.nebo.edu/",
"http://sfjhs.nebo.edu/",
"http://sfhs.nebo.edu/",
"http://mmhs.nebo.edu/",
"http://artcity.nebo.edu/",
"http://brookside.nebo.edu/",
"http://cherrycreek.nebo.edu/",
"http://meadowbrook.nebo.edu/",
"http://sagecreek.nebo.edu/",
"http://westside.nebo.edu/",
"http://sjhs.nebo.edu/",
"http://shs.nebo.edu/",
"http://landmark.nebo.edu/adult-ed/",
"http://alc.nebo.edu/",
"http://legacy.nebo.edu/",
"http://oakridge.nebo.edu/",
"http://summitcenter.nebo.edu/",
"https://www.nebo.edu/do",
"http://alc.nebo.edu/",
"https://www.nebo.edu/schools/status",
"https://www.nebo.edu/node/2848",
"https://www.nebo.edu/coronavirus",
"https://www.nebo.edu/information/calendar",
"http://www.nebo.edu/frontpage",
"https://www.nebo.edu/information/open_enrollment",
"https://www.nebo.edu/node/416",
"http://www.nebo.edu/pubpolicy/",
"https://www.nebo.edu/research",
"https://www.nebo.edu/information/vision",
"http://www.nebo.edu/information/reportcard/",
"https://www.nebo.edu/information/civil_info",
"https://www.nebo.edu/parents",
"https://nebout.infinitecampus.org/campus/portal/parents/nebo.jsp",
"http://www.nebo.edu/child-nutrition/payment",
"https://www.nebo.edu/students",
"https://www.nebo.edu/registration",
"https://apply.nebo.edu/applicant/home.php",
"https://www.facebook.com/NeboSchoolDistrict/",
"https://twitter.com/NeboDistrict",
"https://www.youtube.com/channel/UCnfAb7ngf4QyG6ACUNKLAAw",
"https://www.instagram.com/NeboSchoolDistrict/",
"https://www.instagram.com/SuperintendentRickNielsen/",
"https://www.facebook.com/NeboBus/",
"https://www.nebo.edu/espanol"
]


all_urls_list = []

for url in urls:
  response = requests.get(url)
  soup = BeautifulSoup(requests.get(url).text, "html.parser")

  foundUrls = ([url["href"] for url in soup.find_all("a",href=lambda href: href and not href.startswith("#"))])
  all_urls_list.append(foundUrls)

all_urls_list = list(itertools.chain.from_iterable(all_urls_list ))

dict_of_urls = dict(Counter(all_urls_list))
dict_of_urls = { key:value for key, value in dict_of_urls.items()}
for key, value in reversed(sorted(dict_of_urls.items(), key=lambda item: item[1])):
  print("%s: %s" % (key, value))
sorted_list = list(reversed(sorted(dict_of_urls.items(), key=lambda x: x[1])))

total_urls = len(dict_of_urls)
half_slice = math.floor(total_urls/2)
first_half_urls = sorted_list[:half_slice]
last_half_urls = sorted_list[half_slice:(half_slice + 1)] + sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]


print("______")
print("______")
print("______")
print("______")
print("The median is : % s " % (sorted_list[half_slice:(half_slice + 1)]))
print("The total urls found is : % s " % (total_urls))
print("______")
print("______")
print("______")
print("______")
print(first_half_urls)
print("______")
print("______")
print("______")
print("______")
print("______")
print(last_half_urls)

