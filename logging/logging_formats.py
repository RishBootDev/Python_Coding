
import logging as log

import logging as log

log.basicConfig(
    level=log.DEBUG,
    format="%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


log.debug("Good , the logs are clear")