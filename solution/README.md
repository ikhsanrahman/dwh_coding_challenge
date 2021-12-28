# Dkatalis test

## Author : Ikhsan Rahman Husien

## Tasks

To do the following tasks, you probably gonna need some kinds data processing library in your own choice of programming language.
`pandas`, a data processing library in Python, is recommended due to ease of use and simplicity. However, you are free to choose
any programming language and any framework to implement the solution.

1. Visualize the complete historical table view of each tables in tabular format in stdout (hint: print your table)

   **SOLUTION** :

   	- Read each file json. collect the data into a list
   	- Each list of data will be converted into dataframe
   	- Print each of dataframe

2. Visualize the complete historical table view of the denormalized joined table in stdout by joining these three tables (hint: the join key lies in the `resources` section, please read carefully)

   **SOLUTION** :

    - NaN value in dataframe fill using fillna() function with parameter method='ffill'.
    - Merge these three tables. firstly, merge accounts and cards. secondly, merge accounts and saving_accounts. then, merge the first and second one.
    - Print result

3. From result from point no 2, discuss how many transactions has been made, when did each of them occur, and how much the value of each transaction?  
   Transaction is defined as activity which change the balance of the savings account or credit used of the card

   ​	**SOLUTION** :

    - can be seen in column `datetime` that there are 7 transactions between 2 January 2020 to 20 January 2020.
