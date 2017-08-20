#!/usr/bin/python

script = '''Over the past few years, the rise of cloud-based services \
has also resulted in the growth of a subscription economy.
In 2016, Zuora launched a Subscription Economy Index that looks at \
revenue growth of nearly 360 subscription businesses and compares \
that growth to sales for companies in the S&P 500 (SPY) and US retail sales.
Zuora is expected to go public this year. The company hasn't \
confirmed any plans, but in an interview last year, its CEO and co-founder, \
Tien Tzuo, acknowledged that "2017 would be a good time (for an IPO)".'''

f = file('script.txt', 'w') # file is a class in __builtin__ module
f.write(script)
f.close()

f = file('script.txt', 'r')
# if no mode is specified, 'r'ead mode is assumed by default
while True:
  line = f.readline()
  if len(line) == 0: # Zero length indicates EOF
    break
  print line,
  # Notice comma to avoid automatic newline added by Python

f.close()
