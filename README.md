# Data Science Модуль Описание 
Подробное описание с примерами использования можно посмотреть [здесь](./usage_example.ipynb) 

## Установка

### Requirements
python==3.9

```
conda create --name test_terminal_ds_module python=3.9
conda activate test_terminal_ds_module
pip install git+https://github.com/korney3/fact_extractor_emotion_classifier
python -m dostoevsky download fasttext-social-network-model
```

## Пример использования

```
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
```


## Анализ эмоций

Модуль, отвечающий за скоринг эмоциональных аспектов текстов статьи. Состоит из трех частей: анализатора настроения текста, проверки заголовка статьи на кликбейтность и оценка рациональности\интуитивности текста. 

В нвоостях зачастую используется нейтральный стиль изложения. Появление выраженного эмоционального окраса присуще фейковым новостям. Также отличие эмоционального окраса в первоисточнике и анализируемой новости может свидетельствовать о появлении фейковости.

### Анализатор настроения текста

[Dostoevsky](https://github.com/bureaucratic-labs/dostoevsky) - библиотека, анализирующая настроение текста на русском языке. Классифицирует текст на 5 классов - негативное, позитивное и нейтральное настроение, а так же классифицирует части текста как речевой акт или в неясных случаях дает ответ "пропустить". Для каждого из 5 классов модель выдает скор от 0 до 1, скоры по 5-ти классам в сумме дают 1.

Наша гипотеза заключается в том, что появление высоких коэффициентов у негативного и позитивного классов может коррелировать с фейковостью новости.

### Проверка заголовка на кликбейтность

Модель классификатора, обученная на [датасете](https://github.com/bhargaviparanjape/clickbait). Выдает скор от 0 до 1, где 1 - кликбейт, а 0 - не-кликбейт.

Кликбейтные заголовки обычно принадлежат новостям, цель которых не изложить информацию, а привлечь внимание, что может привести к фейковости.

Модель обучена для английского языка, для классификации заголовков на русском языке дополнительно используется библиотека [translate-python](https://github.com/terryyin/translate-python).

Алгоритм обучения модели: тексты в датасете были очищены от всех символов, кроме букв и приведены к нормальной форме. Стоп-слова не были удалены, поскольку они могут свидетельствовать о кликбейтности. Векторизация текстов была сделана при помощи `tf-idf` трансформера. Логистическая регрессия была использована в качестве модели классификации.

На выборке английский заголовков были получены следующие метрики качества:
![](https://sun9-77.userapi.com/s/v1/if2/I66qVXB9GEb4PK8yNy2O2jInyBx9gqHVnrMu6FkyK2sGHZlxiL7rGneG7CCRCED0NT3J7Qq17AutyGHhXnvIaov6.jpg?size=425x159&quality=96&type=album)

Для оценки качества модели на русских заголовках был собран и размечен датасет `data_clickbait` заголовков с подозрением на кликбейт и без.

### Оценка рациональности\интуитивности текста

Для оценки рациональности и интуитивности текста были созданы корпуса слов, которые имеют характер рациональности (`доказательство, анализировать, результат и т.д`) и интуитивности (`воображать, думать, чувствовать и т.д.`). Рациональность и интуитивность оцениваются как скор от 0 до 1 - относительное количество рациональных и интуитивных терминов к количеству слов в тексте.

В новостях, где интуитивный скор высокий, а рациональный - низкий, может присутствовать больше непроверенны фактов и голословных утверждений, что  может коррелировать с фейковостью.

Подход и стартовые корпуса слов взяты из проекта [polids](https://github.com/AndreCNF/polids) и переведены модулем [translate-python](https://github.com/terryyin/translate-python) с португальского на русский.

Сейчас этот модуль находится в стадии MVP (корпуса слов ограничены), при масштабировании решения они будут расширены.

### Расстояние между текстами в векторном пространстве скоров эмоций

Все полученные скоры были собраны в вектор, отражающий эмоциональную окраску текста. Для первоисточника и анализируемого текста считается косинусное расстояние между полученными векторами. Этот скор принимает значения от 0 до 1, где 0 - эмоциональный окрас идентичен, а 1 - эмоциональный окрас новостей несовпадает.

Большое расхождение эмоциональных окрасов оригинала и ананлизируемого текста может свидетельствовать о фейковости новости.

## Фактчекинг

Модуль, выделяющий в тексте две группы фактов: числовые факты (`информация о числе объектов, номерах и тд`) и сущностные факты (`людей, места, организации и тд`).

Выделенные факты сравниваются между первоисточником и анализируемой статьей, факты, где основная информация не совпадает (количество или ключевые объекты) помечаются как ошибочными. Скором ошибок фактов является относительное количество ошибочных фактов к общему числу найденных фактов.

### Числовые факты

Факты выделяются при помощи набора правил в парсере [yargy](https://github.com/natasha/yargy): сложные текстовые числительные переводятся в числа, объект факта выделяется как прилагательное+существительное, следующие за числом. По одинаковым объектам происходит сравнение чисел для текста-первоисточника и анализируемого текста.

Для объектов-существительных происходит дополнительное сравнение по синонимам из библиотеки [wiki-ru-wordnet](https://wiki-ru-wordnet.readthedocs.io/en/latest/).

### Сущности - факты

Факты-сущности (NER) выделяются при помощи библиотеки [natasha](https://github.com/natasha): словосочетания, относящиеся к людям, локациям, организациям.

Для первоисточника по каждой группе сущностей (люди, локации, организации) выбирается самая часто встречающаяся сущность как ключевая, если она не встречается в перепечатанном тексте - выводится ошибка.

Если в перепечатанном тексте присутствуют сущности, которых нет в источнике - они так же выделяются.
