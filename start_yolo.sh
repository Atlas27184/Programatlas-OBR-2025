#!/bin/bash
# Ativa o ambiente virtual e roda o programa YOLO

cd ~
source yolovenv/bin/activate

# Instala dependências se ainda não estiverem instaladas
pip install bleak ultralytics opencv-python --quiet

# Vai para a pasta onde está o código
cd /home/gabriel/

# Executa o script principal
python3 Teste.py

