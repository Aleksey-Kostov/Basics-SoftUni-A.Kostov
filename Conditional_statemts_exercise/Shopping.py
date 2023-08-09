budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
am_memory_count = int(input())

PRICE_VIDEO_CARD = 250

price_processor = (PRICE_VIDEO_CARD * video_cards_count) * 0.35
price_ram_memory = (PRICE_VIDEO_CARD * video_cards_count) * 0.1

total_price = (video_cards_count * PRICE_VIDEO_CARD) + \
              (processors_count * price_processor) + \
              (am_memory_count * price_ram_memory)

if video_cards_count > processors_count:
    total_price *= 0.85

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
