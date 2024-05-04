#!/usr/bin/env ruby

# Extract the first argument passed in the command line
phone_number = ARGV[0]

# Regular expression to match a 10-digit phone number
pattern = /^\d{10}$/

# Check if the phone number matches the pattern
if phone_number.match?(pattern)
  puts phone_number
end
