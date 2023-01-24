This is my submission for the Crawler Coding Challenge. 
Below are the requirements:

The goal of this challenge is to implement a console application that displays the most common words used in a portion of a webpage.
Requirements
The code should be written in C#, Python.
The code should return the most common words used and the number of times they are used. The following should be configurable:
-	The number of words to return (default: 10)
-	Words to exclude from the search
Your code (only the source code, no binaries) should be returned as a zip posted within the contractor hub tool along with your resume. The code should build into an executable console application. 
Page to crawl
https://en.wikipedia.org/wiki/Microsoft
Only words from the section “history” should be accounted for.

There is an attached example table of the order of the # of occurences. I do not believe this example is to be taken literally as Wikipedia pages are subject to constant change.
This submission makes use of the Wikipedia Python API (https://github.com/martin-majlis/Wikipedia-API/). 
At first I approached this challenge intending to use the BeautifulSoup Python library. However, I then found out that there already exists an official Wikipedia API. 
I believe it makes more sense to use the direct API if available rather than manual screen-scraping.

This application takes in two form of arguments on the console. 
An integer will configure the number of words to return. Only one integer can be supplied as an argument.
Alphabetical strings will configure which words to exclude from the search.

A default run with no arguments will default the arguments to showing the top 10 most common words with no words excluded from the search

python wikicrawler.py
+-----------+------------------+
|    Word   | # of occurrences |
+-----------+------------------+
|    the    |       230        |
| Microsoft |       141        |
|     to    |       108        |
|     of    |       106        |
|     a     |        99        |
|    and    |        96        |
|     in    |        92        |
|    for    |        61        |
|  Windows  |        51        |
|    with   |        44        |
+-----------+------------------+ 

Running while passing in an integer argument will alter the number of words presented

python wikicrawler.py 5
+-----------+------------------+
|    Word   | # of occurrences |
+-----------+------------------+
|    the    |       230        |
| Microsoft |       141        |
|     to    |       108        |
|     of    |       106        |
|     a     |        99        |
+-----------+------------------+

Running while passing in string arguments will alter the words presented

python wikicrawler.py Microsoft the
+---------+------------------+
|   Word  | # of occurrences |
+---------+------------------+
|    to   |       108        |
|    of   |       106        |
|    a    |        99        |
|   and   |        96        |
|    in   |        92        |
|   for   |        61        |
| Windows |        51        |
|   with  |        44        |
|    on   |        37        |
|   was   |        34        |
+---------+------------------+

Both types of arguments can be run at once

python wikicrawler.py 5 Microsoft the
+------+------------------+
| Word | # of occurrences |
+------+------------------+
|  to  |       108        |
|  of  |       106        |
|  a   |        99        |
| and  |        96        |
|  in  |        92        |
+------+------------------+