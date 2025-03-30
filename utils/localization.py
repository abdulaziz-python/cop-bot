from constants import Button, Channel

def get_string(key, language='uz'):
    texts = {
        'uz': {
            'welcome': "<b>👋 Assalomu alaykum, hurmatli foydalanuvchi!</b>\n\nCooplink botga xush kelibsiz. Iltimos, muloqot tilini tanlang:",
            'language_selected': "<b>✅ Til muvaffaqiyatli o'zgartirildi.</b>\n\nBot imkoniyatlaridan foydalanish uchun asosiy menyu tugmalaridan foydalaning.",
            'profile': "<b>👤 Foydalanuvchi ma'lumotlari</b>\n\nID: <code>{user_id}</code>\nUsername: @{username}\nJami e'lonlar: {listings_count} ta",
            'help': "<b>🔍 Botdan foydalanish yo'riqnomasi</b>\n\nBu bot orqali siz o'z dasturlash kod mahsulotlaringizni sotish uchun e'lon joylashtirishingiz mumkin.\n\n<b>Asosiy buyruqlar:</b>\n/start - Botni ishga tushirish\n/cancel - Joriy amalni bekor qilish\n\nSavollar yoki takliflar bo'lsa, @y0rdam42 ga murojaat qiling.",
            'command_list': "🤖 <b>Bot buyruqlari:</b>\n\n/start - Botni ishga tushirish\n/cancel - Joriy amalni bekor qilish\n/profile - Profil ma'lumotlarini ko'rish\n/help - Yordam",
            'sell_code_start': "<b>📝 Dasturlash mahsulotini sotish</b>\n\nIltimos, loyiha/kod nomini kiriting:",
            
            'admin_panel': "<b>Administrator boshqaruv paneli</b>\n\nJami foydalanuvchilar: {total_users}\nJami e'lonlar: {total_listings}",
            'broadcast_prompt': "<b>Barcha foydalanuvchilarga yuborish uchun xabarni kiriting:</b>",
            'broadcast_started': "<b>Xabar yuborilmoqda, iltimos kuting...</b>",
            'broadcast_completed': "<b>Xabar yuborish muvaffaqiyatli yakunlandi!</b>\n\nYuborildi: {sent} foydalanuvchilarga\nYuborilmadi: {failed} foydalanuvchilarga",
            'listing_approved': "<b>E'lon #{listing_id} muvaffaqiyatli tasdiqlandi va kanalga joylashtirildi.</b>",
            'listing_rejected': "<b>E'lon #{listing_id} rad etildi.</b>",
            
            'no_users': "<b>Tizimda foydalanuvchilar mavjud emas.</b>",
            'users_list': "<b>Jami foydalanuvchilar soni: {total}</b>\n\n{users}",
            'user_item': "{number}. ID: <code>{id}</code> - @{username} - Til: {language} - Qo'shilgan sana: {date}\n",
            
            'no_listings': "<b>Tizimda e'lonlar mavjud emas.</b>",
            'listings_header': "<b>Barcha e'lonlar ro'yxati</b> (Sahifa {page}/{total_pages})\n\n",
            'listing_item': "ID: <code>{id}</code> - {name}\nMuallif: @{username}\nNarxi: ${price}\nHolati: {status}\nSana: {date}\n\n",
            'prev_page': "« Oldingi sahifa",
            'next_page': "Keyingi sahifa »",
            
            'users_button': "👥 Foydalanuvchilar ro'yxati",
            'listings_button': "📋 E'lonlar ro'yxati",
            'broadcast_button': "📣 Ommaviy xabar yuborish",
            'back_button': "🔙 Orqaga qaytish",
            'view_details': "🔍 Batafsil ma'lumot ko'rish",
            'select_listing': "<b>Ko'rmoqchi bo'lgan e'lonni tanlang:</b>",
            'listing_details': "<b>E'lon to'liq ma'lumotlari</b>\n\nID: <code>{id}</code>\nNomi: {name}\nMuallif: @{username}\nNarxi: ${price}\nHolati: {status}\nSana: {date}\n\nHavola: {link}\nTexnologiyalar: {technologies}\n\nTavsif:\n{description}",
            
            'enter_project_link': "<b>Loyiha havolasini kiriting:</b>\n\nGitHub, GitLab yoki boshqa manba havolasini kiriting.",
            'enter_technologies': "<b>Qo'llanilgan texnologiyalarni kiriting:</b>\n\nMisol uchun: Python, Django, React, PostgreSQL",
            'enter_price': "<b>Mahsulot narxini kiriting:</b>\n\nFaqat raqam kiriting, masalan: 50 (USD hisobida)",
            'enter_description': "<b>Loyiha tavsifini kiriting:</b>\n\nBu yerda loyiha haqida batafsil ma'lumot bering.",
            'enter_image': "<b>Loyiha uchun rasm yuklang:</b>\n\nRasm yubormaslik uchun \"O'tkazib yuborish\" tugmasini bosing.",
            'confirm_listing': "<b>E'lon ma'lumotlarini tasdiqlang:</b>\n\nNomi: {name}\nHavola: {link}\nTexnologiyalar: {technologies}\nNarxi: ${price}\n\nTavsif: {description}\n\nMa'lumotlar to'g'rimi?",
            'listing_submitted': "<b>✅ E'loningiz muvaffaqiyatli yuborildi!</b>\n\nE'loningiz moderator tekshiruvidan o'tgandan so'ng kanalda e'lon qilinadi.",
            'nothing_to_cancel': "Bekor qilish uchun hech qanday amal mavjud emas.",
            'action_cancelled': "Amal bekor qilindi.",
            
            'announcement': "📢 Yangi kod sotuvda!\n\n💻 Loyiha nomi: {name}\n🔗 Havola: {link}\n🛠 Texnologiyalar: {technologies}\n💵 Narx: ${price}\n📜 Tavsif: {description}\n\n👨‍💻 Dasturchi: {owner}\n\n🔥 @cooplink\n\n{hashtags}",
            
            'new_listing': "<b>Yangi e'lon qo'shildi</b>\n\nFoydalanuvchi: @{username}\nNomi: {name}\nTexnologiyalar: {technologies}\nNarxi: ${price}\n\nTavsif: {description}",
            'your_listing_approved': "<b>✅ Sizning e'loningiz tasdiqlandi!</b>\n\nSizning \"{listing_name}\" nomli e'loningiz moderator tomonidan tasdiqlandi va kanalga joylashtirildi.",
            'your_listing_rejected': "<b>❌ Sizning e'loningiz rad etildi.</b>\n\nSizning \"{listing_name}\" nomli e'loningiz moderator tomonidan rad etildi.",
            
            'approve_button': "✅ Tasdiqlash",
            'reject_button': "❌ Bekor qilish",
        },
        'ru': {
            'welcome': "<b>👋 Здравствуйте, уважаемый пользователь!</b>\n\nДобро пожаловать в бот Cooplink. Пожалуйста, выберите язык интерфейса:",
            'language_selected': "<b>✅ Язык успешно изменен.</b>\n\nИспользуйте кнопки основного меню для работы с ботом.",
            'profile': "<b>👤 Информация о пользователе</b>\n\nID: <code>{user_id}</code>\nUsername: @{username}\nВсего объявлений: {listings_count}",
            'help': "<b>🔍 Руководство по использованию бота</b>\n\nЭтот бот позволяет вам размещать объявления о продаже своих программных продуктов.\n\n<b>Основные команды:</b>\n/start - Запустить бота\n/cancel - Отменить текущее действие\n\nЕсли у вас есть вопросы или предложения, обращайтесь к @y0rdam42.",
            'command_list': "🤖 <b>Команды бота:</b>\n\n/start - Запустить бота\n/cancel - Отменить текущее действие\n/profile - Посмотреть данные профиля\n/help - Помощь",
            'sell_code_start': "<b>📝 Продажа программного продукта</b>\n\nПожалуйста, введите название проекта/кода:",
            
            'admin_panel': "<b>Панель управления администратора</b>\n\nВсего пользователей: {total_users}\nВсего объявлений: {total_listings}",
            'broadcast_prompt': "<b>Введите сообщение для отправки всем пользователям:</b>",
            'broadcast_started': "<b>Отправка сообщения, пожалуйста, подождите...</b>",
            'broadcast_completed': "<b>Отправка сообщений успешно завершена!</b>\n\nОтправлено: {sent} пользователям\nНе удалось отправить: {failed} пользователям",
            'listing_approved': "<b>Объявление #{listing_id} успешно одобрено и опубликовано в канале.</b>",
            'listing_rejected': "<b>Объявление #{listing_id} отклонено.</b>",
            
            'no_users': "<b>В системе нет зарегистрированных пользователей.</b>",
            'users_list': "<b>Общее количество пользователей: {total}</b>\n\n{users}",
            'user_item': "{number}. ID: <code>{id}</code> - @{username} - Язык: {language} - Дата регистрации: {date}\n",
            
            'no_listings': "<b>В системе нет объявлений.</b>",
            'listings_header': "<b>Список всех объявлений</b> (Страница {page}/{total_pages})\n\n",
            'listing_item': "ID: <code>{id}</code> - {name}\nАвтор: @{username}\nЦена: ${price}\nСтатус: {status}\nДата: {date}\n\n",
            'prev_page': "« Предыдущая страница",
            'next_page': "Следующая страница »",
            
            'users_button': "👥 Список пользователей",
            'listings_button': "📋 Список объявлений",
            'broadcast_button': "📣 Отправить массовое сообщение",
            'back_button': "�� Вернуться назад",
            'view_details': "🔍 Просмотреть подробнее",
            'select_listing': "<b>Выберите объявление для просмотра:</b>",
            'listing_details': "<b>Полная информация об объявлении</b>\n\nID: <code>{id}</code>\nНазвание: {name}\nАвтор: @{username}\nЦена: ${price}\nСтатус: {status}\nДата: {date}\n\nСсылка: {link}\nТехнологии: {technologies}\n\nОписание:\n{description}",
            
            'enter_project_link': "<b>Введите ссылку на проект:</b>\n\nВведите ссылку на GitHub, GitLab или другой ресурс.",
            'enter_technologies': "<b>Введите использованные технологии:</b>\n\nНапример: Python, Django, React, PostgreSQL",
            'enter_price': "<b>Введите стоимость продукта:</b>\n\nВведите только число, например: 50 (в USD)",
            'enter_description': "<b>Введите описание проекта:</b>\n\nЗдесь предоставьте подробную информацию о проекте.",
            'enter_image': "<b>Загрузите изображение для проекта:</b>\n\nНажмите кнопку \"Пропустить\", если не хотите загружать изображение.",
            'confirm_listing': "<b>Подтвердите данные объявления:</b>\n\nНазвание: {name}\nСсылка: {link}\nТехнологии: {technologies}\nЦена: ${price}\n\nОписание: {description}\n\nВсе данные указаны верно?",
            'listing_submitted': "<b>✅ Ваше объявление успешно отправлено!</b>\n\nВаше объявление будет опубликовано в канале после проверки модератором.",
            'nothing_to_cancel': "Нет активных действий для отмены.",
            'action_cancelled': "Действие отменено.",
            
            'announcement': "📢 Новый код в продаже!\n\n💻 Название проекта: {name}\n🔗 Ссылка: {link}\n🛠 Технологии: {technologies}\n💵 Цена: ${price}\n📜 Описание: {description}\n\n👨‍💻 Разработчик: {owner}\n\n🔥 @cooplink\n\n{hashtags}",
            
            'new_listing': "<b>Добавлено новое объявление</b>\n\nПользователь: @{username}\nНазвание: {name}\nТехнологии: {technologies}\nЦена: ${price}\n\nОписание: {description}",
            'your_listing_approved': "<b>✅ Ваше объявление одобрено!</b>\n\nВаше объявление \"{listing_name}\" было одобрено модератором и опубликовано в канале.",
            'your_listing_rejected': "<b>❌ Ваше объявление отклонено.</b>\n\nВаше объявление \"{listing_name}\" было отклонено модератором.",
            
            'approve_button': "✅ Подтвердить",
            'reject_button': "❌ Отклонить",
        },
        'en': {
            'welcome': "<b>👋 Greetings, esteemed user!</b>\n\nWelcome to Cooplink bot. Please select your preferred interface language:",
            'language_selected': "<b>✅ Language has been successfully changed.</b>\n\nPlease use the main menu buttons to interact with the bot.",
            'profile': "<b>👤 User Information</b>\n\nID: <code>{user_id}</code>\nUsername: @{username}\nTotal listings: {listings_count}",
            'help': "<b>🔍 Bot Usage Guide</b>\n\nThis bot allows you to post listings to sell your programming products.\n\n<b>Main commands:</b>\n/start - Start the bot\n/cancel - Cancel current operation\n\nIf you have any questions or suggestions, please contact @y0rdam42.",
            'command_list': "🤖 <b>Bot commands:</b>\n\n/start - Start the bot\n/cancel - Cancel current operation\n/profile - View profile information\n/help - Help",
            'sell_code_start': "<b>📝 Sell Programming Product</b>\n\nPlease enter the project/code name:",
            
            'admin_panel': "<b>Administrator Control Panel</b>\n\nTotal Users: {total_users}\nTotal Listings: {total_listings}",
            'broadcast_prompt': "<b>Please enter the message to broadcast to all users:</b>",
            'broadcast_started': "<b>Sending messages, please wait...</b>",
            'broadcast_completed': "<b>Message broadcasting successfully completed!</b>\n\nSent to: {sent} users\nFailed: {failed} users",
            'listing_approved': "<b>Listing #{listing_id} has been successfully approved and published to the channel.</b>",
            'listing_rejected': "<b>Listing #{listing_id} has been rejected.</b>",
            
            'no_users': "<b>There are no registered users in the system.</b>",
            'users_list': "<b>Total number of users: {total}</b>\n\n{users}",
            'user_item': "{number}. ID: <code>{id}</code> - @{username} - Language: {language} - Registration date: {date}\n",
            
            'no_listings': "<b>There are no listings in the system.</b>",
            'listings_header': "<b>List of all listings</b> (Page {page}/{total_pages})\n\n",
            'listing_item': "ID: <code>{id}</code> - {name}\nAuthor: @{username}\nPrice: ${price}\nStatus: {status}\nDate: {date}\n\n",
            'prev_page': "« Previous page",
            'next_page': "Next page »",
            
            'users_button': "👥 User List",
            'listings_button': "📋 Listings List",
            'broadcast_button': "📣 Send Mass Message",
            'back_button': "🔙 Return",
            'view_details': "🔍 View Details",
            'select_listing': "<b>Select a listing to view:</b>",
            'listing_details': "<b>Complete Listing Information</b>\n\nID: <code>{id}</code>\nName: {name}\nAuthor: @{username}\nPrice: ${price}\nStatus: {status}\nDate: {date}\n\nLink: {link}\nTechnologies: {technologies}\n\nDescription:\n{description}",
            
            'enter_project_link': "<b>Enter project link:</b>\n\nPlease provide a link to GitHub, GitLab, or another resource.",
            'enter_technologies': "<b>Enter technologies used:</b>\n\nFor example: Python, Django, React, PostgreSQL",
            'enter_price': "<b>Enter product price:</b>\n\nPlease enter only a number, e.g.: 50 (in USD)",
            'enter_description': "<b>Enter project description:</b>\n\nPlease provide detailed information about the project here.",
            'enter_image': "<b>Upload an image for the project:</b>\n\nPress the \"Skip\" button if you do not wish to upload an image.",
            'confirm_listing': "<b>Confirm listing details:</b>\n\nName: {name}\nLink: {link}\nTechnologies: {technologies}\nPrice: ${price}\n\nDescription: {description}\n\nIs all information correct?",
            'listing_submitted': "<b>✅ Your listing has been successfully submitted!</b>\n\nYour listing will be published in the channel after review by a moderator.",
            'nothing_to_cancel': "There are no active operations to cancel.",
            'action_cancelled': "Operation cancelled.",
            
            'announcement': "📢 New code for sale!\n\n💻 Project name: {name}\n🔗 Link: {link}\n🛠 Technologies: {technologies}\n💵 Price: ${price}\n📜 Description: {description}\n\n👨‍💻 Developer: {owner}\n\n🔥 @cooplink\n\n{hashtags}",
            
            'new_listing': "<b>New listing added</b>\n\nUser: @{username}\nName: {name}\nTechnologies: {technologies}\nPrice: ${price}\n\nDescription: {description}",
            'your_listing_approved': "<b>✅ Your listing has been approved!</b>\n\nYour listing \"{listing_name}\" has been approved by a moderator and published to the channel.",
            'your_listing_rejected': "<b>❌ Your listing has been rejected.</b>\n\nYour listing \"{listing_name}\" has been rejected by a moderator.",
            
            'approve_button': "✅ Approve",
            'reject_button': "❌ Reject",
        }
    }
    
    lang_dict = texts.get(language, texts['uz'])
    string = lang_dict.get(key)
    
    if string is None:
        if key.startswith('btn_'):
            button_key = key.replace('btn_', '')
            try:
                string = Button.get_text(button_key, language)
            except:
                string = f"Missing string: {key}"
        else:
            string = f"Missing string: {key}"
    
    return string