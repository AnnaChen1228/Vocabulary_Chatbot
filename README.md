# Vocabulary Chatbot 🤖

A LINE Bot designed to make vocabulary learning interactive, engaging, and effective through deliberate practice and immediate feedback.

## 🎥 Project Resources
- [Video Demo](https://drive.google.com/file/d/17FuSzyucJa-QZTufxuhMYEbH6EggwXWJ/view?usp=sharing)
- [Project Slides](https://www.canva.com/design/DAGHcck4eTs/mkRmwR2Pb38IMp-zkFVg2w/edit?utm_content=DAGHcck4eTs&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## 🎯 Motivation & Core Concepts

### Why This Project?
- 📚 Learning a new language requires consistent effort and repetitive practice
- 😴 Traditional memorization methods are monotonous and lack interaction
- 🤖 A LINE-based ChatBOT system provides interactive vocabulary learning
- 🎯 Aims to help learners master vocabulary through engaging and effective methods

### Key Learning Principles
1. **Deliberate Practice** 
   - Structured and purposeful practice
   - Focus on specific learning goals

2. **Elaboration**
   - Connecting new words with context
   - Creating meaningful associations

3. **Immediate Feedback**
   - Real-time corrections
   - Progress tracking

4. **Personalization**
   - Adaptive learning pace
   - Individual progress tracking

## 📁 Project Structure
```
.
├── README.md                    # Project documentation
├── Vocabulary.pdf              # Vocabulary reference document
├── build.sh                    # Build script for deployment
├── excel.py                    # Excel data processing module
├── high_school_eng_word.docx   # High school English vocabulary dataset
├── main.py                     # Main application entry point (LINE Bot configuration)
├── read.py                     # File reading utilities
├── requirements.txt            # Project dependencies
├── sentence.py                 # Sentence generation module
├── test.py                     # Testing module
└── vercel.json                 # Vercel deployment configuration
```

## ⚙️ Configuration

### LINE Bot Setup
1. Create a LINE Developer account and create a new channel
2. In `main.py`, configure your LINE Bot credentials:
```python
# LINE Bot configuration
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')
```

> ⚠️ Important: Never commit your actual LINE Bot credentials to public repositories. Use environment variables or configuration files for sensitive data.

## 🚀 Getting Started

1. Clone the repository
```bash
git clone [repository-url]
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure LINE Bot credentials in main.py
```python
# Replace with your LINE Bot credentials
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')
```

4. Run the application
```bash
python main.py
```

## 🎮 System Features

### Interactive Learning
- 💬 Conversational interface
- 🎯 Immediate feedback
- 📝 Example sentences
- 👤 Personalized learning experience

### User Interface
- 📱 Clean and intuitive LINE interface
- 🔄 Easy navigation
- 📊 Progress visualization

### Testing System
- ✍️ Vocabulary quizzes
- 📈 Progress tracking
- 🎯 Performance analytics

### Feedback System
- ✅ Immediate corrections
- 💡 Learning suggestions
- 📊 Progress reports

## 🔮 Future Enhancements

- 🎙️ Voice recognition integration
- 📱 Enhanced mobile features
- 🌍 Multi-language support
- 🤖 Advanced AI interactions
- 📊 Detailed analytics dashboard

## 📞 Contact

For any questions or suggestions, please feel free to reach out:
- 📧 Email: angelachen572@gmail.com
- 🎥 Project Demo: [Watch Video](https://drive.google.com/file/d/17FuSzyucJa-QZTufxuhMYEbH6EggwXWJ/view?usp=sharing)
- 📊 Presentation: [View Slides](https://www.canva.com/design/DAGHcck4eTs/mkRmwR2Pb38IMp-zkFVg2w/edit?utm_content=DAGHcck4eTs&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
