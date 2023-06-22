import logging
from logdna import LogDNAHandler
import os

key=os.environ['MEZMO_INGESTION_KEY']

log = logging.getLogger()
log.setLevel(logging.INFO)

options = {
    "index_meta": True,
    "custom_fields": "meta"
}

mezmo_handler = LogDNAHandler(key, options)

log.addHandler(mezmo_handler)

