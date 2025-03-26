from aiogram.fsm.state import State, StatesGroup

class Button:
    UZBEK = "uzbek"
    RUSSIAN = "russian"
    CHANGE_LANGUAGE = "change_language"
    PROFILE = "profile"
    SELL_CODE = "sell_code"
    HELP = "help"
    SKIP = "skip"
    YES = "yes"
    NO = "no"
    CONFIRM = "confirm"
    CANCEL = "cancel"
    
    @staticmethod
    def get_text(button, lang):
        texts = {
            'uz': {
                Button.UZBEK: "🇺🇿 O'zbek tili",
                Button.RUSSIAN: "🇷🇺 \u0420\u0443\u0441\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a",
                Button.CHANGE_LANGUAGE: "🔄 Tilni o'zgartirish",
                Button.PROFILE: "👤 Mening profilim",
                Button.SELL_CODE: "💰 Kodimni sotish",
                Button.HELP: "❓ Yordam",
                Button.SKIP: "⏭ O'tkazib yuborish",
                Button.YES: "✅ Ha",
                Button.NO: "❌ Yo'q",
                Button.CONFIRM: "✅ Tasdiqlash",
                Button.CANCEL: "❌ Bekor qilish"
            },
            'ru': {
                Button.UZBEK: "🇺🇿 O'zbek tili",
                Button.RUSSIAN: "🇷🇺 \u0420\u0443\u0441\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a",
                Button.CHANGE_LANGUAGE: "🔄 \u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u044f\u0437\u044b\u043a",
                Button.PROFILE: "👤 \u041c\u043e\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u044c",
                Button.SELL_CODE: "💰 \u041f\u0440\u043e\u0434\u0430\u0442\u044c \u043a\u043e\u0434",
                Button.HELP: "❓ \u041f\u043e\u043c\u043e\u0449\u044c",
                Button.SKIP: "⏭ \u041f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c",
                Button.YES: "✅ \u0414\u0430",
                Button.NO: "❌ \u041d\u0435\u0442",
                Button.CONFIRM: "✅ \u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c",
                Button.CANCEL: "❌ \u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c"
            }
        }
        return texts.get(lang, texts['uz']).get(button, f"Unknown button: {button}")

class ButtonText:
    UZBEK = Button.get_text(Button.UZBEK, 'uz')
    RUSSIAN = Button.get_text(Button.RUSSIAN, 'ru')
    CHANGE_LANGUAGE_UZ = Button.get_text(Button.CHANGE_LANGUAGE, 'uz')
    CHANGE_LANGUAGE_RU = Button.get_text(Button.CHANGE_LANGUAGE, 'ru')
    PROFILE_UZ = Button.get_text(Button.PROFILE, 'uz')
    PROFILE_RU = Button.get_text(Button.PROFILE, 'ru')
    SELL_CODE_UZ = Button.get_text(Button.SELL_CODE, 'uz')
    SELL_CODE_RU = Button.get_text(Button.SELL_CODE, 'ru')
    HELP_UZ = Button.get_text(Button.HELP, 'uz')
    HELP_RU = Button.get_text(Button.HELP, 'ru')
    SKIP_UZ = Button.get_text(Button.SKIP, 'uz')
    SKIP_RU = Button.get_text(Button.SKIP, 'ru')
    YES_UZ = Button.get_text(Button.YES, 'uz')
    YES_RU = Button.get_text(Button.YES, 'ru')
    NO_UZ = Button.get_text(Button.NO, 'uz')
    NO_RU = Button.get_text(Button.NO, 'ru')
    CONFIRM_UZ = Button.get_text(Button.CONFIRM, 'uz')
    CONFIRM_RU = Button.get_text(Button.CONFIRM, 'ru')
    CANCEL_UZ = Button.get_text(Button.CANCEL, 'uz')
    CANCEL_RU = Button.get_text(Button.CANCEL, 'ru')

class Language:
    UZBEK = "uz"
    RUSSIAN = "ru"

class Channel:
    COOPLINK = "@cooplink"

class Config:
    DEFAULT_LANGUAGE = Language.UZBEK
    AVAILABLE_LANGUAGES = [Language.UZBEK, Language.RUSSIAN]

class LanguageSelection(StatesGroup):
    waiting_for_language = State()