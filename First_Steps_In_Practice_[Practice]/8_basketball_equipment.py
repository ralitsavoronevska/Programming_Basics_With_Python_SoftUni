# Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

# Input:
# Годишната такса за тренировки по баскетбол – цяло число в интервала [0… 9999]

# Output:
# Да се отпечата на конзолата колко ще са разходите на Джеси, ако започне да спортува баскетбол.

yearly_subscription_for_basketball_training = int(input())

sneakers_price = yearly_subscription_for_basketball_training - (yearly_subscription_for_basketball_training * (40/100))
basketball_sportswear_price = sneakers_price - (sneakers_price * (20 / 100))
basketball_ball_price = basketball_sportswear_price * 1/4
basketball_accessories_price = basketball_ball_price * 1/5
total_basketball_equipment_price = (yearly_subscription_for_basketball_training + sneakers_price +
                                    basketball_sportswear_price + basketball_ball_price + basketball_accessories_price)

print(f"{total_basketball_equipment_price:.2f}")