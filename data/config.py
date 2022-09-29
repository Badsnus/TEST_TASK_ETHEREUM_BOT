from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = [int(i) for i in env.list("ADMINS")]
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

DATABASE_URL = f'sqlite:///{env.str("data_base_name")}'

ETHERSCAN_API_KEY = env.str('ETHERSCAN_API_KEY')

seed_words = [i.replace("\n", "") for i in open('seed_words')]