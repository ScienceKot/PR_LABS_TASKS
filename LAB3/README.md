### Task 3: Web Crawling/Parsing.

Your task during the laboratory work is to create a function that will perform the following actions:
* Extract all urls from a product listing page of 999.md like this one:
  https://999.md/ru/list/real-estate/apartments-and-rooms?o_30_241=894&applied=1&eo=12900&eo=12912&eo=12885&eo=13859&ef=32&ef=33&o_33_1=776
  
* After extracting all links from the page it should filter out the boosters.
* All extracted urls should be absolute urls.
* After extracting all urls, the function should check if there are more pages to extract urls from. Here we have 2 cases:
    * Case 1: If there are more pages, the function should call itself recursively for the new pagination url and pass the parsed url to the function as an argument.
    * Case 2: If there is no more pages to parse then return the list of parsed urls.
  
* Not obligatory: To not wait for the parser to parse all pagination pages you can an additional int argument - ``max_page_num`` - it will limit the number of paged parsed by the function.

## Homework.
For the homework task you should create a function that takes as an argument one of urls parsed by the function above and extract the product details (for example for an apartament it would be the number of rooms, area, location etc.)

## How to submit the lab task.
Please send me a repository containing the following:
1. A script with the in class function (the one extracting the url) named ``in_class.py``
2. A script with the homework function (the one extracting the product details) named ``homework.py``
3. A .json or .txt file containing the list of urls parsed by the first function.

Plese send the url to the homework to this email: *papaluta.vasile@isa.utm.md*