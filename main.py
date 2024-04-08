import pyttsx3

def speak(text):
    engine = pyttsx3.init()  # Inicializa o motor de TTS
    voices = engine.getProperty('voices')
    for voice in voices:
        # Verifica se a lista de idiomas existe e não está vazia antes de acessar
        if voice.languages and 'pt' in voice.languages[0]:  
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 150)  # Velocidade da fala
    engine.say(text)
    engine.runAndWait()

# Exemplo de uso
speak("Olá, este é um teste do sistema de conversão de texto em fala.")
