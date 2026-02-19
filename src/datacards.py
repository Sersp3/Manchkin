card_database = {
    "doors": [
        # --- МОНСТРЫ (15 штук) ---
        # Легкие (1-5)
        {"type": "monster", "name": "Трава в горшке", "level": 1, "treasures": 1, "undead": False, "bad_stuff": "nothing", "text": "Эльфы тянут доп. сокровище."},
        {"type": "monster", "name": "Сопливый нос", "level": 2, "treasures": 1, "undead": False, "bad_stuff": "lose_lvl_1", "text": "Мерзкий тип."},
        {"type": "monster", "name": "Желеобразный октаэдр", "level": 2, "treasures": 1, "undead": False, "bad_stuff": "lose_footgear", "text": "+1 к смывке."},
        {"type": "monster", "name": "Летучие лягушки", "level": 6, "treasures": 2, "undead": False, "bad_stuff": "lose_lvl_2", "text": "-1 к смывке."},
        {"type": "monster", "name": "Хромой гоблин", "level": 1, "treasures": 1, "undead": False, "bad_stuff": "lose_lvl_1", "text": "+1 к смывке."},
        
        # Средние (6-12)
        {"type": "monster", "name": "Адвокат", "level": 6, "treasures": 2, "undead": False, "bad_stuff": "lose_hand_cards", "text": "Не нападает на воров."},
        {"type": "monster", "name": "Амазонка", "level": 8, "treasures": 2, "undead": False, "bad_stuff": "lose_class", "text": "Не бьет женщин. Дает сокровище просто так."},
        {"type": "monster", "name": "Бигфут", "level": 12, "treasures": 3, "undead": False, "bad_stuff": "lose_headgear", "text": "+3 против дварфов."},
        {"type": "monster", "name": "Языческий демон", "level": 12, "treasures": 3, "undead": False, "bad_stuff": "lose_lvl_1", "text": "+5 против клириков."},
        {"type": "monster", "name": "3872 Орка", "level": 10, "treasures": 3, "undead": False, "bad_stuff": "death", "text": "+6 против дварфов."},

        # Боссы (14-20)
        {"type": "monster", "name": "Король Тут", "level": 16, "treasures": 4, "undead": True, "bad_stuff": "lose_lvl_2", "text": "Нежить. Можно подкинуть без бродячей твари."},
        {"type": "monster", "name": "Кальмадзилла", "level": 18, "treasures": 4, "undead": False, "bad_stuff": "death", "text": "Слизьняки не помогают в бою."},
        {"type": "monster", "name": "Братья Зомби", "level": 16, "treasures": 4, "undead": True, "bad_stuff": "lose_lvl_2", "text": "Просыпаются к обеду."},
        {"type": "monster", "name": "Плутониевый дракон", "level": 20, "treasures": 5, "undead": False, "bad_stuff": "death", "text": "Не преследует тех, кто ниже 5 уровня."},
        {"type": "monster", "name": "Ужас в ночи", "level": 14, "treasures": 4, "undead": True, "bad_stuff": "lose_lvl_3", "text": "+4 против воров."},

        # --- ПРОКЛЯТИЯ (5 штук) ---
        {"type": "curse", "name": "Проклятие! Потеряй уровень", "effect_id": "lose_lvl_1", "text": "Ты чувствуешь, как опыт покидает тебя."},
        {"type": "curse", "name": "Проклятие! Курица на башне", "effect_id": "lose_headgear", "text": "Курица клюет твою макушку. Сбрось головняк."},
        {"type": "curse", "name": "Проклятие! Дырявые ботинки", "effect_id": "lose_footgear", "text": "Твоя обувь развалилась. Сбрось обувку."},
        {"type": "curse", "name": "Проклятие! Большая потеря", "effect_id": "lose_big_item", "text": "Сбрось одну большую шмотку."},
        {"type": "curse", "name": "Проклятие! Налоги", "effect_id": "lose_1_item", "text": "Сбрось 1 шмотку по выбору."},
    ],

    "treasures": [
        # --- ОРУЖИЕ (HANDS) ---
        {"type": "gear", "name": "Бензопила кровавого расчленения", "price": 600, "bonus": 3, "slot": "2hand", "is_big": True},
        {"type": "gear", "name": "Огромный камень", "price": 0, "bonus": 3, "slot": "2hand", "is_big": True},
        {"type": "gear", "name": "Палица остроты", "price": 400, "bonus": 4, "slot": "hand", "is_big": False}, # Только для клириков (игнорим)
        {"type": "gear", "name": "Меч широты взглядов", "price": 400, "bonus": 3, "slot": "hand", "is_big": False},
        {"type": "gear", "name": "Дубина", "price": 100, "bonus": 2, "slot": "hand", "is_big": False},
        {"type": "gear", "name": "Швейцарская армейская алебарда", "price": 600, "bonus": 4, "slot": "2hand", "is_big": True},
        {"type": "gear", "name": "Кинжал измены", "price": 400, "bonus": 2, "slot": "hand", "is_big": False},
        {"type": "gear", "name": "Рапира так-себе-остроты", "price": 200, "bonus": 2, "slot": "hand", "is_big": False},

        # --- БРОНЯ (BODY) ---
        {"type": "gear", "name": "Кожаный прикид", "price": 200, "bonus": 1, "slot": "body", "is_big": False},
        {"type": "gear", "name": "Слизьнявая броня", "price": 400, "bonus": 2, "slot": "body", "is_big": False},
        {"type": "gear", "name": "Мифриловая броня", "price": 600, "bonus": 3, "slot": "body", "is_big": True},
        {"type": "gear", "name": "Плащ замутненности", "price": 400, "bonus": 2, "slot": "body", "is_big": False},

        # --- ГОЛОВНЯК (HEAD) ---
        {"type": "gear", "name": "Шлем-рогач", "price": 600, "bonus": 1, "slot": "head", "is_big": False}, # +2 для эльфов (игнорим)
        {"type": "gear", "name": "Бандана крутизны", "price": 400, "bonus": 3, "slot": "head", "is_big": False}, # Только для людей
        {"type": "gear", "name": "Остроконечная шляпа", "price": 400, "bonus": 2, "slot": "head", "is_big": False},

        # --- ОБУВКА (FEET) ---
        {"type": "gear", "name": "Башмаки могучего пенделя", "price": 400, "bonus": 2, "slot": "feet", "is_big": False},
        {"type": "gear", "name": "Сандалеты протекции", "price": 700, "bonus": 2, "slot": "feet", "is_big": False}, # Защищают от проклятий в дверях
        
        # --- РАЗНОЕ (NONE SLOT) ---
        {"type": "gear", "name": "Наколенники развода", "price": 600, "bonus": 1, "slot": "none", "is_big": False},
        {"type": "gear", "name": "Колготки великанской силы", "price": 600, "bonus": 3, "slot": "none", "is_big": False},

        # --- БОНУС: ПОЛУЧИ УРОВЕНЬ (GUAL) ---
        {"type": "level_up", "name": "Получи уровень! (1000 голд)", "price": 1000, "text": "Продай шмотки и купи уровень."},
        {"type": "level_up", "name": "Получи уровень! (Зелье)", "price": 300, "text": "Выпей зелье и стань круче."},
        {"type": "level_up", "name": "Получи уровень! (Взятка ГМу)", "price": 0, "text": "Уговори мастера дать тебе уровень."}
    ]
}