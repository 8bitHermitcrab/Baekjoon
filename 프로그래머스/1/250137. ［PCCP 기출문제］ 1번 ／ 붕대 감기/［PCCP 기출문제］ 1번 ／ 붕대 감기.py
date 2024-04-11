def solution(bandage, health, attacks):
    max_hp = health
    max_time = attacks[-1][0]
    attack_dict = {}
    for i in attacks:
        attack_dict[i[0]] = i[1]
    
    t = 0
    sec = 0
    while t <= max_time:
        if t in attack_dict:
            health -= attack_dict[t]
            sec = 0
            
            if health <= 0:
                return -1
        else:
            sec += 1
            if sec < bandage[0]:
                health += bandage[1]
                if health > max_hp:
                    health = max_hp
            else:
                health = health + bandage[1] + bandage[2]
                if health > max_hp:
                    health = max_hp
                sec = 0
        t += 1
    return health