# **🧠 IQonsulting AI Assistant**
  
<br>
An interactive AI-driven assistant designed to provide pre- and post-operative guidance for patients. This tool leverages speech recognition and text-to-speech technologies to facilitate seamless patient interactions.

<br>
<br>
<br>

**📁 Project Structure**

```IQonsulting/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── tts/
│   │   ├── __init__.py
│   │   └── google_tts.py
│   ├── asr/
│   │   ├── __init__.py
│   │   └── parakeet_asr.py
│   └── utils/
│       ├── __init__.py
│       └── audio_utils.py
├── requirements.txt
└── README.md
```

**🚀 Features**
<br>
<br>
<br>
**Speech-to-Text (ASR):** Utilizes NVIDIA's Parakeet TDT 0.6b v2 model for accurate transcription of patient speech.
<br>
<br>
**Text-to-Speech (TTS):** Employs Google Cloud Text-to-Speech API to deliver responses in a natural, synthesized voice.
<br>
<br>
**Real-time Interaction:** Facilitates dynamic conversations between patients and the AI assistant.
<br>
<br>
**Modular Design:** Structured for easy integration and scalability within virtual machine environments.
