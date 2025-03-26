from constants import Button, Channel

def get_string(key, language='uz'):
    strings = {
        'uz': {
            'welcome': "🇺🇿 <b>Xush kelibsiz!</b>\n\nIltimos, tilni tanlang:",
            'language_selected': "🇺🇿 O'zbek tili tanlandi!",
            'subscription_required': "❗️ Bot imkoniyatlaridan foydalanish uchun {channel} kanaliga obuna bo'ling!",
            'main_menu': "📱 <b>Asosiy menyu</b>\n\nQuyidagi tugmalardan birini tanlang:",
            'profile': "👤 <b>Mening profilim</b>\n\n🆔 ID: <code>{user_id}</code>\n👤 Username: @{username}\n📊 Sotuvdagi kodlar: {listings_count}",
            'sell_code_start': "💰 <b>Kodingizni sotish</b>\n\nIltimos, loyiha nomini kiriting:",
            'enter_project_link': "🔗 Loyiha havolasini kiriting (GitHub, GitLab, va h.k.):",
            'enter_technologies': "🛠 Qo'llanilgan texnologiyalarni kiriting (masalan: Python, Django, React):",
            'enter_price': "💵 Narxni USD da kiriting (faqat raqam):",
            'enter_description': "📝 Loyiha haqida qisqacha ma'lumot kiriting:",
            'enter_image': "🖼 Loyiha uchun rasm yuklang (ixtiyoriy, o'tkazib yuborish uchun \"O'tkazib yuborish\" tugmasini bosing):",
            'skip': Button.get_text(Button.SKIP, 'uz'),
            'confirm_listing': "✅ <b>Tasdiqlash</b>\n\n📝 <b>Loyiha nomi:</b> {name}\n🔗 <b>Havola:</b> {link}\n🛠 <b>Texnologiyalar:</b> {technologies}\n💵 <b>Narx:</b> ${price}\n📜 <b>Tavsif:</b> {description}\n\nMa'lumotlar to'g'rimi?",
            'yes': Button.get_text(Button.YES, 'uz'),
            'no': Button.get_text(Button.NO, 'uz'),
            'listing_submitted': "✅ Sizning e'loningiz moderatorlarga yuborildi. Tasdiqlangandan so'ng kanalda e'lon qilinadi.",
            'help': "❓ <b>Yordam</b>\n\nBot imkoniyatlari:\n\n👤 <b>Mening profilim</b> - Profil ma'lumotlaringizni ko'rish\n💰 <b>Kodimni sotish</b> - Kanalingizda kod sotish uchun e'lon joylashtirish\n\nQo'shimcha savollar uchun: @abdulaziz_python",
            'admin_panel': "🛠 <b>Admin panel</b>\n\n👥 Jami foydalanuvchilar: {total_users}\n📊 Jami e'lonlar: {total_listings}",
            'broadcast_prompt': "📢 <b>Xabar tarqatish</b>\n\nBarcha foydalanuvchilarga xabar yuborish uchun matn kiriting:",
            'broadcast_started': "✅ Xabar yuborish boshlandi...",
            'broadcast_completed': "✅ Xabar yuborish yakunlandi.\n\nYuborildi: {sent}\nYuborilmadi: {failed}",
            'new_listing': "⚠️ <b>Yangi e'lon moderatsiya uchun</b>\n\n👤 Foydalanuvchi: @{username}\n📝 <b>Loyiha nomi:</b> {name}\n🔗 <b>Havola:</b> {link}\n🛠 <b>Texnologiyalar:</b> {technologies}\n💵 <b>Narx:</b> ${price}\n📜 <b>Tavsif:</b> {description}",
            'approve': Button.get_text(Button.CONFIRM, 'uz'),
            'reject': Button.get_text(Button.CANCEL, 'uz'),
            'listing_approved': "✅ E'lon #{listing_id} tasdiqlandi va kanalga joylashtirildi!",
            'listing_rejected': "❌ E'lon #{listing_id} rad etildi!",
            'your_listing_approved': "✅ Sizning \"{listing_name}\" e'loningiz tasdiqlandi va kanalda e'lon qilindi!",
            'your_listing_rejected': "❌ Sizning \"{listing_name}\" e'loningiz rad etildi.",
            'nothing_to_cancel': "❌ Hech qanday faol amal yo'q.",
            'action_cancelled': "✅ Amal bekor qilindi.",
            'announcement': f"📢 <b>Yangi kod sotuvda!</b>\n\n💻 <b>Loyiha nomi:</b> {{name}}\n🔗 <b>Havola:</b> {{link}}\n🛠 <b>Texnologiyalar:</b> {{technologies}}\n💵 <b>Narx:</b> ${{price}}\n📜 <b>Tavsif:</b> {{description}}\n👨‍💻 <b>Dasturchi:</b> {{owner}}\n\n🔥 {Channel.COOPLINK}"
        },
        'ru': {
            'welcome': "🇷🇺 <b>Добро пожаловать!</b>\n\nПожалуйста, выберите язык:",
            'language_selected': "🇷🇺 Выбран русский язык!",
            'subscription_required': "❗️ Для использования возможностей бота, подпишитесь на канал {channel}!",
            'main_menu': "📱 <b>Главное меню</b>\n\nВыберите одну из кнопок ниже:",
            'profile': "👤 <b>Мой профиль</b>\n\n🆔 ID: <code>{user_id}</code>\n👤 Имя пользователя: @{username}\n📊 Кодов на продаже: {listings_count}",
            'sell_code_start': "💰 <b>Продажа вашего кода</b>\n\nПожалуйста, введите название проекта:",
            'enter_project_link': "🔗 Введите ссылку на проект (GitHub, GitLab и т.д.):",
            'enter_technologies': "🛠 Введите использованные технологии (например: Python, Django, React):",
            'enter_price': "💵 Введите цену в USD (только число):",
            'enter_description': "📝 Введите краткое описание проекта:",
            'enter_image': "🖼 Загрузите изображение для проекта (необязательно, нажмите \"Пропустить\" для пропуска):",
            'skip': Button.get_text(Button.SKIP, 'ru'),
            'confirm_listing': "✅ <b>Подтверждение</b>\n\n📝 <b>Название проекта:</b> {name}\n🔗 <b>Ссылка:</b> {link}\n🛠 <b>Технологии:</b> {technologies}\n💵 <b>Цена:</b> ${price}\n📜 <b>Описание:</b> {description}\n\nДанные верны?",
            'yes': Button.get_text(Button.YES, 'ru'),
            'no': Button.get_text(Button.NO, 'ru'),
            'listing_submitted': "✅ Ваше объявление отправлено модераторам. После подтверждения оно будет опубликовано в канале.",
            'help': "❓ <b>Помощь</b>\n\nВозможности бота:\n\n👤 <b>Мой профиль</b> - Просмотр информации о вашем профиле\n💰 <b>Продать код</b> - Разместить объявление о продаже кода в канале\n\nДля дополнительных вопросов: @abdulaziz_python",
            'admin_panel': "🛠 <b>Панель администратора</b>\n\n👥 Всего пользователей: {total_users}\n📊 Всего объявлений: {total_listings}",
            'broadcast_prompt': "📢 <b>Рассылка сообщений</b>\n\nВведите текст для отправки всем пользователям:",
            'broadcast_started': "✅ Рассылка сообщений начата...",
            'broadcast_completed': "✅ Рассылка сообщений завершена.\n\nОтправлено: {sent}\nНе отправлено: {failed}",
            'new_listing': "⚠️ <b>Новое объявление на модерацию</b>\n\n👤 Пользователь: @{username}\n📝 <b>Название проекта:</b> {name}\n🔗 <b>Ссылка:</b> {link}\n🛠 <b>Технологии:</b> {technologies}\n💵 <b>Цена:</b> ${price}\n📜 <b>Описание:</b> {description}",
            'approve': Button.get_text(Button.CONFIRM, 'ru'),
            'reject': Button.get_text(Button.CANCEL, 'ru'),
            'listing_approved': "✅ Объявление #{listing_id} одобрено и размещено в канале!",
            'listing_rejected': "❌ Объявление #{listing_id} отклонено!",
            'your_listing_approved': "✅ Ваше объявление \"{listing_name}\" одобрено и опубликовано в канале!",
            'your_listing_rejected': "❌ Ваше объявление \"{listing_name}\" отклонено.",
            'nothing_to_cancel': "❌ Нет активных действий для отмены.",
            'action_cancelled': "✅ Действие отменено.",
            'announcement': f"📢 <b>Новый код в продаже!</b>\n\n💻 <b>Название проекта:</b> {{name}}\n🔗 <b>Ссылка:</b> {{link}}\n🛠 <b>Технологии:</b> {{technologies}}\n💵 <b>Цена:</b> ${{price}}\n📜 <b>Описание:</b> {{description}}\n👨‍💻 <b>Разработчик:</b> {{owner}}\n\n🔥 {Channel.COOPLINK}"
        }
    }
    
    if language not in strings:
        language = 'uz'
        
    if key not in strings[language]:
        return strings['uz'].get(key, f"Missing string: {key}")
        
    return strings[language][key]