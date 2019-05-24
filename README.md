# python_kpi_2019
This is an individual work for Python course at Kyiv Polytechnic Institute

The basic premise is to explore various methods of finding the right "taxes" for a number 
of members that are needed to "fund" an enterprise that requires a particular amount of investment.

The methods include level, pillow (for member), proportional and N-core.

To be able to calculate the corresponding tax some information is needed: 
1. The income of each member.
2. Amount of "funding" that needed to be raised.
* It is important to mention, that the investment amount should not exceed the total of all incomes. 
Otherwise, the task has no sense.

The program consists of two parts.
generator.py is needed for generating an array of names (random strings) and incomes (random number up to 100000, but could be adjusted)
After the generation is finished, the results are written to the data.csv file.

TRP_final_updated reads the generated file and then writes results in the same file. 
A user gets a CSV table with all data regarding the taxes corresponding to each method.
