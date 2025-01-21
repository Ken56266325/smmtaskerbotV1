from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8091510056:AAHpsxNDeLYmf_itaZlH1lZjrhibk7z0Qow"

# Code d'accès
ACCESS_CODE = "562663251106"

# Utilisateurs autorisés
authorized_users = set()

# File IDs pour les tutoriels
FILE_ID_API = "BAACAgQAAxkBAAMIZ48qXQABLhFcykn_ilJJB2lsXxwaAAJDGAACfYt4UMtzzzIkXBU0NgQ"
FILE_ID_INSTAGRAM = "BAACAgQAAxkBAAOSZ49BbSALt1PkvQWGl7nQcA1Gfc4AAksYAAJ9i3hQZcy2EkQ3Rpw2BA"
FILE_ID_TASK = "BAACAgQAAxkBAAOSZ49BbSALt1PkvQWGl7nQcA1Gfc4AAksYAAJ9i3hQZcy2EkQ3Rpw2BA"
FILE_ID_ERRORS = "BAACAgQAAxkBAAOSZ49BbSALt1PkvQWGl7nQcA1Gfc4AAksYAAJ9i3hQZcy2EkQ3Rpw2BA"
FILE_ID_INSTALLATION_1 = "BAACAgQAAxkBAAMIZ48qXQABLhFcykn_ilJJB2lsXxwaAAJDGAACfYt4UMtzzzIkXBU0NgQ"
FILE_ID_INSTALLATION_2 = "BAACAgQAAxkBAAOSZ49BbSALt1PkvQWGl7nQcA1Gfc4AAksYAAJ9i3hQZcy2EkQ3Rpw2BA"
FILE_ID_ZIP = "file_id_du_fichier_zip"  # Ajoutez ici l'ID du fichier ZIP

# Fonction pour démarrer le bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id in authorized_users:
        # Si l'utilisateur est déjà autorisé, afficher le menu principal
        await show_main_menu(update)
    else:
        # Sinon, demander le code d'accès
        await update.message.reply_text("🔒 Veuillez entrer le code d'accès pour utiliser ce bot :")

# Vérification du code d'accès
async def handle_access_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    if user_id not in authorized_users:
        if text == ACCESS_CODE:
            authorized_users.add(user_id)
            await update.message.reply_text("✅ Accès accordé !")
            await show_main_menu(update)
        else:
            await update.message.reply_text("❌ Code incorrect. Veuillez réessayer :")
    else:
        # Si l'utilisateur est déjà autorisé, gérer son choix
        await handle_choice(update, context)

# Afficher le menu principal
async def show_main_menu(update: Update):
    keyboard = [
        ["📖 Voir des Tuto", "⚙️ Gérer des IDs (en cours)"],
        ["📞 Contacter le service client"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
    await update.message.reply_text(
        "👋 Bienvenue sur Smmtaskerbot !\n\n"
        "Choisissez une option ci-dessous :",
        reply_markup=reply_markup
    )

# Gestion des choix basés sur le clavier
async def handle_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📖 Voir des Tuto":
        # Ajouter le message informatif
        await update.message.reply_text(
            "⚠️ Si vous êtes un nouvel utilisateur ou que vous souhaitez effectuer une mise à jour, "
            "veuillez d'abord consulter le tutoriel d'installation avant de continuer."
        )

        keyboard = [
            ["📋 API Hash & API ID Telegram", "📋 Ajouter un compte Instagram"],
            ["📋 Lancer une tâche", "📋 Gérer les erreurs"],
            ["📋 Tutoriels d'installation"],
            ["⬅️ Retour au menu principal"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
        await update.message.reply_text("📖 Choisissez un tutoriel :", reply_markup=reply_markup)

    elif text == "⬅️ Retour au menu principal":
        await show_main_menu(update)

    elif text == "⚙️ Gérer des IDs (en cours)":
        await update.message.reply_text("⚙️ La gestion des IDs est en cours de développement.")

    elif text == "📞 Contacter le service client":
        keyboard = [["⬅️ Retour au menu principal"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
        await update.message.reply_text(
            "📞 Pour contacter le service client, envoyez un message à @kenny56266.",
            reply_markup=reply_markup
        )

    elif text == "📋 API Hash & API ID Telegram":
        keyboard = [["⬅️ Retour au menu principal"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
        await update.message.reply_video(FILE_ID_API, caption="📋 Voici le tuto pour obtenir l'API Hash et API ID Telegram.", reply_markup=reply_markup)

    elif text == "📋 Ajouter un compte Instagram":
        keyboard = [["⬅️ Retour au menu principal"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
        await update.message.reply_video(FILE_ID_INSTAGRAM, caption="📋 Voici le tuto pour ajouter un compte Instagram.", reply_markup=reply_markup)

    elif text == "📋 Lancer une tâche":
        keyboard = [["⬅️ Retour au menu principal"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
        await update.message.reply_video(FILE_ID_TASK, caption="📋 Voici le tuto pour lancer une tâche.", reply_markup=reply_markup)

    elif text == "📋 Gérer les erreurs":
        keyboard = [["⬅️ Retour au menu principal"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
        await update.message.reply_video(FILE_ID_ERRORS, caption="📋 Voici le tuto pour gérer les erreurs.", reply_markup=reply_markup)

    elif text == "📋 Tutoriels d'installation":
        keyboard = [["⬅️ Retour au menu principal"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
        await update.message.reply_video(FILE_ID_INSTALLATION_1, caption="📋 Tutoriel d'installation - Partie 1.")
        await update.message.reply_video(FILE_ID_INSTALLATION_2, caption="📋 Tutoriel d'installation - Partie 2.")
        await update.message.reply_document(FILE_ID_ZIP, caption="📂 Voici le fichier ZIP pour l'installation.")
        await update.message.reply_text("⬅️ Utilisez le bouton ci-dessous pour revenir au menu principal.", reply_markup=reply_markup)

# Création de l'application
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_access_code))

    print("Bot démarré...")
    app.run_polling()

if __name__ == "__main__":
    main()
