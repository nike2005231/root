def motives_choice(archetype):
    motives_map = {
        'авантюрист': [
            """
            Развитие происходит при:

                1. Амбиция — при увеличении репутации у любой фракции.
                2. Принципы — при воплощении моральных принципов с большими затратами для себя или союзников.
                3. Справедливость — если ваш ПИ добился справедливости для пострадавшего от сильного врага.
                4. Чистые лапы — при достижении преступной цели с правдоподобным алиби.
            """,
            "Амбиция — при увеличении репутации у любой фракции.",
            "Принципы — при воплощении моральных принципов с большими затратами для себя или союзников.",
            "Справедливость — если ваш ПИ добился справедливости для пострадавшего от сильного врага.",
            "Чистые лапы — при достижении преступной цели с правдоподобным алиби."
        ],
        'судья': [
            """
            Развитие происходит при:

                1. Верность — при выполнении приказа важного персонажа с большими затратами.
                2. Защита — если подопечный ПИ в безопасности или спасён от опасности.
                3. Принципы — при воплощении моральных принципов с затратами.
                4. Справедливость — при восстановлении справедливости в пользу слабого.
            """,
            "Верность — при выполнении приказа важного персонажа с большими затратами.",
            "Защита — если подопечный ПИ в безопасности или спасён от опасности.",
            "Принципы — при воплощении моральных принципов с затратами.",
            "Справедливость — при восстановлении справедливости в пользу слабого."
        ],
        'налетчик': [
            """
            Развитие происходит при:

                1. Бесчестье — при снижении репутации у фракции.
                2. Открытие — при нахождении чего-то нового или чудесного.
                3. Преступление — при успешной криминальной операции в сложных условиях.
                4. Странствия — при завершении путешествия к поляне.
            """,
            "Бесчестье — при снижении репутации у фракции.",
            "Открытие — при нахождении чего-то нового или чудесного.",
            "Преступление — при успешной криминальной операции в сложных условиях.",
            "Странствия — при завершении путешествия к поляне."
        ],
        'следопыт': [
            """
            Развитие происходит при:

                1. Защита — при защите подопечного или его безопасности.
                2. Месть — при нанесении вреда врагу или его интересам.
                3. Открытие — при обнаружении нового или чудесного.
                4. Свобода — при освобождении угнетённых.
            """,
            "Защита — при защите подопечного или его безопасности.",
            "Месть — при нанесении вреда врагу или его интересам.",
            "Открытие — при обнаружении нового или чудесного.",
            "Свобода — при освобождении угнетённых."
        ],
        'ронин': [
            """
            Развитие происходит при:

                1. Месть — при вреде врагу или его интересам.
                2. Острые ощущения — при спасении от смерти или ареста.
                3. Принципы — при действии согласно принципам с затратами.
                4. Странствия — при завершении путешествия к поляне.
            """,
            "Месть — при вреде врагу или его интересам.",
            "Острые ощущения — при спасении от смерти или ареста.",
            "Принципы — при действии согласно принципам с затратами.",
            "Странствия — при завершении путешествия к поляне."
        ],
        'поджигатель': [
            """
            Развитие происходит при:

                1. Бесчестье — при снижении репутации.
                2. Острые ощущения — при спасении от смерти или ареста.
                3. Преступление — при получении ценного нелегально.
                4. Хаос — при свержении жестокой власти.
            """,
            "Бесчестье — при снижении репутации.",
            "Острые ощущения — при спасении от смерти или ареста.",
            "Преступление — при получении ценного нелегально.",
            "Хаос — при свержении жестокой власти."
        ],
        'вор': [
            """
            Развитие происходит при:

                1. Амбиция — при росте репутации у фракции.
                2. Жадность — при получении ценного трофея или сокровища.
                3. Острые ощущения — при спасении от смерти или ареста.
                4. Свобода — при освобождении угнетённых.
            """,
            "Амбиция — при росте репутации у фракции.",
            "Жадность — при получении ценного трофея или сокровища.",
            "Острые ощущения — при спасении от смерти или ареста.",
            "Свобода — при освобождении угнетённых."
        ],
        'ремесленник': [
            """
            Развитие происходит при:

                1. Амбиция — при увеличении репутации у фракции.
                2. Жадность — при получении серьёзной награды.
                3. Защита — если подопечный спасён или в безопасности.
                4. Месть — при вреде врагу или его интересам.
            """,
            "Амбиция — при увеличении репутации у фракции.",
            "Жадность — при получении серьёзной награды.",
            "Защита — если подопечный спасён или в безопасности.",
            "Месть — при вреде врагу или его интересам."
        ],
        'скиталец': [
            """
            Развитие происходит при:

                1. Амбиция — при получении престижа у фракции.
                2. Свобода — при освобождении кого-либо от ограничений.
                3. Исследование — при открытии новых мест или тайн.
                4. Одиночество — при успешных действиях в одиночку.
            """,
            "Амбиция — при получении престижа у фракции.",
            "Свобода — при освобождении кого-либо от ограничений.",
            "Исследование — при открытии новых мест или тайн.",
            "Одиночество — при успешных действиях в одиночку."
        ]
    }
    return motives_map[archetype.lower()]
