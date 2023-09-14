-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Check description of crime scene reports
SELECT description
FROM crime_scene_reports
WHERE street = "Humphrey Street" AND day = 28 AND month = 7 AND year = 2021;

-- Check interviews with three witnesses
SELECT name,transcript
FROM interviews
WHERE year = 2021 AND day = 28 AND month = 7;

-- Check bakery security logs
SELECT name,bakery_security_logs.activity
FROM people
JOIN bakery_security_logs
ON people.license_plate = bakery_security_logs.license_plate
WHERE year = 2021 AND day = 28 AND month = 7
AND hour = 10 AND minute BETWEEN 15 AND 25;

-- Check phone calls
SELECT name,phone_calls.duration
FROM people
JOIN phone_calls
ON people.phone_number = phone_calls.caller
WHERE year = 2021 AND day = 28 AND month = 7 AND duration < 60;

-- Check name of receiver (accomplice)
SELECT name,phone_calls.duration
FROM people
JOIN phone_calls
ON people.phone_number = phone_calls.receiver
WHERE year = 2021 AND day = 28 AND month = 7 AND duration < 60;

-- Check ATM transactions
SELECT name
FROM people
JOIN bank_accounts
ON people.id = bank_accounts.person_id
JOIN atm_transactions
ON bank_accounts.account_number = atm_transactions.account_number
WHERE year = 2021 AND month = 7
AND day = 28 AND atm_location = "Leggett Street"
AND transaction_type = "withdraw";


-- Check what flight id is the earliest in Fiftyville's Airport
SELECT full_name,city,flights.id,flights.hour,flights.minute
FROM airports
JOIN flights
ON airports.id = flights.origin_airport_id
WHERE year = 2021 AND month = 7
AND day = 29 AND airports.city = "Fiftyville"
ORDER BY hour
LIMIT 1;

-- Check airport of destination
SELECT full_name,city,flights.id,flights.hour,flights.minute
FROM airports
JOIN flights
ON airports.id = flights.destination_airport_id
WHERE year = 2021 AND month = 7
AND day = 29 AND flights.id = 36;

-- Check passengers
SELECT name,passengers.seat,flights.id
FROM people
JOIN passengers
ON people.passport_number = passengers.passport_number
JOIN flights
ON flights.id = passengers.flight_id
WHERE passengers.flight_id = 36;

-- Final suspects: Bruce (accomplice Robin) and Diana (accomplice Philip).
-- They both appeared in the phone calls, bakery parking lot and ATM transaction queries
-- But only Bruce appeared in the flights query