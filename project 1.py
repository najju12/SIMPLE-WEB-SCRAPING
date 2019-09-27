Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> import bs4
>>> import pandas as pd
>>> res=requests.get('https://www.imdb.com/list/ls000049962/')
>>> soup=bs4.BeautifulSoup(res.text,'lxml')
>>> p=soup.select('h3.lister-item-header')
>>> p
[<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">1.</span>
<a href="/title/tt0111161/">The Shawshank Redemption</a>
<span class="lister-item-year text-muted unbold">(1994)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">2.</span>
<a href="/title/tt0068646/">The Godfather</a>
<span class="lister-item-year text-muted unbold">(1972)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">3.</span>
<a href="/title/tt0071562/">The Godfather: Part II</a>
<span class="lister-item-year text-muted unbold">(1974)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">4.</span>
<a href="/title/tt0060196/">Il buono, il brutto, il cattivo</a>
<span class="lister-item-year text-muted unbold">(1966)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">5.</span>
<a href="/title/tt0110912/">Pulp Fiction</a>
<span class="lister-item-year text-muted unbold">(1994)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">6.</span>
<a href="/title/tt0108052/">Schindler's List</a>
<span class="lister-item-year text-muted unbold">(1993)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">7.</span>
<a href="/title/tt0050083/">12 Angry Men</a>
<span class="lister-item-year text-muted unbold">(1957)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">8.</span>
<a href="/title/tt1375666/">Inception</a>
<span class="lister-item-year text-muted unbold">(2010)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">9.</span>
<a href="/title/tt0073486/">One Flew Over the Cuckoo's Nest</a>
<span class="lister-item-year text-muted unbold">(1975)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">10.</span>
<a href="/title/tt0468569/">The Dark Knight</a>
<span class="lister-item-year text-muted unbold">(2008)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">11.</span>
<a href="/title/tt0080684/">Star Wars: Episode V - The Empire Strikes Back</a>
<span class="lister-item-year text-muted unbold">(1980)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">12.</span>
<a href="/title/tt0167260/">The Lord of the Rings: The Return of the King</a>
<span class="lister-item-year text-muted unbold">(2003)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">13.</span>
<a href="/title/tt0047478/">Shichinin no samurai</a>
<span class="lister-item-year text-muted unbold">(1954)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">14.</span>
<a href="/title/tt0137523/">Fight Club</a>
<span class="lister-item-year text-muted unbold">(1999)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">15.</span>
<a href="/title/tt0099685/">Goodfellas</a>
<span class="lister-item-year text-muted unbold">(1990)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">16.</span>
<a href="/title/tt0076759/">Star Wars</a>
<span class="lister-item-year text-muted unbold">(1977)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">17.</span>
<a href="/title/tt0034583/">Casablanca</a>
<span class="lister-item-year text-muted unbold">(1942)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">18.</span>
<a href="/title/tt0317248/">Cidade de Deus</a>
<span class="lister-item-year text-muted unbold">(2002)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">19.</span>
<a href="/title/tt0120737/">The Lord of the Rings: The Fellowship of the Ring</a>
<span class="lister-item-year text-muted unbold">(2001)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">20.</span>
<a href="/title/tt0064116/">Once Upon a Time in the West</a>
<span class="lister-item-year text-muted unbold">(1968)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">21.</span>
<a href="/title/tt0047396/">Rear Window</a>
<span class="lister-item-year text-muted unbold">(1954)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">22.</span>
<a href="/title/tt0082971/">Raiders of the Lost Ark</a>
<span class="lister-item-year text-muted unbold">(1981)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">23.</span>
<a href="/title/tt0054215/">Psycho</a>
<span class="lister-item-year text-muted unbold">(1960)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">24.</span>
<a href="/title/tt0114814/">The Usual Suspects</a>
<span class="lister-item-year text-muted unbold">(1995)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">25.</span>
<a href="/title/tt0102926/">The Silence of the Lambs</a>
<span class="lister-item-year text-muted unbold">(1991)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">26.</span>
<a href="/title/tt0114369/">Se7en</a>
<span class="lister-item-year text-muted unbold">(1995)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">27.</span>
<a href="/title/tt0038650/">It's a Wonderful Life</a>
<span class="lister-item-year text-muted unbold">(1946)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">28.</span>
<a href="/title/tt0209144/">Memento</a>
<span class="lister-item-year text-muted unbold">(2000)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">29.</span>
<a href="/title/tt0435761/">Toy Story 3</a>
<span class="lister-item-year text-muted unbold">(2010)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">30.</span>
<a href="/title/tt0167261/">The Lord of the Rings: The Two Towers</a>
<span class="lister-item-year text-muted unbold">(2002)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">31.</span>
<a href="/title/tt0043014/">Sunset Blvd.</a>
<span class="lister-item-year text-muted unbold">(1950)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">32.</span>
<a href="/title/tt0109830/">Forrest Gump</a>
<span class="lister-item-year text-muted unbold">(1994)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">33.</span>
<a href="/title/tt0110413/">Léon</a>
<span class="lister-item-year text-muted unbold">(1994)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">34.</span>
<a href="/title/tt0057012/">Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb</a>
<span class="lister-item-year text-muted unbold">(1964)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">35.</span>
<a href="/title/tt0078788/">Apocalypse Now</a>
<span class="lister-item-year text-muted unbold">(1979)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">36.</span>
<a href="/title/tt0033467/">Citizen Kane</a>
<span class="lister-item-year text-muted unbold">(1941)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">37.</span>
<a href="/title/tt0053125/">North by Northwest</a>
<span class="lister-item-year text-muted unbold">(1959)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">38.</span>
<a href="/title/tt0169547/">American Beauty</a>
<span class="lister-item-year text-muted unbold">(1999)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">39.</span>
<a href="/title/tt0120586/">American History X</a>
<span class="lister-item-year text-muted unbold">(1998)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">40.</span>
<a href="/title/tt0075314/">Taxi Driver</a>
<span class="lister-item-year text-muted unbold">(1976)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">41.</span>
<a href="/title/tt0103064/">Terminator 2: Judgment Day</a>
<span class="lister-item-year text-muted unbold">(1991)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">42.</span>
<a href="/title/tt0120815/">Saving Private Ryan</a>
<span class="lister-item-year text-muted unbold">(1998)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">43.</span>
<a href="/title/tt0052357/">Vertigo</a>
<span class="lister-item-year text-muted unbold">(1958)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">44.</span>
<a href="/title/tt0078748/">Alien</a>
<span class="lister-item-year text-muted unbold">(1979)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">45.</span>
<a href="/title/tt0211915/">Amélie</a>
<span class="lister-item-year text-muted unbold">(2001)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">46.</span>
<a href="/title/tt0910970/">WALL·E</a>
<span class="lister-item-year text-muted unbold">(2008)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">47.</span>
<a href="/title/tt0245429/">Sen to Chihiro no kamikakushi</a>
<span class="lister-item-year text-muted unbold">(2001)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">48.</span>
<a href="/title/tt0081505/">The Shining</a>
<span class="lister-item-year text-muted unbold">(1980)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">49.</span>
<a href="/title/tt0050825/">Paths of Glory</a>
<span class="lister-item-year text-muted unbold">(1957)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">50.</span>
<a href="/title/tt0056172/">Lawrence of Arabia</a>
<span class="lister-item-year text-muted unbold">(1962)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">51.</span>
<a href="/title/tt0253474/">The Pianist</a>
<span class="lister-item-year text-muted unbold">(2002)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">52.</span>
<a href="/title/tt0036775/">Double Indemnity</a>
<span class="lister-item-year text-muted unbold">(1944)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">53.</span>
<a href="/title/tt0066921/">A Clockwork Orange</a>
<span class="lister-item-year text-muted unbold">(1971)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">54.</span>
<a href="/title/tt0021749/">City Lights</a>
<span class="lister-item-year text-muted unbold">(1931)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">55.</span>
<a href="/title/tt0405094/">The Lives of Others</a>
<span class="lister-item-year text-muted unbold">(2006)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">56.</span>
<a href="/title/tt0022100/">M - Eine Stadt sucht einen Mörder</a>
<span class="lister-item-year text-muted unbold">(1931)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">57.</span>
<a href="/title/tt0407887/">The Departed</a>
<span class="lister-item-year text-muted unbold">(2006)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">58.</span>
<a href="/title/tt0056592/">To Kill a Mockingbird</a>
<span class="lister-item-year text-muted unbold">(1962)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">59.</span>
<a href="/title/tt0090605/">Aliens</a>
<span class="lister-item-year text-muted unbold">(1986)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">60.</span>
<a href="/title/tt0947798/">Black Swan</a>
<span class="lister-item-year text-muted unbold">(2010)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">61.</span>
<a href="/title/tt0338013/">Eternal Sunshine of the Spotless Mind</a>
<span class="lister-item-year text-muted unbold">(2004)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">62.</span>
<a href="/title/tt0180093/">Requiem for a Dream</a>
<span class="lister-item-year text-muted unbold">(2000)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">63.</span>
<a href="/title/tt0082096/">Das Boot</a>
<span class="lister-item-year text-muted unbold">(1981)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">64.</span>
<a href="/title/tt0041959/">The Third Man</a>
<span class="lister-item-year text-muted unbold">(1949)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">65.</span>
<a href="/title/tt0105236/">Reservoir Dogs</a>
<span class="lister-item-year text-muted unbold">(1992)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">66.</span>
<a href="/title/tt0119488/">L.A. Confidential</a>
<span class="lister-item-year text-muted unbold">(1997)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">67.</span>
<a href="/title/tt0027977/">Modern Times</a>
<span class="lister-item-year text-muted unbold">(1936)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">68.</span>
<a href="/title/tt0071315/">Chinatown</a>
<span class="lister-item-year text-muted unbold">(1974)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">69.</span>
<a href="/title/tt0118799/">La vita è bella</a>
<span class="lister-item-year text-muted unbold">(1997)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">70.</span>
<a href="/title/tt0040897/">The Treasure of the Sierra Madre</a>
<span class="lister-item-year text-muted unbold">(1948)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">71.</span>
<a href="/title/tt0088763/">Back to the Future</a>
<span class="lister-item-year text-muted unbold">(1985)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">72.</span>
<a href="/title/tt0482571/">The Prestige</a>
<span class="lister-item-year text-muted unbold">(2006)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">73.</span>
<a href="/title/tt0071853/">Monty Python and the Holy Grail</a>
<span class="lister-item-year text-muted unbold">(1975)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">74.</span>
<a href="/title/tt0081398/">Raging Bull</a>
<span class="lister-item-year text-muted unbold">(1980)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">75.</span>
<a href="/title/tt0457430/">Pan's Labyrinth</a>
<span class="lister-item-year text-muted unbold">(2006)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">76.</span>
<a href="/title/tt0095765/">Nuovo Cinema Paradiso</a>
<span class="lister-item-year text-muted unbold">(1988)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">77.</span>
<a href="/title/tt0045152/">Singin' in the Rain</a>
<span class="lister-item-year text-muted unbold">(1952)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">78.</span>
<a href="/title/tt0053291/">Some Like It Hot</a>
<span class="lister-item-year text-muted unbold">(1959)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">79.</span>
<a href="/title/tt0050212/">The Bridge on the River Kwai</a>
<span class="lister-item-year text-muted unbold">(1957)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">80.</span>
<a href="/title/tt0042876/">Rashômon</a>
<span class="lister-item-year text-muted unbold">(1950)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">81.</span>
<a href="/title/tt0087843/">Once Upon a Time in America</a>
<span class="lister-item-year text-muted unbold">(1984)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">82.</span>
<a href="/title/tt0120689/">The Green Mile</a>
<span class="lister-item-year text-muted unbold">(1999)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">83.</span>
<a href="/title/tt0086879/">Amadeus</a>
<span class="lister-item-year text-muted unbold">(1984)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">84.</span>
<a href="/title/tt0042192/">All About Eve</a>
<span class="lister-item-year text-muted unbold">(1950)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">85.</span>
<a href="/title/tt0093058/">Full Metal Jacket</a>
<span class="lister-item-year text-muted unbold">(1987)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">86.</span>
<a href="/title/tt0040522/">Ladri di biciclette</a>
<span class="lister-item-year text-muted unbold">(1948)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">87.</span>
<a href="/title/tt0032553/">The Great Dictator</a>
<span class="lister-item-year text-muted unbold">(1940)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">88.</span>
<a href="/title/tt0062622/">2001: A Space Odyssey</a>
<span class="lister-item-year text-muted unbold">(1968)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">89.</span>
<a href="/title/tt0112573/">Braveheart</a>
<span class="lister-item-year text-muted unbold">(1995)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">90.</span>
<a href="/title/tt0361748/">Inglourious Basterds</a>
<span class="lister-item-year text-muted unbold">(2009)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">91.</span>
<a href="/title/tt0053604/">The Apartment</a>
<span class="lister-item-year text-muted unbold">(1960)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">92.</span>
<a href="/title/tt0363163/">Der Untergang</a>
<span class="lister-item-year text-muted unbold">(2004)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">93.</span>
<a href="/title/tt1049413/">Up</a>
<span class="lister-item-year text-muted unbold">(2009)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">94.</span>
<a href="/title/tt1504320/">The King's Speech</a>
<span class="lister-item-year text-muted unbold">(2010)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">95.</span>
<a href="/title/tt0017136/">Metropolis</a>
<span class="lister-item-year text-muted unbold">(1927)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">96.</span>
<a href="/title/tt0172495/">Gladiator</a>
<span class="lister-item-year text-muted unbold">(2000)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">97.</span>
<a href="/title/tt1205489/">Gran Torino</a>
<span class="lister-item-year text-muted unbold">(2008)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">98.</span>
<a href="/title/tt0070735/">The Sting</a>
<span class="lister-item-year text-muted unbold">(1973)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">99.</span>
<a href="/title/tt0105695/">Unforgiven</a>
<span class="lister-item-year text-muted unbold">(1992)</span>
</h3>, <h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">100.</span>
<a href="/title/tt0364569/">Oldeuboi</a>
<span class="lister-item-year text-muted unbold">(2003)</span>
</h3>]
>>> for i in p:
	print(p.text)

	
Traceback (most recent call last):
  File "<pyshell#9>", line 2, in <module>
    print(p.text)
AttributeError: 'list' object has no attribute 'text'
>>> pd.Series(p)
0     [\n, [1.], \n, [The Shawshank Redemption], \n,...
1     [\n, [2.], \n, [The Godfather], \n, [(1972)], \n]
2     [\n, [3.], \n, [The Godfather: Part II], \n, [...
3     [\n, [4.], \n, [Il buono, il brutto, il cattiv...
4      [\n, [5.], \n, [Pulp Fiction], \n, [(1994)], \n]
                            ...                        
95       [\n, [96.], \n, [Gladiator], \n, [(2000)], \n]
96     [\n, [97.], \n, [Gran Torino], \n, [(2008)], \n]
97       [\n, [98.], \n, [The Sting], \n, [(1973)], \n]
98      [\n, [99.], \n, [Unforgiven], \n, [(1992)], \n]
99       [\n, [100.], \n, [Oldeuboi], \n, [(2003)], \n]
Length: 100, dtype: object
>>> for i in p:
	print(i.text)

	

1.
The Shawshank Redemption
(1994)


2.
The Godfather
(1972)


3.
The Godfather: Part II
(1974)


4.
Il buono, il brutto, il cattivo
(1966)


5.
Pulp Fiction
(1994)


6.
Schindler's List
(1993)


7.
12 Angry Men
(1957)


8.
Inception
(2010)


9.
One Flew Over the Cuckoo's Nest
(1975)


10.
The Dark Knight
(2008)


11.
Star Wars: Episode V - The Empire Strikes Back
(1980)


12.
The Lord of the Rings: The Return of the King
(2003)


13.
Shichinin no samurai
(1954)


14.
Fight Club
(1999)


15.
Goodfellas
(1990)


16.
Star Wars
(1977)


17.
Casablanca
(1942)


18.
Cidade de Deus
(2002)


19.
The Lord of the Rings: The Fellowship of the Ring
(2001)


20.
Once Upon a Time in the West
(1968)


21.
Rear Window
(1954)


22.
Raiders of the Lost Ark
(1981)


23.
Psycho
(1960)


24.
The Usual Suspects
(1995)


25.
The Silence of the Lambs
(1991)


26.
Se7en
(1995)


27.
It's a Wonderful Life
(1946)


28.
Memento
(2000)


29.
Toy Story 3
(2010)


30.
The Lord of the Rings: The Two Towers
(2002)


31.
Sunset Blvd.
(1950)


32.
Forrest Gump
(1994)


33.
Léon
(1994)


34.
Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb
(1964)


35.
Apocalypse Now
(1979)


36.
Citizen Kane
(1941)


37.
North by Northwest
(1959)


38.
American Beauty
(1999)


39.
American History X
(1998)


40.
Taxi Driver
(1976)


41.
Terminator 2: Judgment Day
(1991)


42.
Saving Private Ryan
(1998)


43.
Vertigo
(1958)


44.
Alien
(1979)


45.
Amélie
(2001)


46.
WALL·E
(2008)


47.
Sen to Chihiro no kamikakushi
(2001)


48.
The Shining
(1980)


49.
Paths of Glory
(1957)


50.
Lawrence of Arabia
(1962)


51.
The Pianist
(2002)


52.
Double Indemnity
(1944)


53.
A Clockwork Orange
(1971)


54.
City Lights
(1931)


55.
The Lives of Others
(2006)


56.
M - Eine Stadt sucht einen Mörder
(1931)


57.
The Departed
(2006)


58.
To Kill a Mockingbird
(1962)


59.
Aliens
(1986)


60.
Black Swan
(2010)


61.
Eternal Sunshine of the Spotless Mind
(2004)


62.
Requiem for a Dream
(2000)


63.
Das Boot
(1981)


64.
The Third Man
(1949)


65.
Reservoir Dogs
(1992)


66.
L.A. Confidential
(1997)


67.
Modern Times
(1936)


68.
Chinatown
(1974)


69.
La vita è bella
(1997)


70.
The Treasure of the Sierra Madre
(1948)


71.
Back to the Future
(1985)


72.
The Prestige
(2006)


73.
Monty Python and the Holy Grail
(1975)


74.
Raging Bull
(1980)


75.
Pan's Labyrinth
(2006)


76.
Nuovo Cinema Paradiso
(1988)


77.
Singin' in the Rain
(1952)


78.
Some Like It Hot
(1959)


79.
The Bridge on the River Kwai
(1957)


80.
Rashômon
(1950)


81.
Once Upon a Time in America
(1984)


82.
The Green Mile
(1999)


83.
Amadeus
(1984)


84.
All About Eve
(1950)


85.
Full Metal Jacket
(1987)


86.
Ladri di biciclette
(1948)


87.
The Great Dictator
(1940)


88.
2001: A Space Odyssey
(1968)


89.
Braveheart
(1995)


90.
Inglourious Basterds
(2009)


91.
The Apartment
(1960)


92.
Der Untergang
(2004)


93.
Up
(2009)


94.
The King's Speech
(2010)


95.
Metropolis
(1927)


96.
Gladiator
(2000)


97.
Gran Torino
(2008)


98.
The Sting
(1973)


99.
Unforgiven
(1992)


100.
Oldeuboi
(2003)

>>> 
