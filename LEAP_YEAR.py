def is_leap_year(year):
  """
  This function checks if a given year is a leap year.

  Args:
      year: An integer representing the year.

  Returns:
      True if the year is a leap year, False otherwise.
  """
  return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Enter a year: "))

if is_leap_year(year):
  print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")