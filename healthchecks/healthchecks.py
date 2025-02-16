#!/usr/local/bin/python3

import argparse
import requests

def send_healthcheck(url) -> bool:
  """
  Sends notifications to healthchecks.io
  """
  # Retry up to 5 times
  retry_count = 0
  while True:
    response = requests.get(url, timeout = 5)
    if retry_count < 5 and response and not response.ok:
      retry_count+=1
      continue
    break

  return response.ok

parser = argparse.ArgumentParser()
parser.add_argument('--healthcheck-url', help='URL for healthcheck', type=str, required=True)
arguments = parser.parse_args()

send_healthcheck(arguments.healthcheck_url)
