# Data Science Модуль Описание 
Подробное описание с примерами использования можно посмотреть [здесь](./usage_example.ipynb) 

## Установка

### Requirements
python==3.9

```
nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
python -m dostoevsky download fasttext-social-network-model
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
