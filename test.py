import pprint

from data_science_module.ds_module import text_source_sentiment_score, text_source_facts_comparison, \
    get_sentiment_scores

text_source = 'Москва признана первой среди европейских городов в рейтинге инноваций, помогающих в формировании ' \
              'устойчивости коронавирусу. Она опередила Лондон и Барселону.\nСреди мировых мегаполисов российская ' \
              'столица занимает третью строчку — после Сан-Франциско и Нью-Йорка. Пятерку замыкают Бостон и Лондон. ' \
              'Рейтинг составило международное исследовательское агентство StartupBlink.\n\nДобиться высоких ' \
              'показателей Москве помогло почти 160 передовых решений, которые применяются для борьбы с ' \
              'распространением коронавируса. Среди них алгоритмы компьютерного зрения на основе искусственного ' \
              'интеллекта. Это методика уже помогла рентгенологам проанализировать более трех миллионов ' \
              'исследований.\n\nЕще одно инновационное решение — облачная платформа, которая объединяет пациентов, ' \
              'врачей, медицинские организации, страховые компании, фармакологические производства и сайты. ' \
              'Способствовали высоким результатам и технологии, которые помогают адаптировать жизнь горожан во время ' \
              'пандемии. Это проекты в сфере умного туризма, электронной коммерции и логистики, а также дистанционной ' \
              'работы и онлайн-образования.\n\nЭксперты агентства StartupBlink оценивали принятые в Москве меры с ' \
              'точки зрения эпидемиологических показателей и влияния на экономику.\n\nВ борьбе с коронавирусом Москва ' \
              'отказалась от крайностей. Ставку сделали на профилактику: увеличили количество пунктов бесплатного ' \
              'экспресс-тестирования и вакцинации, запатентовали онлайн-программы и платформы для обучения, ' \
              'развивали возможности телемедицины.\n\nМосковская система здравоохранения за время пандемии накопила ' \
              'достаточно большой запас прочности, который позволяет не останавливать плановую и экстренную помощь ' \
              'даже в периоды пиков заболеваемости COVID-19.\n\nСтолица поддерживает бизнес, выделяя субсидии и ' \
              'предоставляя льготы. В этом году мерами поддержки воспользовалось около 25 тысяч предприятий малого и ' \
              'среднего бизнеса.\n\nРейтинг составляется на базе глобальной карты инновационных решений по борьбе с ' \
              'коронавирусом и оценивает около 100 ведущих городов и 40 стран мира. Глобальная карта была создана в ' \
              'марте 2020 года, и в течение года на нее было добавлено более тысячи решений. '
text_source_title = 'В мире Москва занимает третье место, уступая лишь Нью-Йорку и Сан-Франциско.'

text = 'Бостон признан первым среди европейских городов в рейтинге инноваций, помогающих в формировании устойчивости коронавирусу. Он опередил Лондон, Барселону и Андроново.\n' \
       'В мире Бостон занимает третье место, уступая лишь Нью-Йорку и Сан-Франциско. Андроново не участвовало в оценке в этом году. Рейтинг составило международное исследовательское агентство StartupBlink.\n' \
       'Обойти преследователей Бостону помогло более 100 передовых решений, которые применяются для борьбы с распространением коронавируса.\n' \
       'В свою очередь Андроново уже несколько лет не участвует в рейтинге по причине отсутствия кислорода в атмосфере города и водорода в составе воды в реке Лене.\n' \
       'В качестве инновационного решения, позволяющего исправить положение, неким человеком на улице было предложено использовать фаршированных гонобобелем голубей для обеспечения регулярного авиасообщения с планетой Железяка.\n' \
       'Другое предложенное решение оказалось ещё более странным, чем предыдущее — облачная платформа, которая объединяет перистые и кучевые облака в сверхмассивный кластер инновационных перисто-кучевых облаков.\n' \
       'Такого рода высокие технологии вряд ли помогут Андронову занять какое-либо место в каком-нибудь конкурсе.'
text_title = 'Бостон занял первое место среди европейских городов в рейтинге инноваций в медицине, а Андроново отказалось от участия в оценке'

sentiment_score = text_source_sentiment_score(text, text_title, text_source, text_source_title)

negative_score, positive_score, neutral_score, skip_score, speech_score, clickbait_score, rationality_score, intuition_score = get_sentiment_scores(
    text, text_title)

error_numerical_facts_score, error_ner_facts_score, facts_message = text_source_facts_comparison(text, text_source)

pprint.pprint({'sentiment_index': sentiment_score,
               'facts': facts_message,
               'error_numerical_facts_score': error_numerical_facts_score,
               'error_ner_facts_score': error_ner_facts_score,
               'intuition_score': intuition_score,
               'speech_index': speech_score})
