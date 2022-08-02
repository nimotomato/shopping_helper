from bs4 import BeautifulSoup
import requests
import re
import sys
#A program intended to find items on sales in stores I frequent and then search using the item.

def soup_getter(n):
    """Global function, gets soup"""
    url = n
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html5lib")
    return soup


class Ica:
    def get_soup():
        """gets the soup"""
        return soup_getter("https://www.ica.se/butiker/maxi/malmo/maxi-ica-stormarknad-malmo-2748/erbjudanden/")


    def get_deals(url):
        """gets all deals"""
        list = ["ICA"]
        for row in url.find_all(class_="offer-type__product-details"):
            deals = row.h2.text
            list.append(deals.strip())
        return list

    
    def driver():
        """runs functions in order"""
        return Ica.get_deals(Ica.get_soup())


class Lidl:  
    def get_soup():
        """gets soup for lidl"""
        return soup_getter("https://www.lidl.se/c/mandag-sondag/c4048/w1")

       
    def get_deals(url):
        """gets all basic deals"""
        list = ["LIDL"]
        for row in url.find_all("h3", class_="ret-o-card__headline"):
            list.append(row.text.strip())
        return list


    def driver():    
        return Lidl.get_deals(Lidl.get_soup())


class Coop:
    def get_soup():
        return soup_getter("https://www.coop.se/216535")

    def get_deals(soup):
        list = ["COOP"]
        for row in soup.find_all("div", class_="ItemTeaser-info"):
            deals = row.h3.text
            list.append(deals)
        return list

    def driver():
        return Coop.get_deals(Coop.get_soup())
        

class Recipes:
    """gets the soup from recipe book"""
    def get_soup(s):
        return soup_getter(f"https://www.tasteline.com/sok/{s}")


    def show(soup):
        """gets 10 recipe heads"""
        list = []
        for row in soup.find_all("h3"):
            if len(list) < 10:
                row = row.text
                list.append(row + "\n")
            else:
                return list


    def links(soup):
        """gets the recipe links"""
        list = []
        for row in soup.find_all(class_="u-block u-no-underline u-flex-grow"):
            if len(list) < 10:
                if matches := re.search(r"href=\"(.+)\"(?:.+?)", str(row)):
                    list.append(matches.group(1))
        return list


    def output(r1, r2):
        """combines the recipe lists"""
        list = []
        for n, h in zip(r1, r2):
            list.append(f"{n}{h}\n")
        return list


    def driver(s):
        """driver for recipes"""
        url = Recipes.get_soup(s)
        r1 = Recipes.show(url)
        r2 = Recipes.links(url)
        list = Recipes.output(r1, r2)
        return list


def main():
    print("Please, wait a moment to see the items on sale: ")
    for item in Ica.driver():
        print(item)
    print("")
    
    for item in Lidl.driver():
        print(item)
    print("")

    for item in Coop.driver():
        print(item)
    print("")

    while True:
        try:
            while True:
                choice = input("What item would you like to see recipes of?")
                print("")
                for i in Recipes.driver(choice):
                    print(i)
        except ValueError:
            print("No recipe found.")
            continue
        except TypeError:
            print("No recipe found.")
            continue
        except EOFError:
            sys.exit("Thank you for browsing!")
                     
    

if __name__ == "__main__":
    main()
