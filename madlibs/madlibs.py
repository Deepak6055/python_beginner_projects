def madlib():
    
    time_of_day = input("Time of the day: ")
    body_part_plural = input("Body Part (plural) :")
    color = input("color: ")
    verb_past_tense = input("verb (past tense): ")
    food = input("food: ")
    noun1 = input("noun: ")
    noun_plural_1 = input("Noun (plural): ")
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")

    madlib = f"It was a {adj1} {time_of_day} in Gru's neighborhood when we realized that the serum created to turn minions into invincible warriors didn't work as planned. Instead, it turned them into {color} minions with an insatiable craving for {body_part_plural}. These little creatures {verb_past_tense} around the lab, causing chaos and munching on {food}.\
    They were {adj2} and {adj3}, with their big eyes fixed on any {body_part_plural} in sight. Gru and his team were astonished, as the minions were wreaking havoc, leaving a trail of {noun_plural_1} behind them.\
    Despite their mischief, Gru couldn't help but find them {adj1} and {adj2}, even in the midst of their misadventures. It seemed like they were destined to be troublemakers, yet Gru couldn't imagine life without their antics and love for {noun1}."

    print(madlib)

madlib()
