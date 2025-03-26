# -*- coding: utf-8 -*-
from constants import Button, Channel

strings = {
    'uz': {
        'welcome': "🇺🇿 *Xush kelibsiz!*\n\nIltimos, tilni tanlang:",
        'language_selected': "🇺🇿 O'zbek tili tanlandi!",
        'subscription_required': f"❗️ Bot imkoniyatlaridan foydalanish uchun {{channel}} kanaliga obuna bo'ling!",
        'main_menu': "📱 *Asosiy menyu*\n\nQuyidagi tugmalardan birini tanlang:",
        'profile': "👤 *Mening profilim*\n\n🆔 ID: `{user_id}`\n👤 Username: @{username}\n📊 Sotuvdagi kodlar: {listings_count}",
        'sell_code_start': "💰 *Kodingizni sotish*\n\nIltimos, loyiha nomini kiriting:",
        'enter_project_link': "🔗 Loyiha havolasini kiriting (GitHub, GitLab, va h.k.):",
        'enter_technologies': "🛠 Qo'llanilgan texnologiyalarni kiriting (masalan: Python, Django, React):",
        'enter_price': "💵 Narxni USD da kiriting (faqat raqam):",
        'enter_description': "📝 Loyiha haqida qisqacha ma'lumot kiriting:",
        'enter_image': "🖼 Loyiha uchun rasm yuklang (ixtiyoriy, o'tkazib yuborish uchun \"O'tkazib yuborish\" tugmasini bosing):",
        'skip': Button.get_text(Button.SKIP, 'uz'),
        'confirm_listing': "✅ *Tasdiqlash*\n\n📝 *Loyiha nomi:* {name}\n🔗 *Havola:* {link}\n🛠 *Texnologiyalar:* {technologies}\n💵 *Narx:* ${price}\n📜 *Tavsif:* {description}\n\nMa'lumotlar to'g'rimi?",
        'yes': Button.get_text(Button.YES, 'uz'),
        'no': Button.get_text(Button.NO, 'uz'),
        'listing_submitted': "✅ Sizning e'loningiz moderatorlarga yuborildi. Tasdiqlangandan so'ng kanalda e'lon qilinadi.",
        'help': "❓ *Yordam*\n\nBot imkoniyatlari:\n\n👤 *Mening profilim* - Profil ma'lumotlaringizni ko'rish\n💰 *Kodimni sotish* - Kanalingizda kod sotish uchun e'lon joylashtirish\n\nQo'shimcha savollar uchun: @abdulaziz_python",
        'admin_panel': "🛠 *Admin panel*\n\n👥 Jami foydalanuvchilar: {total_users}\n📊 Jami e'lonlar: {total_listings}",
        'broadcast': "📢 *Xabar tarqatish*\n\nBarcha foydalanuvchilarga xabar yuborish uchun matn kiriting:",
        'broadcast_sent': "✅ Xabar {count} ta foydalanuvchiga yuborildi!",
        'new_listing': "⚠️ *Yangi e'lon moderatsiya uchun*\n\n👤 Foydalanuvchi: @{username}\n📝 *Loyiha nomi:* {name}\n🔗 *Havola:* {link}\n🛠 *Texnologiyalar:* {technologies}\n💵 *Narx:* ${price}\n📜 *Tavsif:* {description}",
        'approve': Button.get_text(Button.CONFIRM, 'uz'),
        'reject': Button.get_text(Button.CANCEL, 'uz'),
        'listing_approved': "✅ E'lon tasdiqlandi va kanalga joylashtirildi!",
        'listing_rejected': "❌ E'lon rad etildi!",
        'announcement': f"📢 *Yangi kod sotuvda!*\n\n💻 *Loyiha nomi:* {{name}}\n🔗 *Havola:* {{link}}\n🛠 *Texnologiyalar:* {{technologies}}\n💵 *Narx:* ${{price}}\n📜 *Tavsif:* {{description}}\n👨‍💻 *Dasturchi:* {{owner}}\n\n🔥 {Channel.COOPLINK}"
    },
    'ru': {
        'welcome': "🇷🇺 *Добро пожаловать!*\n\nПожалуйста, выберите язык:",
        'language_selected': "🇷🇺 Выбран русский язык!",
        'subscription_required': f"❗️ Для использования возможностей бота, подпишитесь на канал {{channel}}!",
        'main_menu': "📱 *Главное меню*\n\nВыберите одну из кнопок ниже:",
        'profile': "👤 *Мой профиль*\n\n🆔 ID: `{user_id}`\n👤 Имя пользователя: @{username}\n📊 Кодов на продаже: {listings_count}",
        'sell_code_start': "💰 *Продажа вашего кода*\n\nПожалуйста, введите название проекта:",
        'enter_project_link': "🔗 Введите ссылку на проект (GitHub, GitLab и т.д.):",
        'enter_technologies': "🛠 Введите использованные технологии (например: Python, Django, React):",
        'enter_price': "💵 Введите цену в USD (только число):",
        'enter_description': "📝 Введите краткое описание проекта:",
        'enter_image': "🖼 Загрузите изображение для проекта (необязательно, нажмите \"Пропустить\" для пропуска):",
        'skip': Button.get_text(Button.SKIP, 'ru'),
        'confirm_listing': "✅ *Подтверждение*\n\n📝 *Название проекта:* {name}\n🔗 *Ссылка:* {link}\n🛠 *Технологии:* {technologies}\n💵 *Цена:* ${price}\n📜 *Описание:* {description}\n\nДанные верны?",
        'yes': Button.get_text(Button.YES, 'ru'),
        'no': Button.get_text(Button.NO, 'ru'),
        'listing_submitted': "✅ Ваше объявление отправлено модераторам. После подтверждения оно будет опубликовано в канале.",
        'help': "❓ *Помощь*\n\nВозможности бота:\n\n👤 *Мой профиль* - Просмотр информации о вашем профиле\n💰 *Продать код* - Разместить объявление о продаже кода в канале\n\nДля дополнительных вопросов: @abdulaziz_python",
        'admin_panel': "🛠 *Панель администратора*\n\n👥 Всего пользователей: {total_users}\n📊 Всего объявлений: {total_listings}",
        'broadcast': "📢 *Рассылка сообщений*\n\nВведите текст для отправки всем пользователям:",
        'broadcast_sent': "✅ Сообщение отправлено {count} пользователям!",
        'new_listing': "⚠️ *Новое объявление на модерацию*\n\n👤 Пользователь: @{username}\n📝 *Название проекта:* {name}\n🔗 *Ссылка:* {link}\n🛠 *Технологии:* {technologies}\n💵 *Цена:* ${price}\n📜 *Описание:* {description}",
        'approve': Button.get_text(Button.CONFIRM, 'ru'),
        'reject': Button.get_text(Button.CANCEL, 'ru'),
        'listing_approved': "✅ Объявление одобрено и размещено в канале!",
        'listing_rejected': "❌ Объявление отклонено!",
        'announcement': f"📢 *Новый код в продаже!*\n\n💻 *Название проекта:* {{name}}\n🔗 *Ссылка:* {{link}}\n🛠 *Технологии:* {{technologies}}\n💵 *Цена:* ${{price}}\n📜 *Описание:* {{description}}\n👨‍💻 *Разработчик:* {{owner}}\n\n🔥 {Channel.COOPLINK}"
    }
}

def get_string(key, language='uz'):
    if language not in strings:
        language = 'uz'
        
    if key not in strings[language]:
        return strings['uz'].get(key, f"Missing string: {key}")
        
    return strings[language][key]

