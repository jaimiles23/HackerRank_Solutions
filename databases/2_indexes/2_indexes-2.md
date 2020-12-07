Solution to [Indexes - 2](https://www.hackerrank.com/challenges/indexes-2)

Review the following definitions of clustered & non-clustered indices, found [here](https://logicalread.com/sql-server-understanding-indexes-w02/#.X866orOIaUk)
1. Clustered index
   1. Clustered indexes store and sort data based on the key column(s). There can only be one clustered index per table because data can be sorted in only one order. A clustered index is created by default when a table definition includes a primary key constraint.
2. Non-clustered Indexes
   1. Non-clustered indexes contain index key values and row locators that point to the actual data row. If there is no clustered index, the row locator is a pointer to the row. When there is a clustered index present, the row locator is the clustered index key for the row.
    
   Non-clustered indexes can be optimized to satisfy more queries, improve query response times, and reduce index size. The two most important of these optimized non-clustered indexes are described in the next two sections.


Thus, the clustered index is often the primary key for a table and the row locator.

**Answer**: If the table has a clustered index, or the index is on an indexed view, the row locator is the clustered index key for the row.