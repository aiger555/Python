import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config


from_email = config('from_email',default='')
password = config('password',default='')


msg = MIMEMultipart()

to_email = 'nuralieva.aik@gmail.com'
message = 'Hi, it is a message with smtp!'

msg.attach(MIMEText(message, 'Homework'))

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(from_email, password)
server.sendmail(from_email, to_email, msg.as_string())
server.quit()

"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

class Solution:
    def  maxProfit(self, prices):
        n = len(prices)
        max_sum = 0
        for i in range(n-1):
            for j in range(i+1, n):
                max_sum =  max(prices[j] - prices[i], max_sum)
        return max_sum 

"""