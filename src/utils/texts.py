# common texts for bot
import pytz

MY_TIMEZONE = pytz.timezone('Europe/Moscow')


welcome_support = '''
Я являюсь ботом поддержки, через которы Ты 
можешь получить доступ к полнофункциональному боту.

Что имеет полноценный бот:

1. Систематизированную базу данных о важных добавках
2. Может контролировать твои состояние
3. Будет напоминать тебе о приёмах
4. Имеет специально разработанные курсы

🔑 Для использования полноценного бота требуется
особый пропуск:
/access

🔧 Для взаимодействия рекомендуем использовать
левые боковые команды или ниже:
'''


welcome_main = f'''
👁️ Это точка отсчёта.
                                       
'''

# helping
help_info = '''
Отзыв? Проблема? Предложение?
'''

send_review = '''
Пиши здесь 

Если передумал, введи "пропустить"
'''


you_are_access_user = '''
🔑 Добро пожаловать

<i>Начало: {buy_time}</i>
<i>Конец: {end_time}</i>

Бот: @your_supplementation_bot
'''


you_are_not_access_user = '''
🛑 Я не работаю бесплатно

@OkulussSuportBot
'''



for_library = '''
Википедия о наиболее полезных БАДах и рейтинг.
'''


timetable_info = '''
Твоё персональное расписание
'''

course_info = '''
Раздел специализированных курсов
'''



only_course_sections = [
    '📆 Мой курс',
    '📝👨‍⚕️ Готовые курсы'
]

course_names = [
    '🫨 Депрессия',
    '💪 Тренировка',
    '🤒 Простуда',
    '😈 Тестостерон'
]


step_1 = '''
⚙️ <b>Шаг 1/4</b>:
Добавь название (например: габа, теанин утром)

Для отмены напиши "пропустить"
'''

step_2 = '''
⚙️ <b>Шаг 2/4</b>:
Добавь дозировку (например, если штуки - 55 штук, если грамы - 1.5)

Для отмены напиши "пропустить"
'''

step_3 = '''
⚙️ <b>Шаг 3/4</b>:
Выбери нужное время приёма

Для отмены напиши "пропустить"
'''

completed_courses_info = '''
Тут будут расположены уже готовые курсы приёма
добавок по разным темам:
'''


depression_info = '''
🫨 Депрессия

💡 Депрессия - это серьезное психическое
расстройство, которое может серьезно влиять
на качество жизни человека.
В нашем курсе мы предлагаем набор проверенных
добавок, которые помогут вам преодолеть
депрессию и вернуть радость жизни.
'''


training_info = '''
💪 Тренировка

💡 Этот курс предназначен для спортсменов,
которые хотят максимально эффективно использовать
спортивные добавки для улучшения своих спортивных
результатов. В рамках курса вы узнаете, какие виды
БАДов существуют, как правильно выбрать подходящие
для вас добавки, как их применять.
'''
