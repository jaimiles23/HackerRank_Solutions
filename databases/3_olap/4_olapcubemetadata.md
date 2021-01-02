Solution to [OLAP Cube Metadata](https://www.hackerrank.com/challenges/olap-cube-metadata/problem)

[OLAP](https://en.wikipedia.org/wiki/Online_analytical_processing)
> An OLAP cube consists of numeric facts called measures that are categorized by dimensions. The cube metadata is typically created from a star schema or snowflake schema or fact constellation of tables in a relational database.

- **star schema** simplest data mart schema used in data warehousing. A fact table (quantitative measures) is surrounded by dimension tables (discrete, text values). This design helps with querying.
- **snowflake schema** is a logical arrangement of tables in multidimensional data where the ERD resembles a snowflake shape. It is similarly composed of a fact sheet and linked dimensional tables.

**Answer**

Both star and snowflake schema(s)