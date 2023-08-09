processor_price = float(input())
graphic_card_price = float(input())
price_ram = float(input())
numbers_of_ram = int(input())
percent_discount = float(input())

USD_BGN = 1.57

bgn_processor_price = processor_price * USD_BGN
total_processor_price = bgn_processor_price - (bgn_processor_price * percent_discount)
bgn_graphic_card_price = graphic_card_price * USD_BGN
total_graphic_card_price = bgn_graphic_card_price - (bgn_graphic_card_price * percent_discount)
bgn_price_ram = price_ram * USD_BGN
total_price_ram = bgn_price_ram * numbers_of_ram


total_price = total_price_ram + total_graphic_card_price + total_processor_price


print(f"Money needed - {total_price:.2f} leva.")
