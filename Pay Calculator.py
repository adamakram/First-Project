Hours_Worked_Per_Week = int(input('Please enter the amount of hours you work in a week...'))

print('So, you work, per week')
print(Hours_Worked_Per_Week)

Hourly_Pay_Rate = float(input('What is your hourly pay rate in euros?'))

print('So, your pay rate is')
print(Hourly_Pay_Rate)

Tax_Rate = float(input('What is your tax-rate?'))

print('So, your tax rate is')
print(Tax_Rate)


Gross_Pay_In_Euros = ((Hours_Worked_Per_Week)*(Hourly_Pay_Rate))


print ('Your Gross Pay in Euros is...')
print(Gross_Pay_In_Euros)

Gross_Pay_In_Sterling = Gross_Pay_In_Euros / 1.1243
Gross_Pay_In_Sterling = float(round(Gross_Pay_In_Sterling,2))

print ('Your Gross Pay in Sterling is...')
print(Gross_Pay_In_Sterling)

Net_Pay_In_Sterling= Gross_Pay_In_Sterling * (1-Tax_Rate)
Net_Pay_In_Sterling= float(round(Net_Pay_In_Sterling,2))

print('Finally Meaning that your Net Pay In Sterling is...')
print(Net_Pay_In_Sterling)
