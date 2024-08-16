-- Absolute Value:
-- What's the absolute difference in price between the 'Chicken Burrito' and the 'Veggie Bowl'?
SELECT ABS(7.5 - 7.8);

-- Power:
-- If you were to raise the price of the 'Steak Tacos' to the power of 2, what value would you get?
SELECT POWER (8, 2);

-- Square Root:
-- What's the square root of the calories for the 'Chips & Guacamole'?
SELECT SQRT(770) 
FROM ChipotleMenu; 

-- Ceiling:
-- What's the ceiling value of the price for 'Barbacoa Salad'?
SELECT CEILING(9);

-- Floor:
-- What's the floor value of the calories of 'Carnitas Quesadilla'?
SELECT FLOOR(750);

-- Round:
-- Round the price of the 'Sofritas Burrito Bowl' to the nearest whole number.
SELECT ROUND(7.9);


-- Round to Decimals:
-- Round the price of 'Chicken Burrito' to 2 decimal places.
SELECT ROUND(7.5,2);

-- Modulo:
-- If you divide the calories of 'Chicken Burrito' by the calories of 'Veggie Bowl', what's the remainder?
SELECT MOD (7.5,7.8);