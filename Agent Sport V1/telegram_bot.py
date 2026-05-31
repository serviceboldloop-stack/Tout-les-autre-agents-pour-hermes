"""
Bot Telegram — Agent Sport V1 (Lucas)
Appel direct API Anthropic avec token OAuth (abonnement Claude Pro)
Pas de CLI, pas de tokens payants separement.
"""

import json
import logging
import asyncio
import urllib.request
import urllib.parse
from pathlib import Path
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes

# ─── CONFIG ───────────────────────────────────────────────────────────────────

BOT_TOKEN = "8872094803:AAGA2quUl49xPTAJR6R1AiKcfA4T01s4XPY"
AGENT_DIR = Path(r"C:\Users\chapo\Documents\01_Agent Personnaliser\Agent Sport V1")
CREDENTIALS_FILE = Path(r"C:\Users\chapo\.claude\.credentials.json")
AUTHORIZED_CHAT_ID = 7579717556  # Lucas

ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-sonnet-4-5"

# ─── LOGGING ──────────────────────────────────────────────────────────────────

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ─── CHARGE LE CONTEXTE ───────────────────────────────────────────────────────

def load_file(relative_path: str) -> str:
    full = AGENT_DIR / relative_path
    if full.exists():
        return full.read_text(encoding="utf-8")
    return f"[Fichier introuvable : {relative_path}]"

def build_system_prompt() -> str:
    claude_md     = load_file("CLAUDE.md")
    profil        = load_file("Context/profil.md")
    programme     = load_file("Context/programme_muscu.md")
    memory        = load_file("Memory/base_memory.md")
    progression   = load_file("Data/progression.md")

    return f"""Tu es l'Agent Sport V1 de Lucas — coach sportif complet (nutrition, musculation, football).

=== CLAUDE.md (instructions systeme) ===
{claude_md}

=== PROFIL LUCAS (profil.md) ===
{profil}

=== PROGRAMME MUSCU (programme_muscu.md) ===
{programme}

=== MEMOIRE TERRAIN (base_memory.md) ===
{memory}

=== PROGRESSION (progression.md) ===
{progression}

---
IMPORTANT : Tu reponds en francais. Reponses courtes et denses. Chiffres concrets toujours.
Lucas parle en voix-to-text donc ses messages peuvent avoir des fautes — interprete le sens."""

# ─── RECUPERE LE TOKEN OAUTH ──────────────────────────────────────────────────

def get_oauth_token() -> str:
    creds = json.loads(CREDENTIALS_FILE.read_text(encoding="utf-8"))
    return creds["claudeAiOauth"]["accessToken"]

# ─── APPEL API ANTHROPIC ──────────────────────────────────────────────────────

def call_anthropic(user_message: str, system_prompt: str) -> str:
    token = get_oauth_token()

    payload = json.dumps({
        "model": MODEL,
        "max_tokens": 2048,
        "system": system_prompt,
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }).encode("utf-8")

    req = urllib.request.Request(
        ANTHROPIC_API_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "x-api-key": token,
            "anthropic-version": "2023-06-01"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result["content"][0]["text"]
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        logger.error(f"API Error {e.code}: {body}")
        return f"Erreur API {e.code} : {body}"
    except Exception as e:
        logger.error(f"Erreur appel API : {e}")
        return f"Erreur : {str(e)}"

# ─── HELPERS ──────────────────────────────────────────────────────────────────

async def send_long_message(update: Update, text: str):
    max_len = 4000
    if len(text) <= max_len:
        await update.message.reply_text(text)
        return
    chunks = []
    while text:
        if len(text) <= max_len:
            chunks.append(text)
            break
        split_at = text.rfind("\n", 0, max_len)
        if split_at == -1:
            split_at = max_len
        chunks.append(text[:split_at])
        text = text[split_at:].lstrip("\n")
    for i, chunk in enumerate(chunks):
        if i > 0:
            chunk = f"(suite {i+1}/{len(chunks)})\n\n" + chunk
        await update.message.reply_text(chunk)

def is_authorized(chat_id: int) -> bool:
    return chat_id == AUTHORIZED_CHAT_ID

# ─── HANDLERS ─────────────────────────────────────────────────────────────────

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Agent Sport V1 actif !\n\n"
        "Commandes :\n"
        "/seance - seance du jour\n"
        "/nutri - coaching nutrition\n"
        "/help - aide\n\n"
        "Ou envoie n'importe quel message."
    )

async def cmd_seance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_authorized(update.effective_chat.id):
        return
    await update.message.reply_text("Generation de la seance du jour...")
    system = build_system_prompt()
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, call_anthropic, "seance du jour", system)
    await send_long_message(update, response)

async def cmd_nutri(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_authorized(update.effective_chat.id):
        return
    await update.message.reply_text("Coaching nutrition en cours...")
    system = build_system_prompt()
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, call_anthropic, "coach nutri", system)
    await send_long_message(update, response)

async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commandes :\n"
        "/seance - seance du jour\n"
        "/nutri - coaching nutrition\n"
        "/start - accueil\n\n"
        "Messages libres :\n"
        "- 'coach muscu'\n"
        "- 'coach foot'\n"
        "- 'note mes perfs 18kg x 12/12/10'\n"
        "- 'je stagne'\n"
        "- 'check semaine'"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_authorized(update.effective_chat.id):
        await update.message.reply_text("Acces non autorise.")
        return

    user_message = update.message.text
    logger.info(f"Message : {user_message[:60]}")

    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    await update.message.reply_text("...")

    system = build_system_prompt()
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, call_anthropic, user_message, system)
    await send_long_message(update, response)

# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    print("Agent Sport V1 -- Bot Telegram (API directe)")
    print(f"Repertoire : {AGENT_DIR}")
    print("Bot demarre. Ctrl+C pour arreter.")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("seance", cmd_seance))
    app.add_handler(CommandHandler("nutri", cmd_nutri))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
