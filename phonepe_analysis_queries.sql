-- phonepe_analysis_queries.sql

-- Database: phonepe_pulse_db

-- --- Case Study 1: Decoding Transaction Dynamics on PhonePe ---
-- Scenario: Understand variations in transaction behavior across states, quarters, and payment categories.

-- Query 1.1: Total transaction count and amount per payment instrument across all years and quarters
SELECT
    transaction_type,
    SUM(transaction_count) AS total_transactions,
    SUM(transaction_amount) AS total_transaction_amount
FROM Aggregated_transaction
GROUP BY transaction_type
ORDER BY total_transaction_amount DESC;

-- Query 1.2: Quarterly transaction trend for a specific state (e.g., 'maharashtra') and payment instrument (e.g., 'Recharge & bill payments')
SELECT
    year,
    quarter,
    SUM(transaction_count) AS quarterly_transactions,
    SUM(transaction_amount) AS quarterly_amount
FROM Aggregated_transaction
WHERE state = 'maharashtra' AND transaction_type = 'Recharge & bill payments'
GROUP BY year, quarter
ORDER BY year, quarter;

-- Query 1.3: Top 5 states by total transaction amount for a specific year (e.g., 2022)
SELECT
    state,
    SUM(transaction_amount) AS total_transaction_amount
FROM Map_transaction
WHERE year = 2022
GROUP BY state
ORDER BY total_transaction_amount DESC
LIMIT 5;


-- --- Case Study 2: Device Dominance and User Engagement Analysis ---
-- Scenario: Understand user preferences across different device brands, user engagement (registered users, app opens) segmented by devices, regions, and time periods.

-- Query 2.1: Number of registered users and app opens by device brand across all years and quarters
SELECT
    brand_name,
    SUM(registered_users) AS total_registered_users,
    SUM(app_opens) AS total_app_opens
FROM users_by_device, Aggregated_user
GROUP BY brand_name
ORDER BY total_registered_users DESC;

-- Query 2.2: User engagement (registered users) for a specific state (e.g., 'karnataka') by device brand in a given year (e.g., 2021)
SELECT
    ud.brand_name,
    SUM(ud.count) AS total_users_by_brand
FROM users_by_device AS ud
WHERE ud.state = 'karnataka' AND ud.year = 2021
GROUP BY ud.brand_name
ORDER BY total_users_by_brand DESC;



-- --- Case Study 3: Insurance Penetration and Growth Potential Analysis ---
-- Scenario: Analyze the growth trajectory of the insurance domain and identify untapped opportunities at the state level.

-- Query 3.1: Total insurance premium count and amount over time (by year and quarter)
SELECT
    year,
    quarter,
    SUM(total_count) AS total_premium_count,
    SUM(total_amount) AS total_premium_amount
FROM
    (-- Data from districts_data table
        SELECT
            year,
            quarter,
            count AS total_count,
            amount AS total_amount
        FROM top_insurance_districts_data

        UNION ALL

        -- Data from pincodes_data table
        SELECT
            year,
            quarter,
            count AS total_count,
            amount AS total_amount
        FROM top_insurance_pincodes_data
    ) AS combined_data
GROUP BY year, quarter
ORDER BY year ASC, quarter ASC;


-- Query 3.2: Top 5 states with the highest total insurance premium amount for the latest year/quarter
SELECT
    state,
    SUM(total_amount) AS total_premium_amount
FROM
    (-- Get data from districts_data table for the latest year and quarter
        SELECT
            state,
            amount AS total_amount
        FROM top_insurance_districts_data
        WHERE (year, quarter) = (SELECT MAX(year), MAX(quarter) FROM top_insurance_districts_data WHERE year = (SELECT MAX(year) FROM top_insurance_districts_data))

        UNION ALL

        -- Get data from pincodes_data table for the latest year and quarter
        SELECT
            state,
            amount AS total_amount
        FROM top_insurance_pincodes_data
        WHERE (year, quarter) = (SELECT MAX(year), MAX(quarter) FROM top_insurance_pincodes_data WHERE year = (SELECT MAX(year) FROM top_insurance_pincodes_data))
    ) AS combined_latest_data
GROUP BY state
ORDER BY total_premium_amount DESC
LIMIT 5;


-- --- Case Study 4: Transaction Analysis for Market Expansion ---
-- Scenario: Identify trends, opportunities, and potential areas for expansion by understanding transaction dynamics at the state level.

-- Query 4.1: States with the highest growth in transaction amount year-over-year (Example for 2021 vs 2022)
SELECT
    t1.state,
    SUM(t1.transaction_amount) AS total_amount_2021,
    SUM(t2.transaction_amount) AS total_amount_2022,
    (SUM(t2.transaction_amount) - SUM(t1.transaction_amount)) AS amount_growth
FROM Map_transaction t1
JOIN Map_transaction t2 ON t1.state = t2.state AND t1.quarter = t2.quarter
WHERE t1.year = 2021 AND t2.year = 2022
GROUP BY t1.state
ORDER BY amount_growth DESC
LIMIT 10;

-- Query 4.2: Total transaction volume and value per state for the latest year and quarter
SELECT
    state,
    SUM(transaction_count) AS total_transaction_volume,
    SUM(transaction_amount) AS total_transaction_value
FROM Map_transaction
WHERE year = (SELECT MAX(year) FROM Map_transaction)
  AND quarter = (SELECT MAX(quarter) FROM Map_transaction WHERE year = (SELECT MAX(year) FROM Map_transaction))
GROUP BY state
ORDER BY total_transaction_value DESC;


-- --- Case Study 5: User Engagement and Growth Strategy ---
-- Scenario: Enhance market position by analyzing user engagement (registered users, app opens) across different states and districts.

-- Query 5.1: Top 10 districts by total registered users for the latest year and quarter
SELECT
    district_name,
    SUM(registered_users) AS total_registered_users
FROM top_user_districts_data
WHERE
    (year, quarter) = (
        SELECT
            year,
            quarter
        FROM top_user_districts_data
        ORDER BY year DESC, quarter DESC
        LIMIT 1
    )
GROUP BY district_name
ORDER BY total_registered_users DESC
LIMIT 10;

-- Query 5.2: State-wise average app opens per registered user (simple ratio)
SELECT
    state,
    SUM(registered_users) AS total_registered_users,
    SUM(app_opens) AS total_app_opens,
    SUM(app_opens) / NULLIF(SUM(registered_users), 0) AS avg_app_opens_per_user
FROM Aggregated_user
GROUP BY state
ORDER BY avg_app_opens_per_user DESC;


-- --- Case Study 6: Insurance Engagement Analysis ---
-- Scenario: Understand the uptake of insurance services among users across states and districts.

-- Query 6.1: Insurance transaction volume (premium_count) per district for a specific year and quarter (e.g., 2022 Q3)
SELECT
    district,
    SUM(premium_count) AS total_premium_count
FROM Map_insurance
WHERE year = 2022 AND quarter = 3
GROUP BY district
ORDER BY total_premium_count DESC;

-- Query 6.2: States showing significant growth in insurance premium amount between two years (Example for 2021 vs 2022)
SELECT
    y1.state,
    y1.total_premium_2021,
    y2.total_premium_2022,
    (y2.total_premium_2022 - y1.total_premium_2021) AS growth_amount,
    CASE
        WHEN y1.total_premium_2021 > 0 THEN
            ((y2.total_premium_2022 - y1.total_premium_2021) / y1.total_premium_2021) * 100
        ELSE 0 -- Handle cases where initial premium is zero or null to avoid division by zero
    END AS percentage_growth
FROM
    (
        -- Total premium amount for each state in Year 1 (2021)
        SELECT
            state,
            SUM(amount) AS total_premium_2021
        FROM
            (
                SELECT state, amount FROM top_insurance_districts_data WHERE year = 2021
                UNION ALL
                SELECT state, amount FROM top_insurance_pincodes_data WHERE year = 2021
            ) AS combined_data_2021
        GROUP BY state
    ) AS y1
JOIN
    (
        -- Total premium amount for each state in Year 2 (2022)
        SELECT
            state,
            SUM(amount) AS total_premium_2022
        FROM
            (
                SELECT state, amount FROM top_insurance_districts_data WHERE year = 2022
                UNION ALL
                SELECT state, amount FROM top_insurance_pincodes_data WHERE year = 2022
            ) AS combined_data_2022
        GROUP BY state
    ) AS y2 ON y1.state = y2.state
WHERE
    (y2.total_premium_2022 - y1.total_premium_2021) > 0 -- Filter for positive growth
ORDER BY
    percentage_growth DESC; -- Order by percentage growth to see "significant" growth


-- --- Case Study 7: Transaction Analysis Across States and Districts ---
-- Scenario: Identify top-performing states, districts, and pin codes in terms of transaction volume and value.

-- Query 7.1: Top 10 states by total transaction value for the most recent data
SELECT
    state,
    SUM(total_amount) AS total_transaction_value
FROM
    (
        -- Get data from districts_data table for the latest year and quarter
        SELECT
            state,
            amount AS total_amount
        FROM top_transaction_districts_data
        WHERE (year, quarter) = (SELECT MAX(year), MAX(quarter) FROM top_transaction_districts_data WHERE year = (SELECT MAX(year) FROM top_transaction_districts_data))

        UNION ALL

        -- Get data from pincodes_data table for the latest year and quarter
        SELECT
            state,
            amount AS total_amount
        FROM top_transaction_pincodes_data
        WHERE (year, quarter) = (SELECT MAX(year), MAX(quarter) FROM top_transaction_pincodes_data WHERE year = (SELECT MAX(year) FROM top_transaction_pincodes_data))
    ) AS combined_latest_data
GROUP BY state
ORDER BY total_transaction_value DESC
LIMIT 10;

-- Query 7.2: Top 5 districts by total transaction count in 'Maharashtra' state for 2022 Q4
SELECT
    district_name,
    SUM(count) AS total_transaction_count
FROM top_insurance_districts_data
WHERE state = 'maharashtra' AND year = 2022 AND quarter = 4
GROUP BY district_name
ORDER BY total_transaction_count DESC
LIMIT 5;


-- --- Case Study 8: User Registration Analysis ---
-- Scenario: Identify top states, districts, and pin codes from which the most users registered during a specific year-quarter combination.

-- Query 8.1: Top 10 pincodes by registered users for the latest available quarter

SELECT
    pincode,
    SUM(registered_users) AS total_registered_users
FROM top_user_pincodes_data
WHERE
    (year, quarter) = (
        SELECT
            year,
            quarter
        FROM top_user_pincodes_data
        ORDER BY year DESC, quarter DESC
        LIMIT 1
    )
GROUP BY pincode
ORDER BY total_registered_users DESC
LIMIT 10;

-- Query 8.2: States with the highest total registered users over all time
SELECT
    state,
    SUM(registered_users) AS total_registered_users
FROM
    (
        -- Registered users from districts data
        SELECT
            state,
            registered_users
        FROM top_user_districts_data

        UNION ALL

        -- Registered users from pincodes data
        SELECT
            state,
            registered_users
        FROM top_user_pincodes_data
    ) AS combined_user_data
GROUP BY state
ORDER BY total_registered_users DESC
LIMIT 10;


-- --- Case Study 9: Insurance Transactions Analysis ---
-- Scenario: Identify top states, districts, and pin codes where the most insurance transactions occurred during a specific year-quarter combination.

-- Query 9.1: Top 5 districts by insurance premium count for 2021 Q2
SELECT
    district_name,
    SUM(count) AS premium_count
FROM top_insurance_districts_data
WHERE year = 2021 AND quarter = 2
GROUP BY district_name
ORDER BY premium_count DESC
LIMIT 5;

-- Query 9.2: Top 10 states by total insurance premium amount for the latest year and quarter
SELECT
    state,
    SUM(total_amount) AS total_insurance_premium_amount
FROM
    (
        -- Get data from top_insurance_districts_data table for its latest year and quarter
        SELECT
            state,
            amount AS total_amount
        FROM top_insurance_districts_data
        WHERE
            (year, quarter) = (
                SELECT
                    year,
                    quarter
                FROM top_insurance_districts_data
                ORDER BY year DESC, quarter DESC
                LIMIT 1
            )

        UNION ALL

        -- Get data from top_insurance_pincodes_data table for its latest year and quarter
        SELECT
            state,
            amount AS total_amount
        FROM top_insurance_pincodes_data
        WHERE
            (year, quarter) = (
                SELECT
                    year,
                    quarter
                FROM top_insurance_pincodes_data
                ORDER BY year DESC, quarter DESC
                LIMIT 1
            )
    ) AS combined_latest_insurance_data
GROUP BY state
ORDER BY total_insurance_premium_amount DESC
LIMIT 10;