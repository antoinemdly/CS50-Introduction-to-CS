-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT * FROM crime_scene_reports WHERE street = "Humphrey Street";
--Report of the duck : at 10:15am at Humphrey Street Bakery

SELECT * FROM interviews WHERE day = "28" AND month = "7" AND transcript LIKE "%bakery%";
--within ten minutes of the theft, left with a car
--Thief withdraw morning earlier in the morning on Leggett Street
--while leaving, called accomplice, planned to take the earliest flight tomorrow
--asked to purschase the flight ticket

SELECT license_plate FROM bakery_security_logs WHERE month = "7" AND day = "28" AND hour = "10" AND minute > "05" AND minute < "25" AND activity = "exit";
--All potential thief license_plate

SELECT amount, account_number FROM atm_transactions WHERE month = "7" AND day = "28" AND atm_location = "Leggett Street" AND transaction_type = "withdraw";
--All potential thief account_number and withdraw amount

SELECT name FROM people WHERE id IN
(SELECT person_id FROM bank_accounts WHERE account_number IN
(SELECT account_number FROM atm_transactions WHERE month = "7" AND day = "28" AND atm_location = "Leggett Street" AND transaction_type = "withdraw"
))

SELECT name FROM people WHERE license_plate IN
(SELECT license_plate FROM bakery_security_logs WHERE month = "7" AND day = "28" AND hour = "10" AND minute > "05" AND minute < "25" AND activity = "exit"
)
--By comparing these two, we know that the thiefs name is either Iman,Luca,Diana,Bruce

SELECT name FROM people WHERE phone_number IN(
SELECT caller,duration FROM phone_calls WHERE month = "7" AND day = "28" AND caller IN (SELECT phone_number FROM people WHERE name = "Iman" OR name = "Luca" OR name = "Diana" OR name = "Bruce")
)
--name of the thief is either Diana or Bruce

SELECT name FROM people WHERE phone_number IN(
SELECT receiver FROM phone_calls WHERE month = "7" AND day = "28" AND duration < 60 AND caller IN (SELECT phone_number FROM people WHERE name = "Diana" OR name = "Bruce")
)
--name of the potential accomplice

SELECT full_name FROM airports WHERE id IN(SELECT DISTINCT(origin_airport_id) FROM flights);
--airports name

SELECT * FROM flights WHERE month = "7" AND day = "29";
--earliest flight is at 8:20 from Fiftyville Regioal Airport and the id is 36

SELECT name FROM people WHERE passport_number IN(SELECT passport_number FROM passengers WHERE flight_id = "36");
--Bruce is on the flight so it is the thief

SELECT name FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE day = "28" AND duration < 60 AND caller IN (SELECT phone_number FROM people WHERE name = "Bruce"));
--The accomplice is Robin

SELECT city FROM airports WHERE id = "4";
--The city where he escaped is New York City