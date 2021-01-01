Solution to [OLAP Operations - 2](https://www.hackerrank.com/challenges/olap-operations-2)

An OLAP cube is a multi-dimensional array of data. Cube indicates a multi-dimensional dataset. This is useful if a company wanted to summarize financial data by product, time-period, and city. This lends to different operations for analysis, including: slice and dice, rollup, and pivot.

- **Slice** accesses a subset of the cube by choosing a single value for its dimensions.
- **Dice** accesses a subset of the cube by selecting multiple dimensions.
- **Drill** navigates among levels of hierarchical data, e.g., grouped products
- **Roll-up** uses aggregate functions to summarize along dimensions
- **Pivot** rotates the cube in space to examine different dimensions

**Answer**:

Pivot

From [wiki](https://en.wikipedia.org/wiki/OLAP_cube#Operations)
> Pivot allows an analyst to rotate the cube in space to see its various faces. For example, cities could be arranged vertically and products horizontally while viewing data for a particular quarter. Pivoting could replace products with time periods to see data across time for a single product.
