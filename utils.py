import os
import re
import base64
import gzip
import io
import json
from datetime import datetime


def benedictus_ascii_art():
  alexandria = r"""
     _____      _ _  ____           _      _ 
    |  ___|   _| | |/ ___|   _  ___| | ___(_)
    | |_ | | | | | | |  | | | |/ __| |/ _ \ |
    |  _|| |_| | | | |__| |_| | (__| |  __/ |
    |_|   \__,_|_|_|\____\__, |\___|_|\___|_|
                        |___/               
  Author: Bendictus | Jão
  Community: https://t.me/+7imfib1o0CQwNmUx5
  Script: {name}
  Version: {version}
  """
  print(alexandria.format(name='fu11cyclei', version='Alpha 0.1'))


def clear_screen():
  os.system('cls || clear')


def create_folder(folder_name):
  path = os.path.join(os.getcwd(), folder_name)

  if not os.path.exists(path):
    os.mkdir(path)

  return path


def clear_folder_name(name, is_file=None, ext=''):
  if is_file:
    name, ext = os.path.splitext(name)
  sanitized_base = re.sub(r'[<>:."/\\|?*]|\s+|\.$', ' ', name).strip()
  return sanitized_base + ext if ext else sanitized_base


def decode_content(token):
  decoded_new_data = base64.b64decode(token)

  with gzip.GzipFile(fileobj=io.BytesIO(decoded_new_data)) as f:
    decompressed_new_data = f.read()

  result = decompressed_new_data.decode('utf-8')
  result = json.loads(result)
  return result


def log_to_file(filename, message):
  timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
  with open(filename, 'a', encoding='UTF-8') as file:
    file.write(f'{timestamp} - {message}\n')


def logger(message, error=None, warning=None):
  if error:
    log_to_file('fullcyclei_erros.txt', message)
  if warning:
    log_to_file('fullcyclei_avisos.txt', message)


def shorten_folder_name(full_path, max_length=241):
  if len(full_path) <= max_length:
    return full_path
  directory, file_name = os.path.split(full_path)
  base_name, extension = os.path.splitext(file_name)
  base_name = base_name[:max_length - len(directory) - len(extension) - 1]
  return os.path.join(directory, base_name + extension)
