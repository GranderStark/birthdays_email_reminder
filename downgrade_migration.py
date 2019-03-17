from alembic import command
from alembic.config import Config
import sys

alembic_cfg = Config('alembic.ini')
if sys.argv:
    try:
        command.downgrade(alembic_cfg, sys.argv[1])
    except Exception:
        pass
