import os

import environ

from project.settings.constants.paths import BASE_DIR

ENV = environ.Env()
env_path = ENV.str("ENV_PATH", os.path.join(BASE_DIR, ".env"))
if os.path.exists(env_path):
    ENV.read_env(env_path)
