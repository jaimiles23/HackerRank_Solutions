Solution to [Index Architecture Types](https://www.hackerrank.com/challenges/indexes-1)


The below excerpts are taken from [About SQL Server](https://aboutsqlserver.com/2010/09/22/indexes-structure/)
1. **Clustered indexes**. 
   1. This is one index per table and basically specifies the order how data is stored in the table. For example, if the table has the clustered key index on the integer field, it means data will be actually sorted by that integer field. Please don’t be confused – there is still no such thing like default sorting order for the queries – the order of the rows SQL Server returns would depend on the execution plan which could be different than clustered index scan.
2. **non-clustered indexes**
   1. SQL Server allows to have up to 249 non-clustered indexes per table in SQL 2005 and 999 non-clustered indexes in SQL 2008 (thanks to Chirag for pointing this out). This is “just an index”.


**Answer**: 2