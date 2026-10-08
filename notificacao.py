import subprocess

titulo = 'Aviso'
mensagem = 'Hora de estudar python'

subprocess.run([
    "notify-send",
    titulo,
    mensagem
])
