-- 1 Top 5 Funds by AUM
SELECT *
FROM aum_by_fund_house
ORDER BY aum DESC
LIMIT 5;

-- 2 Average NAV
SELECT AVG(nav)
FROM nav_history;

-- 3 Monthly SIP Trend
SELECT *
FROM monthly_sip_inflows
ORDER BY month;

-- 4 Category-wise Inflows
SELECT category,
SUM(net_inflow)
FROM category_inflows
GROUP BY category;

-- 5 Expense Ratio < 1
SELECT scheme_name,
expense_ratio
FROM scheme_performance
WHERE expense_ratio < 1;

-- 6 Top Performing Funds
SELECT scheme_name,
return_1y
FROM scheme_performance
ORDER BY return_1y DESC
LIMIT 10;

-- 7 Lowest Expense Funds
SELECT scheme_name,
expense_ratio
FROM scheme_performance
ORDER BY expense_ratio;

-- 8 Transaction Type Distribution
SELECT transaction_type,
COUNT(*)
FROM investor_transactions
GROUP BY transaction_type;

-- 9 Portfolio Sector Allocation
SELECT sector,
COUNT(*)
FROM portfolio_holdings
GROUP BY sector;

-- 10 NAV History Count
SELECT COUNT(*)
FROM nav_history;