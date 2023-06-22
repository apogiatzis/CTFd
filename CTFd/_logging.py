import logging
import os

from logdna import LogDNAHandler

key = os.environ["MEZMO_INGESTION_KEY"]

log = logging.getLogger()
log.setLevel(logging.INFO)

options = {"index_meta": True, "custom_fields": "meta"}

mezmo_handler = LogDNAHandler(key, options)

log.addHandler(mezmo_handler)
