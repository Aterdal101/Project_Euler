def number_to_words(n):
  words_less_than_20 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

  words_tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

  if n == 1000:
      return "onethousand"
  elif n < 100:
      return words_tens[n // 10] + words_less_than_20[n % 10]
  else:
      return words_less_than_20[n // 100] + ("hundred" if n % 100 == 0 else "hundredand" + number_to_words(n % 100))

def count_letters_in_numbers(start, end):
  return sum(len(number_to_words(number)) for number in range(start, end + 1))

result = count_letters_in_numbers(1, 1000)
print(result)
