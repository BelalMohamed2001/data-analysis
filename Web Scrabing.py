import requests
from bs4 import BeautifulSoup
import csv

date=input("Enter your date in format MM/DD/YEAR: ")
page=requests.get(f"https://www.yallakora.com/match-center/?date={date}")# to get page data from wedsite

def main(page):
    src=page.content# to get the content opf bage
    soup=BeautifulSoup(src,"lxml")# to make the content can read and make it as html from xml parsing
    

    matches_deatails=[] # to save data
    championships= soup.find_all("div",{'class':'matchCard'}) #  to find all divs has class matchcard get more than one dive like list


    def get_match(championships):
        championships_title=championships.contents[1].find("h2").text.strip()
        # contents is array list has childe elemnt of parent elemnt 1 is tilte in some websites 0 is the first child so use try and error
        # text to get text inside tag <h2>
        # strip to rempve spaces in right and in left
        # always use try and error
        all_matches = championships.contents[3].find_all("div",{'class': 'item future liItem'}) # try and error [2] ot [3]
        number_of_matches=len(all_matches)

        for i in range(number_of_matches):
            #getteamA
            team_A=all_matches[i].find('div',{'class':'teamA'}).text.strip()
            team_B=all_matches[i].find('div',{'class':'teamB'}).text.strip()

            #get_score
            match_result=all_matches[i].find('div',{'class':'MResult'}).find_all('span',{'class':'score'})
            score=f"{match_result[0].text.strip()} - {match_result[1].text.strip()} "

            #gettime
            time=all_matches[i].find('div',{'class':'MResult'}).find('span',{'class':'time'}).text.strip()
            

            # add info to match details list
            matches_deatails.append({"نوع البطولة":championships_title,"الفريق الاول":team_A,"الفريق الثاني":team_B,
                                     "ميعاد المباراة":time,"النتيجة":score})
            

    
    for i in range (len(championships)):
       get_match(championships[i])# to get first div only

    keys=matches_deatails[0].keys()# get the keys of dic to be headers
    with open('C:/Users/belal/Downloads/mean/1.csv', 'w', newline='', encoding='utf-8') as output:
        dic_writer=csv.DictWriter(output,keys) # dic writer is class
        dic_writer.writeheader()# to make keys in header
        dic_writer.writerows(matches_deatails)# to make rows for match tje values of dic values only
        print("file is created")

main(page)

