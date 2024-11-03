import pyautogui
import time

# Pressione a tecla Win para abrir o menu Iniciar
pyautogui.press("win")
time.sleep(1)  # Aguarde um pouco para o menu abrir

# Digite "notepad" para pesquisar o Bloco de Notas
pyautogui.write("notepad", interval=0.1)
time.sleep(1)  # Aguarde para o Notepad aparecer na busca

# Pressione Enter para abrir o Bloco de Notas
pyautogui.press("enter")
