# shopping_helper
#### Description:
This program is supposed to help me find items on sale in my local neighbourhood stores. Then, it suggests some recipes for me too chose from using the chosen item. 
Firstly, it uses beautiful soup to parse the html from the webpages I selected. I chose three stores, Ica, Lidl, and Coop.
Secondly, each store has a class of functions that gets the data I want: the item on sale. Each of the class' drivers then return the items as a list.
Thirdly, the list is then printed to terminal.
Then, the user is prompted to choose an item and type it into the terminal.
The recipe class then searches on a popular recipe site. If there the search doesn't return any recipes for the item, the user is prompted again.
The class driver then returns the ten topmost recipes as well as links to the recipe. I divided the links and the title of the recipe into two different loops that are then joined with zip(). Unfortunately, I did not manage to get both the title and the link in the same loop. I think this might not be optimal, but it looked cleaner to have the functions split into two functions instead of making one bigger but messier one. 
To fullfill all the requirements for the project, I wrote three functions to implement the classes. 
Finally, the user is promted to search for more recipes until the user commits EOF.
I realized testing a webscraper tool was very difficult, so I just tried testing that the functions actually output something which I considered good enough.
